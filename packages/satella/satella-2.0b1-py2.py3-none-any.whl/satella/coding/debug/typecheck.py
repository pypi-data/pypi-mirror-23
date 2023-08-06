# coding=UTF-8
"""
Decorator for debug-time typechecking
"""
from __future__ import print_function, absolute_import, division
import six
import inspect
import logging
import itertools
try:
    import typing
except ImportError:
    from backports import typing
import types
from collections import namedtuple
import functools

logger = logging.getLogger(__name__)

List = typing.List
Tuple = typing.Tuple
Dict = typing.Dict
NewType = typing.NewType
Callable = typing.Callable
Sequence = typing.Sequence
TypeVar = typing.TypeVar
Generic = typing.Generic
Mapping = typing.Mapping
Iterable = typing.Iterable
Union = typing.Union
Any = typing.Any
Optional = typing.Optional


# Internal tokens - only instances will be
class _NotGiven(object):
    pass
class _NoDefault(object):
    pass



_CSArgument = namedtuple('_CSArgument', ('name', 'required','default_value'))

class CSArgument(_CSArgument):
    def __str__(self):
        p = ['Argument '+self.name]
        if not self.required:
            p.append('optional with default %s' % (self.default_value, ))
        return ' '.join(p)

class CSVarargsPlaceholder(CSArgument):
    def __init__(self, name):
        super(CSVarargsPlaceholder, self).__init__('*args', False, ())

class CSKwargsPlaceholder(CSArgument):
    def __init__(self, name):
        super(CSKwargsPlaceholder, self).__init__('**kwargs', False, {})

class TypeErrorReason(object):
    pass


class CSTypeError(TypeError):
    """
    A TypeError exception on steroids
    """
    def __str__(self):
        return 'Problem with argument %s' % (arg.name, )

    def __init__(self, arg):
        """
        :param arg: Argument definition
        :type arg: CSArgument
        """
        super(CSTypeError, self).__init__(str(self))
        self.arg = arg

class CSBadTypeError(CSTypeError):

    def __init__(self, arg, expected, got):
        super(CSBadTypeError, self).__init__(arg)

        self.expected = expected
        self.got = got

    def __str__(self):
        return 'Bad type given for arg %s, expected %s got %s' % (self.arg.name, self.expected, self.got)


class CSNotGivenError(CSTypeError):
    def __str__(self):
        return 'Value for argument %s not given' % (self.arg.name, )


class CSMultipleValuesGivenError(CSTypeError):
    def __str__(self):
        return 'Got multiple values for argument' % (self.arg.name, )


class CallSignature(object):
    """
    Call signature of a callable.
    
    Properties:
      - has_varargs (Bool) - if has varargs
      - has_kwargs (Bool) - if has kwargs
      - locals (Dict[str => CSArgument]) - list of locals this function call will generate
      - pos_args (List[CSArgument)] - list of positional arguments
      - varargs_name (Union[str, None]) - name of varargs argument, or None if not present
      - kwargs_name (Union[str, None]) - name of kwargs argument, or None if not present
    """
    __slots__ = ('has_varargs', 'has_kwargs', 'pos_args', 'locals')

    def count_required_positionals(self):
        return len((a for a in self.pos_args if a.required))

    def __init__(self, callable):
        args, varargs, kwargs, defaults = inspect.getargspec(callable)

        # pad them
        while len(defaults) < len(args):
            defaults = [_NoDefault] + list(defaults)

        # process positionals
        self.pos_args = []
        self.locals = {}
        for arg, default in zip(args, defaults):

            cs_arg = CSArgument(arg,
                                default is _NoDefault,
                                default)
            self.pos_args.append(cs_arg)
            self.locals[arg] = cs_arg

        self.varargs_name = varargs
        if varargs is not None:
            self.has_varargs = True
            self.locals[self.varargs_name] = CSVarargsPlaceholder(self.varargs_name)

        self.kwargs_name = kwargs
        if kwargs is not None:
            self.has_kwargs = True
            self.locals[self.kwargs_name] = CSKwargsPlaceholder(self.kwargs_name)

    def result(self, *args, **kwargs):
        """
        Simulate a function call, see what locals are defined
        
        Return a dict of (local_variable_name => it's value),
        or TypeError

        :param args: function call parameters
        :param kwargs: function call parameters
        :return: dict
        :raise CSTypeError: call would raise a TypeError
        """
        assert len(args) >= self.count_required_positionals()

        locals = {}

        # positional
        for arg, value in itertools.izip_longest(self.pos_args,
                                                 args[:len(self.pos_args)],
                                                 fillvalue=_NotGiven):

            if value is _NotGiven:
                if arg.required:
                    raise CSNotGivenError(arg)
                else:
                    value = arg.default_value

            locals[arg.name] = value

        # varargs
        if self.has_varargs:
            locals[self.varargs_name] = args[len(self.pos_args):]

        # kwargs
        if self.has_kwargs:
            locals[self.kwargs_name] = kwargs

        return locals



def typed(*t_args, **t_kwargs):
    """
    Use like:

        @typed(int, six.text_type)
        def display(times, text):
            ...

    int will automatically include long for checking (Python 3 compatibility)
    If you want to check for None, type (None, )
    None for an argument means "do no checking", (None, ) means "type must be NoneType"
    You can pass tuples or lists to match for multiple types

    :param t_args:
    :param t_kwargs:
    :return:
    """

    def typeinfo_to_tuple_of_types(typeinfo):
        if typeinfo is None:
            return (type(None), )
        elif typeinfo == int and six.PY2:
            return six.integer_types
        else:
            if isinstance(typeinfo, (tuple, list)):
                new_tup = []
                for elem in typeinfo:
                    new_tup.extend(typeinfo_to_tuple_of_types(elem))
                return tuple(new_tup)
            else:
                return (typeinfo, )

    t_args = [(typeinfo_to_tuple_of_types(x) if x is not None else None) for x in t_args]

    def outer(fun):

        if not __debug__:
            return fun

        @functools.wraps(fun)
        def inner(*args, **kwargs):

            if isinstance(fun, types.MethodType):   # instancemethod or classmethod
                cargs = args[1:]
            else:
                cargs = args

            for argument, typedescr in zip(cargs, t_args):

                if typedescr is not None:
                    if not isinstance(argument, typedescr):
                        raise TypeError('Got %s, expected %s' % (argument, typedescr))

            return fun(*args, **kwargs)
        return inner

    return outer

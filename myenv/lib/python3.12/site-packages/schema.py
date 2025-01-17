"""schema is a library for validating Python data structures, such as those
obtained from config-files, forms, external services or command-line
parsing, converted from JSON/YAML (or something else) to Python data-types."""

import re

__version__ = '0.6.7'
__all__ = ['Schema',
           'And', 'Or', 'Regex', 'Optional', 'Use', 'Forbidden', 'Const',
           'SchemaError',
           'SchemaWrongKeyError',
           'SchemaMissingKeyError',
           'SchemaForbiddenKeyError',
           'SchemaUnexpectedTypeError']


class SchemaError(Exception):
    """Error during Schema validation."""

    def __init__(self, autos, errors=None):
        self.autos = autos if type(autos) is list else [autos]
        self.errors = errors if type(errors) is list else [errors]
        Exception.__init__(self, self.code)

    @property
    def code(self):
        """
        Removes duplicates values in auto and error list.
        parameters.
        """
        def uniq(seq):
            """
            Utility function that removes duplicate.
            """
            seen = set()
            seen_add = seen.add
            # This way removes duplicates while preserving the order.
            return [x for x in seq if x not in seen and not seen_add(x)]
        data_set = uniq(i for i in self.autos if i is not None)
        error_list = uniq(i for i in self.errors if i is not None)
        if error_list:
            return '\n'.join(error_list)
        return '\n'.join(data_set)


class SchemaWrongKeyError(SchemaError):
    """Error Should be raised when an unexpected key is detected within the
    data set being."""
    pass


class SchemaMissingKeyError(SchemaError):
    """Error should be raised when a mandatory key is not found within the
    data set being vaidated"""
    pass


class SchemaForbiddenKeyError(SchemaError):
    """Error should be raised when a forbidden key is found within the
    data set being validated, and its value matches the value that was specified"""
    pass


class SchemaUnexpectedTypeError(SchemaError):
    """Error should be raised when a type mismatch is detected within the
    data set being validated."""
    pass


class And(object):
    """
    Utility function to combine validation directives in AND Boolean fashion.
    """
    def __init__(self, *args, **kw):
        self._args = args
        assert set(kw).issubset(['error', 'schema', 'ignore_extra_keys'])
        self._error = kw.get('error')
        self._ignore_extra_keys = kw.get('ignore_extra_keys', False)
        # You can pass your inherited Schema class.
        self._schema = kw.get('schema', Schema)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__,
                           ', '.join(repr(a) for a in self._args))

    def validate(self, data):
        """
        Validate data using defined sub schema/expressions ensuring all
        values are valid.
        :param data: to be validated with sub defined schemas.
        :return: returns validated data
        """
        for s in [self._schema(s, error=self._error,
                               ignore_extra_keys=self._ignore_extra_keys)
                  for s in self._args]:
            data = s.validate(data)
        return data


class Or(And):
    """Utility function to combine validation directives in a OR Boolean
    fashion."""
    def validate(self, data):
        """
        Validate data using sub defined schema/expressions ensuring at least
        one value is valid.
        :param data: data to be validated by provided schema.
        :return: return validated data if not validation
        """
        x = SchemaError([], [])
        for s in [self._schema(s, error=self._error,
                               ignore_extra_keys=self._ignore_extra_keys)
                  for s in self._args]:
            try:
                return s.validate(data)
            except SchemaError as _x:
                x = _x
        raise SchemaError(['%r did not validate %r' % (self, data)] + x.autos,
                          [self._error.format(data) if self._error else None] +
                          x.errors)


class Regex(object):
    """
    Enables schema.py to validate string using regular expressions.
    """
    # Map all flags bits to a more readable description
    NAMES = ['re.ASCII', 're.DEBUG', 're.VERBOSE', 're.UNICODE', 're.DOTALL',
             're.MULTILINE', 're.LOCALE', 're.IGNORECASE', 're.TEMPLATE']

    def __init__(self, pattern_str, flags=0, error=None):
        self._pattern_str = pattern_str
        flags_list = [Regex.NAMES[i] for i, f in  # Name for each bit
                      enumerate('{0:09b}'.format(flags)) if f != '0']

        if flags_list:
            self._flags_names = ', flags=' + '|'.join(flags_list)
        else:
            self._flags_names = ''

        self._pattern = re.compile(pattern_str, flags=flags)
        self._error = error

    def __repr__(self):
        return '%s(%r%s)' % (
            self.__class__.__name__, self._pattern_str, self._flags_names
        )

    def validate(self, data):
        """
        Validated data using defined regex.
        :param data: data to be validated
        :return: return validated data.
        """
        e = self._error

        try:
            if self._pattern.search(data):
                return data
            else:
                raise SchemaError('%r does not match %r' % (self, data), e)
        except TypeError:
            raise SchemaError('%r is not string nor buffer' % data, e)


class Use(object):
    """
    For more general use cases, you can use the Use class to transform
    the data while it is being validate.
    """
    def __init__(self, callable_, error=None):
        assert callable(callable_)
        self._callable = callable_
        self._error = error

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._callable)

    def validate(self, data):
        try:
            return self._callable(data)
        except SchemaError as x:
            raise SchemaError([None] + x.autos,
                              [self._error.format(data)
                               if self._error else None] + x.errors)
        except BaseException as x:
            f = _callable_str(self._callable)
            raise SchemaError('%s(%r) raised %r' % (f, data, x),
                              self._error.format(data)
                              if self._error else None)


COMPARABLE, CALLABLE, VALIDATOR, TYPE, DICT, ITERABLE = range(6)


def _priority(s):
    """Return priority for a given object."""
    if type(s) in (list, tuple, set, frozenset):
        return ITERABLE
    if type(s) is dict:
        return DICT
    if issubclass(type(s), type):
        return TYPE
    if hasattr(s, 'validate'):
        return VALIDATOR
    if callable(s):
        return CALLABLE
    else:
        return COMPARABLE


class Schema(object):
    """
    Entry point of the library, use this class to instantiate validation
    schema for the data that will be validated.
    """
    def __init__(self, schema, error=None, ignore_extra_keys=False):
        self._schema = schema
        self._error = error
        self._ignore_extra_keys = ignore_extra_keys

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._schema)

    @staticmethod
    def _dict_key_priority(s):
        """Return priority for a given key object."""
        if isinstance(s, Forbidden):
            return _priority(s._schema) - 0.5
        if isinstance(s, Optional):
            return _priority(s._schema) + 0.5
        return _priority(s)

    def validate(self, data):
        Schema = self.__class__
        s = self._schema
        e = self._error
        i = self._ignore_extra_keys
        flavor = _priority(s)
        if flavor == ITERABLE:
            data = Schema(type(s), error=e).validate(data)
            o = Or(*s, error=e, schema=Schema, ignore_extra_keys=i)
            return type(data)(o.validate(d) for d in data)
        if flavor == DICT:
            data = Schema(dict, error=e).validate(data)
            new = type(data)()  # new - is a dict of the validated values
            coverage = set()  # matched schema keys
            # for each key and value find a schema entry matching them, if any
            sorted_skeys = sorted(s, key=self._dict_key_priority)
            for key, value in data.items():
                for skey in sorted_skeys:
                    svalue = s[skey]
                    try:
                        nkey = Schema(skey, error=e).validate(key)
                    except SchemaError:
                        pass
                    else:
                        if isinstance(skey, Forbidden):
                            # As the content of the value makes little sense for
                            # forbidden keys, we reverse its meaning:
                            # we will only raise the SchemaErrorForbiddenKey
                            # exception if the value does match, allowing for
                            # excluding a key only if its value has a certain type,
                            # and allowing Forbidden to work well in combination
                            # with Optional.
                            try:
                                nvalue = Schema(svalue, error=e).validate(value)
                            except SchemaError:
                                continue
                            raise SchemaForbiddenKeyError(
                                    'Forbidden key encountered: %r in %r' %
                                    (nkey, data), e)
                        else:
                            try:
                                nvalue = Schema(svalue, error=e,
                                                ignore_extra_keys=i).validate(value)
                            except SchemaError as x:
                                k = "Key '%s' error:" % nkey
                                raise SchemaError([k] + x.autos, [e] + x.errors)
                            else:
                                new[nkey] = nvalue
                                coverage.add(skey)
                                break
            required = set(k for k in s if type(k) not in [Optional, Forbidden])
            if not required.issubset(coverage):
                missing_keys = required - coverage
                s_missing_keys = \
                    ', '.join(repr(k) for k in sorted(missing_keys, key=repr))
                raise \
                    SchemaMissingKeyError('Missing keys: ' + s_missing_keys, e)
            if not self._ignore_extra_keys and (len(new) != len(data)):
                wrong_keys = set(data.keys()) - set(new.keys())
                s_wrong_keys = \
                    ', '.join(repr(k) for k in sorted(wrong_keys, key=repr))
                raise \
                    SchemaWrongKeyError(
                        'Wrong keys %s in %r' % (s_wrong_keys, data),
                        e.format(data) if e else None)

            # Apply default-having optionals that haven't been used:
            defaults = set(k for k in s if type(k) is Optional and
                           hasattr(k, 'default')) - coverage
            for default in defaults:
                new[default.key] = default.default

            return new
        if flavor == TYPE:
            if isinstance(data, s):
                return data
            else:
                raise SchemaUnexpectedTypeError(
                    '%r should be instance of %r' % (data, s.__name__),
                    e.format(data) if e else None)
        if flavor == VALIDATOR:
            try:
                return s.validate(data)
            except SchemaError as x:
                raise SchemaError([None] + x.autos, [e] + x.errors)
            except BaseException as x:
                raise SchemaError(
                    '%r.validate(%r) raised %r' % (s, data, x),
                    self._error.format(data) if self._error else None)
        if flavor == CALLABLE:
            f = _callable_str(s)
            try:
                if s(data):
                    return data
            except SchemaError as x:
                raise SchemaError([None] + x.autos, [e] + x.errors)
            except BaseException as x:
                raise SchemaError(
                    '%s(%r) raised %r' % (f, data, x),
                    self._error.format(data) if self._error else None)
            raise SchemaError('%s(%r) should evaluate to True' % (f, data), e)
        if s == data:
            return data
        else:
            raise SchemaError('%r does not match %r' % (s, data),
                              e.format(data) if e else None)


class Optional(Schema):
    """Marker for an optional part of the validation Schema."""
    _MARKER = object()

    def __init__(self, *args, **kwargs):
        default = kwargs.pop('default', self._MARKER)
        super(Optional, self).__init__(*args, **kwargs)
        if default is not self._MARKER:
            # See if I can come up with a static key to use for myself:
            if _priority(self._schema) != COMPARABLE:
                raise TypeError(
                    'Optional keys with defaults must have simple, '
                    'predictable values, like literal strings or ints. '
                    '"%r" is too complex.' % (self._schema,))
            self.default = default
            self.key = self._schema

    def __hash__(self):
        return hash(self._schema)

    def __eq__(self, other):
        return (self.__class__ is other.__class__ and
                getattr(self, 'default', self._MARKER) ==
                getattr(other, 'default', self._MARKER) and
                self._schema == other._schema)


class Forbidden(Schema):
    def __init__(self, *args, **kwargs):
        super(Forbidden, self).__init__(*args, **kwargs)
        self.key = self._schema


class Const(Schema):
    def validate(self, data):
        super(Const, self).validate(data)
        return data


def _callable_str(callable_):
    if hasattr(callable_, '__name__'):
        return callable_.__name__
    return str(callable_)

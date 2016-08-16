"""
Error heirarchy for stratis cli.
"""

class StratisCliError(Exception):
    """
    Top-level stratis cli error.
    """
    pass


class StratisCliValueError(StratisCliError):
    """ Raised when a parameter has an unacceptable value.

        May also be raised when the parameter has an unacceptable type.
    """
    _FMT_STR = "value '%s' for parameter %s is unacceptable"

    def __init__(self, value, param, msg=None):
        """ Initializer.

            :param object value: the value
            :param str param: the parameter
            :param str msg: an explanatory message
        """
        # pylint: disable=super-init-not-called
        self._value = value
        self._param = param
        self._msg = msg

    def __str__(self): # pragma: no cover
        if self._msg:
            fmt_str = self._FMT_STR + ": %s"
            return fmt_str % (self._value, self._param, self._msg)
        else:
            return self._FMT_STR % (self._value, self._param)


class StratisCliValueUnimplementedError(StratisCliValueError):
    """
    Raised if a parameter is not intrinsically bad but functionality
    is unimplemented for this value.
    """
    pass

class StratisCliUnimplementedError(StratisCliError):
    """
    Raised if a method is temporarily unimplemented.
    """
    pass

class StratisCliKnownBugError(StratisCliError):
    """
    Raised if a method is unimplemented due to a bug.
    """
    pass

class StratisCliRuntimeError(StratisCliError):
    """
    Raised if there was a failure due to a RuntimeError.
    """

    def __init__(self, rc, message):
        """ Initializer.

            :param object value: the value
            :param str param: the parameter
            :param str msg: an explanatory message
        """
        # pylint: disable=super-init-not-called
        self.rc = rc
        self.message = message

    def __str__(self):
        return "%s: %s" % (self.rc, self.message)

class StratisCliImpossibleError(StratisCliError):
    """
    Raised when a should be logically impossible situation is encountered.
    """
    pass

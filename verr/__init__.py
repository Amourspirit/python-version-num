# coding: utf-8
__version__ = "1.1.0"
# coding: utf-8

from enum import Enum
from typing import Optional, Tuple, Union
# region Error Classes


class ArgumentError(ValueError):
    '''The error that is raised when one of the arguments provided to a method is not valid.'''


class ArgumentNullError(ValueError):
    '''The error that is raised when a null reference is passed to a method that does not accept it as a valid argument.'''


class ArgumentOutOfRangeError(IndexError):
    '''The error that is raised when the value of an argument is outside the allowable range of values as defined by the invoked method.'''


class FormatError(ValueError):
    '''The error that is raised when the format of an argument is invalid, or when a composite format string is not well formed.'''


# endregion Error Classes
class Version(dict):
    '''
    Represents the version number. This class cannot be extended.
    
    Remarks:
        Version instances can be compared usins `=`, `<`, `<=`, `>`, `>=`, `!=`
    '''
    # region Internal Classes
    class ParseFailureKind(Enum):
        NONE = 0
        ARGUMENT_NULL_ERR = 1
        ARGUMENT_ERR = 2
        ARGUMENT_OUT_OF_RANGE_ERR = 3
        FORMAT_ERR = 4

    class VersionResult:
        def __init__(self):
            self._parsed_version = None  # Version
            # Version.ParseFailureKind
            self._failure: Version.ParseFailureKind = Version.ParseFailureKind.NONE
            self._exception_argument = None  # str
            self._argument_name = ''  # str
            self._can_throw = False  # bool

        def init(self, argument_name: str, can_throw: bool):
            self._can_throw = can_throw
            self._argument_name = argument_name

        def set_failure(self, failure: 'Version.ParseFailureKind', argument: str = ""):
            self._failure = failure
            self._exception_argument = argument
            if self._can_throw:
                raise self.get_version_parse_exception()

        def get_version_parse_exception(self):
            if self._failure == Version.ParseFailureKind.ARGUMENT_NULL_ERR:
                return ArgumentNullError(self._argument_name)
            if self._failure == Version.ParseFailureKind.ARGUMENT_ERR:
                return ArgumentError("Version string portion was too short or too long.")
            if self._failure == Version.ParseFailureKind.ARGUMENT_OUT_OF_RANGE_ERR:
                return ArgumentOutOfRangeError("Version's parameters must be greater than or equal to zero.")
            if self._failure == Version.ParseFailureKind.FORMAT_ERR:
                try:
                    _ = int(self._exception_argument)
                except ValueError as e:
                    return ArgumentError(e)
                except Exception:
                    return FormatError("Input string was not in a correct format.")
            return ArgumentError("Version string portion was too short or too long.")

        @property
        def parsed_version(self) -> 'Version':
            return self._parsed_version

        @parsed_version.setter
        def parsed_version(self, value: 'Version') -> None:
            self._parsed_version = value
    # endregion Internal Classes
    _default_no_val: int = -999

    def __init__(self, *args):
        '''
        Class constructor
        @version:
            A string containing the major, minor, build, and revision numbers, where each number is delimited
            with a period character ('.').
        @arg1: Type:int|str If integer then the major version number.
            If str then will be parsed to construct major, minor, build and revision. Samse as `Version.parse()`
        @arg2: Type:int|str, the minor version number.
        @arg3: Type:int|str, the build number.
        @arg4: Type:int|str, the revision number.
        
        Remarks:
            The version parameter can contain only the components major, minor, build, and revision, in that
            order, and all separated by periods. There must be at least one component, and at most four. The
            first two components are assumed to be major and minor. The value of unspecified components is
            `0`.
            The format of the version number is as follows. Optional components are shown in square brackets
            ('[' and ']'):
            major.minor[.build[.revision]]
            All defined components must be integers greater than or equal to 0. For example, if the major number
            is 3, the minor number is 4, the build number is 2, and the revision number is 5, then version
            should be "3.4.2.5".
        
        Version(major, minor)
            Initializes a new instance of the MfVersion class using the specified major and minor values.
      
        Version(major, minor, build)
            Initializes a new instance of the MfVersion class using the specified major, minor, and build values.
        
        Version(major, minor, build, revision)
            Initializes a new instance of the MfVersion class with the specified major, minor, build, and revision numbers.
        '''
        if self.__class__.__name__ != 'Version':
            raise TypeError("version is a seal class")
        super_args = {}
        self._element_count: Union[int, None] = None
        self._major: Union[int, None] = None
        self._minor: Union[int, None] = None
        self._build: int = Version._default_no_val
        self._revision: int = Version._default_no_val
        self._arg_len = len(args)
        if self._arg_len > 4:
            raise ArgumentError(
                f"{self.__class__.__name__} has a max of four args")

        major: Union[str, int, None] = None
        minor: Union[int, str, float, None] = None
        build: Union[int, str, float, None] = None
        revision: Union[int, str, float, None] = None
        if self._arg_len == 0:
            self._major = 0
            self._minor = 0
            return None
        if self._arg_len >= 1:
            major = args[0]
        if self._arg_len >= 2:
            minor = args[1]
        if self._arg_len >= 3:
            build = args[2]
        if self._arg_len == 4:
            revision = args[3]

        if minor is None:
            if isinstance(major, int):
                self._major = major
                self._minor = 0
                self._set_super_args(super_args, 'major', self._major)
                self._set_super_args(super_args, 'minor', self._minor)
            elif isinstance(major, dict):
                self._init_by_dict(major, super_args)
            else:
                version2 = Version.parse(major)
                self._major = version2._major
                self._minor = version2._minor
                self._build = version2._build
                self._revision = version2._revision
                self._set_super_args(super_args, 'major', self._major)
                self._set_super_args(super_args, 'minor', self._minor)
                if self._build != Version._default_no_val:
                    self._set_super_args(
                        super_args, 'build', self._build)
                if self._revision != Version._default_no_val:
                    self._set_super_args(
                        super_args, 'revision', self._revision)
        elif build is None:
            self._major = Version._parse_int_arg(arg=major, arg_name='major')
            self._minor = Version._parse_int_arg(arg=minor, arg_name='minor')
            self._set_super_args(super_args, 'major', self._major)
            self._set_super_args(super_args, 'minor', self._minor)
        elif revision is None:
            self._major = Version._parse_int_arg(arg=major, arg_name='major')
            self._minor = Version._parse_int_arg(arg=minor, arg_name='minor')
            self._build = Version._parse_int_arg(arg=build, arg_name='build')
            self._set_super_args(super_args, 'major', self.major)
            self._set_super_args(super_args, 'minor', self._minor)
            self._set_super_args(super_args, 'build', self._build)
        else:
            self._major = Version._parse_int_arg(arg=major, arg_name='major')
            self._minor = Version._parse_int_arg(arg=minor, arg_name='minor')
            self._build = Version._parse_int_arg(arg=build, arg_name='build')
            self._revision = Version._parse_int_arg(
                arg=revision, arg_name='revision')
            self._set_super_args(super_args, 'major', self.major)
            self._set_super_args(super_args, 'minor', self._minor)
            self._set_super_args(super_args, 'build', self._build)
            self._set_super_args(super_args, 'revision', self._revision)
        self._validate()
        dict.__init__(self, **super_args)

    def _set_super_args(self, args: dict, key: str, value: int) -> None:
        if not key in args:
            args[key] = value

    def _init_by_dict(self, d: dict, super_args: dict):
        local_d = {
            'major': True,
            'minor': True,
            'build': False,
            'revision': False
        }
        for k, v in local_d.items():
            if k in d:
                val = d[k]
                i = Version._parse_int_arg(val, k)
                setattr(self, f"_{k}", i)
                super_args[k] = i
            else:
                if v:
                    raise ArgumentNullError(
                        f"{self.__class__.__name__} dictionary missing required key of '{k}'")

    @classmethod
    def _parse_int_arg(cls, arg, arg_name: str) -> int:
        if isinstance(arg, int):
            return arg
        if isinstance(arg, str):
            _arg = arg.strip()
            result = -1
            try:
                result = int(_arg)
                return result
            except:
                pass
            _arg = _arg.lower()
            if _arg.startswith('0x'):
                try:
                    result = int(_arg, 16)
                    return result
                except:
                    pass
        msg = (f"{cls.__name__}, arg '{arg_name}' cannot be converted to an interger."
               f" '{arg_name}' type '{type(arg).__name__}'")
        raise ArgumentError(msg)

    def _validate(self) -> None:
        msg = "Version's parameters must be greater than or equal to zero."
        if self._major < 0:
            raise ArgumentOutOfRangeError("major", msg)
        if self._minor < 0:
            raise ArgumentOutOfRangeError("minor", msg)
        if self._build != Version._default_no_val and self._build < 0:
            raise ArgumentOutOfRangeError("build", msg)
        if self._revision != Version._default_no_val and self._revision < 0:
            raise ArgumentOutOfRangeError("revision", msg)

    @staticmethod
    def _try_parse_component(component: str, component_name: str, result: 'Version.VersionResult') -> Tuple[bool, int]:
        pc = -1
        try:
            pc = Version._parse_int_arg(component, component_name)
        except Exception as e:
            result.set_failure(Version.ParseFailureKind.FORMAT_ERR, component)
            return False, -1
        if pc < 0:
            result.set_failure(
                Version.ParseFailureKind.ARGUMENT_OUT_OF_RANGE_ERR, component_name)
            return False, -1
        return True, pc

    @staticmethod
    def _try_parse_version(version: str, result: 'Version.VersionResult') -> bool:
        _ver = version.strip()
        if len(_ver) == 0:
            result.set_failure(Version.ParseFailureKind.ARGUMENT_NULL_ERR)
            return False
        ver_lst = _ver.split('.')
        split_count = len(ver_lst)
        if split_count < 2 or split_count > 4:
            result.set_failure(Version.ParseFailureKind.ARGUMENT_ERR)
            return False
        major = 0
        tp = Version._try_parse_component(ver_lst[0], "Version", result)
        if tp[0] == False:
            return False
        else:
            major = tp[1]
        minor = 0
        tp = Version._try_parse_component(ver_lst[1], "Version", result)
        if tp[0] == False:
            return False
        else:
            minor = tp[1]
        split_count -= 2
        if split_count > 0:
            build = 0
            tp = Version._try_parse_component(ver_lst[2], "build", result)
            if tp[0] == False:
                return False
            else:
                build = tp[1]
            split_count -= 1
            if split_count > 0:
                revision = 0
                tp = Version._try_parse_component(
                    ver_lst[3], "revision", result)
                if tp[0] == False:
                    return False
                else:
                    revision = tp[1]
                result.parsed_version = Version(major, minor, build, revision)
            else:
                result.parsed_version = Version(major, minor, build)
        else:
            result.parsed_version = Version(major, minor)
        return True

    @staticmethod
    def parse(input: str):
        '''
        Converts the string representation of a version number to an equivalent `Version` instance.
        @input: A string that contains a version number to convert.
        @return: A `Version` instance that is equivalent to the version number specified in the input parameter
        @error: Will raise errors if they occur. 
        @see also: `try_parse()`
        @example:
        ```
        ver = Version.parse("1.3")
        print(ver.major) # 1
        print(ver.minor) # 3
        
        ver = Version.parse("1.3.8.97")
        print(ver.major) # 1
        print(ver.minor) # 3
        print(ver.build) # 8
        print(ver.revision) # 97
        ```
        '''
        if not isinstance(input, str):
            raise ArgumentError(
                "Version.Parse() 'input' must be of type 'str'")
        version_result = Version.VersionResult()
        version_result.init('input', True)
        # no need to test the result of the following line. It will never raise an error when init is set with True: init('input' True)
        Version._try_parse_version(input, version_result)
        return version_result.parsed_version

    @staticmethod
    def try_parse(input: str) -> Tuple[bool, Union['Version', Exception]]:
        '''
        Converts the string representation of a version number to an equivalent `Version` instance.
        @input: A string that contains a version number to convert.
        @return: tuple with the first element as bool. first element will be `True` when parse is a success;
        Otherwise, first element will be `False`.
        When first element is `True` an instance of the `Version` will be returned as the second element.
        When first element is `False` second element will contain the error that occured that caused the failure.
        @example:
        ```
        v_result = Version.try_parse('2.1.12')
        if v_result[0] == True:
            v = v_result[1]
            print(v.major) # 2
            print(v.minor) # 1
            print(v.build) # 17
        else:
            print("An Error has occured", v_result[1])
        ```
        '''
        err = None
        if not isinstance(input, str):
            err = ArgumentError(
                "Version.Parse() 'input' must be of type 'str'")
            return False, err
        version_result = Version.VersionResult()
        version_result.init('input', False)
        if Version._try_parse_version(input, version_result) == False:
            err = version_result.get_version_parse_exception()
            return False, err
        return True, version_result.parsed_version
    # region Properties

    @property
    def build(self) -> int:
        '''
        Gets the value of the build component of the version number for the current Version instance.
        @return: int representing build
        '''
        if self._build == Version._default_no_val:
            return 0
        return self._build

    @property
    def major(self) -> int:
        '''
        Gets the value of the major component of the version number for the current Version instnace.
        @return: int representing major
        '''
        return self._major

    @property
    def major_revision(self) -> int:
        '''
        Gets the high 16 bits of the revision number.
        
        @remarks:
        Read-only property
        Suppose you release an interim version of your application to temporarily correct a problem until you
        can release a permanent solution. The temporary version does not warrant a new revision number,
        but it does need to be identified as a different version. In this case, encode the identification
        information in the high and low 16-bit portions of the 32-bit revision number. Use the `revision`
        property to obtain the entire revision number, use the `major_revision` property to obtain the high 16 bits,
        and use the `minor_revision` property to obtain the low 16 bits.
        '''
        hi_word = self.revision >> 16
        return hi_word

    @property
    def minor(self) -> int:
        '''
        Gets the value of the minor component of the version number for the current Version instnace.
        @return: int representing minor
        '''
        return self._minor

    @property
    def minor_revision(self) -> int:
        '''
        Gets the low 16 bits of the revision number.
        
        @remarks:
        Read-only property
        Suppose you release an interim version of your application to temporarily correct a problem until you
        can release a permanent solution. The temporary version does not warrant a new revision number,
        but it does need to be identified as a different version. In this case, encode the identification
        information in the high and low 16-bit portions of the 32-bit revision number. Use the `revision`
        property to obtain the entire revision number, use the `major_revision` property to obtain the high 16 bits,
        and use the `minor_revision` property to obtain the low 16 bits.
        '''
        lo_word = self.revision & int('0xFFFF', 16)
        return lo_word

    @property
    def revision(self) -> int:
        '''
        Gets the value of the revision component of the version number for the current Version instnace.
        @return: int representing minor
        '''
        if self._revision == Version._default_no_val:
            return 0
        return self._revision
    
    @property
    def elements(self) -> int:
        '''
        Gets the number of elements in the current instance.
        @return: int of 2, 3 or 4
        @example:
        ```
        v = Version(11, 22 ,33, 44)
        print(v.count) # 4
        v = Version(11, 22 ,33)
        print(v.count) # 3
        v = Version(11, 22)
        print(v.count) # 2
        v = Version(11)
        print(v.count) # 2
        print(v.to_str()) # 11.0
        ```
        '''
        if self._element_count is None:
            if self._build == Version._default_no_val:
                self._element_count = 2
            elif self._revision == Version._default_no_val:
                self._element_count = 3
            else:
                self._element_count = 4
        return self._element_count
            
    # endregion Properties

    # region Compare

    def _compare(self, other: 'Version'):
        if self.major != other.major:
            if self.major > other.major:
                return 1
            return -1
        elif self.minor != other.minor:
            if self.minor > other.minor:
                return 1
            return -1
        elif self.build != other.build:
            if self.build > other.build:
                return 1
            return -1
        elif self.revision == other.revision:
            return 0
        elif self.revision > other.revision:
            return 1
        return -1

    def __eq__(self, other: 'Version'):
        if not isinstance(other, Version):
            return NotImplemented
        return self._compare(other) == 0

    def __le__(self, other: 'Version'):
        if not isinstance(other, Version):
            return NotImplemented
        return self._compare(other) <= 0

    def __gt__(self, other: 'Version'):
        if not isinstance(other, Version):
            return NotImplemented
        return self._compare(other) > 0

    def __lt__(self, other: 'Version'):
        if not isinstance(other, Version):
            return NotImplemented
        return self._compare(other) < 0

    def __ge__(self, other: 'Version'):
        if not isinstance(other, Version):
            return NotImplemented
        return self._compare(other) >= 0

    def __hash__(self):
        _int = 0
        _int |= (self.major & 15) << 28
        _int |= (self.minor & 255) << 20
        _int |= (self.build & 255) << 12
        _int |= (self.revision & 4095)
        return _int
    # endregion Compare
    # region string methodos

    def _to_str(self, field_count: int):
        if field_count == 1:
            return f"{self.major}"
        elif field_count == 2:
            return f"{self.major}.{self.minor}"
        if field_count == 3:
            return f"{self.major}.{self.minor}.{self.build}"
        if field_count == 4:
            return f"{self.major}.{self.minor}.{self.build}.{self.revision}"

    def to_str(self, field_count: Optional[int] = None) -> str:
        '''
        Get the version as a string delimite by '.'
        @field_count: (optional) Type:int, number of fields to return.
        Must be a value from `1` to `elements` property value.
        Default: `elements` property value.
        @example:
        ```
        v = Version(11, 22, 33, 44)
        print(v.to_str() == '11.22.33.44') # True
        print(v.to_str(field_count=3) == '11.22.33') # True
        print(v.to_str(field_count=2) == '11.22') # True
        print(v.to_str(field_count=1) == '11') # True
        
        ```
        '''
        if field_count is not None:
            if not isinstance(field_count, int):
                raise ArgumentError(f"{self.__class__.__name__}.to_str() arg field_count must be of type 'int'")
            if field_count < 1 or field_count > self.elements:
                raise ArgumentOutOfRangeError(
                    f"{self.__class__.__name__}.to_str() arg field_count arg must be from 1 to current instance.elements that currently has a value of '{self.elements}'")
                        
            return self._to_str(field_count)
        return self._to_str(self.elements)

    def to_tuple(self, field_count: Optional[int] = None) -> Tuple[int]:
        '''
        Get the version as a tuple
        @field_count: (optional) Type:int, number of fields to return.
        Must be a value from `1` to `elements` property value.
        Default: `elements` property value.
        @example:
        ```
        v = Version(11, 22, 33, 44)
        print(v.to_tuple() == (11, 22, 33, 44)) # True
        print(v.to_tuple(field_count=3) == (11, 22, 33)) # True
        print(v.to_tuple(field_count=2) == (11, 22)) # True
        print(v.to_tuple(field_count=1) == (11,)) # True
        
        ```
        '''
        if field_count is not None:
            if not isinstance(field_count, int):
                raise ArgumentError(
                    f"{self.__class__.__name__}.to_tuple() arg field_count must be of type 'int'")
            if field_count < 1 or field_count > self.elements:
                raise ArgumentOutOfRangeError(
                    f"{self.__class__.__name__}.to_tuple() arg field_count arg must be from 1 to current instance.elements that currently has a value of '{self.elements}'")
        result = tuple([int(x) for x in self.to_str(field_count=field_count).split('.')])
        return result
    
    def __str__(self):
       return self.to_str()

    def __repr__(self):
        s = self.to_str()
        s_arg = s.replace('.', ', ')
        return f"<{self.__class__.__name__}({s_arg})>"
    # endregion string methods

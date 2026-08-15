# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fake_depth2_interfaces:srv/CalibrateDepth.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CalibrateDepth_Request(type):
    """Metaclass of message 'CalibrateDepth_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('fake_depth2_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'fake_depth2_interfaces.srv.CalibrateDepth_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__calibrate_depth__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__calibrate_depth__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__calibrate_depth__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__calibrate_depth__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__calibrate_depth__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CalibrateDepth_Request(metaclass=Metaclass_CalibrateDepth_Request):
    """Message class 'CalibrateDepth_Request'."""

    __slots__ = [
        '_reset_to_zero',
        '_requested_offset',
    ]

    _fields_and_field_types = {
        'reset_to_zero': 'boolean',
        'requested_offset': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.reset_to_zero = kwargs.get('reset_to_zero', bool())
        self.requested_offset = kwargs.get('requested_offset', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.reset_to_zero != other.reset_to_zero:
            return False
        if self.requested_offset != other.requested_offset:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def reset_to_zero(self):
        """Message field 'reset_to_zero'."""
        return self._reset_to_zero

    @reset_to_zero.setter
    def reset_to_zero(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'reset_to_zero' field must be of type 'bool'"
        self._reset_to_zero = value

    @builtins.property
    def requested_offset(self):
        """Message field 'requested_offset'."""
        return self._requested_offset

    @requested_offset.setter
    def requested_offset(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'requested_offset' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'requested_offset' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._requested_offset = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_CalibrateDepth_Response(type):
    """Metaclass of message 'CalibrateDepth_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('fake_depth2_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'fake_depth2_interfaces.srv.CalibrateDepth_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__calibrate_depth__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__calibrate_depth__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__calibrate_depth__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__calibrate_depth__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__calibrate_depth__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CalibrateDepth_Response(metaclass=Metaclass_CalibrateDepth_Response):
    """Message class 'CalibrateDepth_Response'."""

    __slots__ = [
        '_success',
        '_message',
        '_applied_offset',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'message': 'string',
        'applied_offset': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())
        self.message = kwargs.get('message', str())
        self.applied_offset = kwargs.get('applied_offset', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.success != other.success:
            return False
        if self.message != other.message:
            return False
        if self.applied_offset != other.applied_offset:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value

    @builtins.property
    def message(self):
        """Message field 'message'."""
        return self._message

    @message.setter
    def message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'message' field must be of type 'str'"
        self._message = value

    @builtins.property
    def applied_offset(self):
        """Message field 'applied_offset'."""
        return self._applied_offset

    @applied_offset.setter
    def applied_offset(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'applied_offset' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'applied_offset' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._applied_offset = value


class Metaclass_CalibrateDepth(type):
    """Metaclass of service 'CalibrateDepth'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('fake_depth2_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'fake_depth2_interfaces.srv.CalibrateDepth')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__calibrate_depth

            from fake_depth2_interfaces.srv import _calibrate_depth
            if _calibrate_depth.Metaclass_CalibrateDepth_Request._TYPE_SUPPORT is None:
                _calibrate_depth.Metaclass_CalibrateDepth_Request.__import_type_support__()
            if _calibrate_depth.Metaclass_CalibrateDepth_Response._TYPE_SUPPORT is None:
                _calibrate_depth.Metaclass_CalibrateDepth_Response.__import_type_support__()


class CalibrateDepth(metaclass=Metaclass_CalibrateDepth):
    from fake_depth2_interfaces.srv._calibrate_depth import CalibrateDepth_Request as Request
    from fake_depth2_interfaces.srv._calibrate_depth import CalibrateDepth_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')

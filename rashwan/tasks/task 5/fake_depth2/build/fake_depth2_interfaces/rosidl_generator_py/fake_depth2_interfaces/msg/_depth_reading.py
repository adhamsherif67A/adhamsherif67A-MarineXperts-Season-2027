# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fake_depth2_interfaces:msg/DepthReading.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_DepthReading(type):
    """Metaclass of message 'DepthReading'."""

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
                'fake_depth2_interfaces.msg.DepthReading')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__depth_reading
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__depth_reading
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__depth_reading
            cls._TYPE_SUPPORT = module.type_support_msg__msg__depth_reading
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__depth_reading

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DepthReading(metaclass=Metaclass_DepthReading):
    """Message class 'DepthReading'."""

    __slots__ = [
        '_header',
        '_depth',
        '_zero_offset',
        '_threshold_crossed',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'depth': 'float',
        'zero_offset': 'float',
        'threshold_crossed': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.depth = kwargs.get('depth', float())
        self.zero_offset = kwargs.get('zero_offset', float())
        self.threshold_crossed = kwargs.get('threshold_crossed', bool())

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
        if self.header != other.header:
            return False
        if self.depth != other.depth:
            return False
        if self.zero_offset != other.zero_offset:
            return False
        if self.threshold_crossed != other.threshold_crossed:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def depth(self):
        """Message field 'depth'."""
        return self._depth

    @depth.setter
    def depth(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'depth' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'depth' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._depth = value

    @builtins.property
    def zero_offset(self):
        """Message field 'zero_offset'."""
        return self._zero_offset

    @zero_offset.setter
    def zero_offset(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'zero_offset' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'zero_offset' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._zero_offset = value

    @builtins.property
    def threshold_crossed(self):
        """Message field 'threshold_crossed'."""
        return self._threshold_crossed

    @threshold_crossed.setter
    def threshold_crossed(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'threshold_crossed' field must be of type 'bool'"
        self._threshold_crossed = value

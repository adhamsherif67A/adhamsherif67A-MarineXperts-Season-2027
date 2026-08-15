# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fake_depth2_interfaces:action/DiveToDepth.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_DiveToDepth_Goal(type):
    """Metaclass of message 'DiveToDepth_Goal'."""

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
                'fake_depth2_interfaces.action.DiveToDepth_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dive_to_depth__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dive_to_depth__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dive_to_depth__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__dive_to_depth__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dive_to_depth__goal

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DiveToDepth_Goal(metaclass=Metaclass_DiveToDepth_Goal):
    """Message class 'DiveToDepth_Goal'."""

    __slots__ = [
        '_target_depth',
        '_dive_rate',
    ]

    _fields_and_field_types = {
        'target_depth': 'float',
        'dive_rate': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.target_depth = kwargs.get('target_depth', float())
        self.dive_rate = kwargs.get('dive_rate', float())

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
        if self.target_depth != other.target_depth:
            return False
        if self.dive_rate != other.dive_rate:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def target_depth(self):
        """Message field 'target_depth'."""
        return self._target_depth

    @target_depth.setter
    def target_depth(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'target_depth' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'target_depth' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._target_depth = value

    @builtins.property
    def dive_rate(self):
        """Message field 'dive_rate'."""
        return self._dive_rate

    @dive_rate.setter
    def dive_rate(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'dive_rate' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'dive_rate' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._dive_rate = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_DiveToDepth_Result(type):
    """Metaclass of message 'DiveToDepth_Result'."""

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
                'fake_depth2_interfaces.action.DiveToDepth_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dive_to_depth__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dive_to_depth__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dive_to_depth__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__dive_to_depth__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dive_to_depth__result

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DiveToDepth_Result(metaclass=Metaclass_DiveToDepth_Result):
    """Message class 'DiveToDepth_Result'."""

    __slots__ = [
        '_success',
        '_final_depth',
        '_message',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'final_depth': 'float',
        'message': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())
        self.final_depth = kwargs.get('final_depth', float())
        self.message = kwargs.get('message', str())

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
        if self.final_depth != other.final_depth:
            return False
        if self.message != other.message:
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
    def final_depth(self):
        """Message field 'final_depth'."""
        return self._final_depth

    @final_depth.setter
    def final_depth(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'final_depth' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'final_depth' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._final_depth = value

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


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_DiveToDepth_Feedback(type):
    """Metaclass of message 'DiveToDepth_Feedback'."""

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
                'fake_depth2_interfaces.action.DiveToDepth_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dive_to_depth__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dive_to_depth__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dive_to_depth__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__dive_to_depth__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dive_to_depth__feedback

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DiveToDepth_Feedback(metaclass=Metaclass_DiveToDepth_Feedback):
    """Message class 'DiveToDepth_Feedback'."""

    __slots__ = [
        '_current_depth',
        '_remaining_distance',
        '_percent_complete',
    ]

    _fields_and_field_types = {
        'current_depth': 'float',
        'remaining_distance': 'float',
        'percent_complete': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.current_depth = kwargs.get('current_depth', float())
        self.remaining_distance = kwargs.get('remaining_distance', float())
        self.percent_complete = kwargs.get('percent_complete', float())

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
        if self.current_depth != other.current_depth:
            return False
        if self.remaining_distance != other.remaining_distance:
            return False
        if self.percent_complete != other.percent_complete:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def current_depth(self):
        """Message field 'current_depth'."""
        return self._current_depth

    @current_depth.setter
    def current_depth(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'current_depth' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'current_depth' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._current_depth = value

    @builtins.property
    def remaining_distance(self):
        """Message field 'remaining_distance'."""
        return self._remaining_distance

    @remaining_distance.setter
    def remaining_distance(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'remaining_distance' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'remaining_distance' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._remaining_distance = value

    @builtins.property
    def percent_complete(self):
        """Message field 'percent_complete'."""
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'percent_complete' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'percent_complete' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._percent_complete = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DiveToDepth_SendGoal_Request(type):
    """Metaclass of message 'DiveToDepth_SendGoal_Request'."""

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
                'fake_depth2_interfaces.action.DiveToDepth_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dive_to_depth__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dive_to_depth__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dive_to_depth__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__dive_to_depth__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dive_to_depth__send_goal__request

            from fake_depth2_interfaces.action import DiveToDepth
            if DiveToDepth.Goal.__class__._TYPE_SUPPORT is None:
                DiveToDepth.Goal.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DiveToDepth_SendGoal_Request(metaclass=Metaclass_DiveToDepth_SendGoal_Request):
    """Message class 'DiveToDepth_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'fake_depth2_interfaces/DiveToDepth_Goal',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['fake_depth2_interfaces', 'action'], 'DiveToDepth_Goal'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_Goal
        self.goal = kwargs.get('goal', DiveToDepth_Goal())

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
        if self.goal_id != other.goal_id:
            return False
        if self.goal != other.goal:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def goal(self):
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value):
        if __debug__:
            from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_Goal
            assert \
                isinstance(value, DiveToDepth_Goal), \
                "The 'goal' field must be a sub message of type 'DiveToDepth_Goal'"
        self._goal = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DiveToDepth_SendGoal_Response(type):
    """Metaclass of message 'DiveToDepth_SendGoal_Response'."""

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
                'fake_depth2_interfaces.action.DiveToDepth_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dive_to_depth__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dive_to_depth__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dive_to_depth__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__dive_to_depth__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dive_to_depth__send_goal__response

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DiveToDepth_SendGoal_Response(metaclass=Metaclass_DiveToDepth_SendGoal_Response):
    """Message class 'DiveToDepth_SendGoal_Response'."""

    __slots__ = [
        '_accepted',
        '_stamp',
    ]

    _fields_and_field_types = {
        'accepted': 'boolean',
        'stamp': 'builtin_interfaces/Time',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.accepted = kwargs.get('accepted', bool())
        from builtin_interfaces.msg import Time
        self.stamp = kwargs.get('stamp', Time())

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
        if self.accepted != other.accepted:
            return False
        if self.stamp != other.stamp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def accepted(self):
        """Message field 'accepted'."""
        return self._accepted

    @accepted.setter
    def accepted(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'accepted' field must be of type 'bool'"
        self._accepted = value

    @builtins.property
    def stamp(self):
        """Message field 'stamp'."""
        return self._stamp

    @stamp.setter
    def stamp(self, value):
        if __debug__:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'stamp' field must be a sub message of type 'Time'"
        self._stamp = value


class Metaclass_DiveToDepth_SendGoal(type):
    """Metaclass of service 'DiveToDepth_SendGoal'."""

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
                'fake_depth2_interfaces.action.DiveToDepth_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__dive_to_depth__send_goal

            from fake_depth2_interfaces.action import _dive_to_depth
            if _dive_to_depth.Metaclass_DiveToDepth_SendGoal_Request._TYPE_SUPPORT is None:
                _dive_to_depth.Metaclass_DiveToDepth_SendGoal_Request.__import_type_support__()
            if _dive_to_depth.Metaclass_DiveToDepth_SendGoal_Response._TYPE_SUPPORT is None:
                _dive_to_depth.Metaclass_DiveToDepth_SendGoal_Response.__import_type_support__()


class DiveToDepth_SendGoal(metaclass=Metaclass_DiveToDepth_SendGoal):
    from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_SendGoal_Request as Request
    from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_SendGoal_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DiveToDepth_GetResult_Request(type):
    """Metaclass of message 'DiveToDepth_GetResult_Request'."""

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
                'fake_depth2_interfaces.action.DiveToDepth_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dive_to_depth__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dive_to_depth__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dive_to_depth__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__dive_to_depth__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dive_to_depth__get_result__request

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DiveToDepth_GetResult_Request(metaclass=Metaclass_DiveToDepth_GetResult_Request):
    """Message class 'DiveToDepth_GetResult_Request'."""

    __slots__ = [
        '_goal_id',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())

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
        if self.goal_id != other.goal_id:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DiveToDepth_GetResult_Response(type):
    """Metaclass of message 'DiveToDepth_GetResult_Response'."""

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
                'fake_depth2_interfaces.action.DiveToDepth_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dive_to_depth__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dive_to_depth__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dive_to_depth__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__dive_to_depth__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dive_to_depth__get_result__response

            from fake_depth2_interfaces.action import DiveToDepth
            if DiveToDepth.Result.__class__._TYPE_SUPPORT is None:
                DiveToDepth.Result.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DiveToDepth_GetResult_Response(metaclass=Metaclass_DiveToDepth_GetResult_Response):
    """Message class 'DiveToDepth_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
    ]

    _fields_and_field_types = {
        'status': 'int8',
        'result': 'fake_depth2_interfaces/DiveToDepth_Result',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['fake_depth2_interfaces', 'action'], 'DiveToDepth_Result'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.status = kwargs.get('status', int())
        from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_Result
        self.result = kwargs.get('result', DiveToDepth_Result())

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
        if self.status != other.status:
            return False
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'status' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'status' field must be an integer in [-128, 127]"
        self._status = value

    @builtins.property
    def result(self):
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value):
        if __debug__:
            from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_Result
            assert \
                isinstance(value, DiveToDepth_Result), \
                "The 'result' field must be a sub message of type 'DiveToDepth_Result'"
        self._result = value


class Metaclass_DiveToDepth_GetResult(type):
    """Metaclass of service 'DiveToDepth_GetResult'."""

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
                'fake_depth2_interfaces.action.DiveToDepth_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__dive_to_depth__get_result

            from fake_depth2_interfaces.action import _dive_to_depth
            if _dive_to_depth.Metaclass_DiveToDepth_GetResult_Request._TYPE_SUPPORT is None:
                _dive_to_depth.Metaclass_DiveToDepth_GetResult_Request.__import_type_support__()
            if _dive_to_depth.Metaclass_DiveToDepth_GetResult_Response._TYPE_SUPPORT is None:
                _dive_to_depth.Metaclass_DiveToDepth_GetResult_Response.__import_type_support__()


class DiveToDepth_GetResult(metaclass=Metaclass_DiveToDepth_GetResult):
    from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_GetResult_Request as Request
    from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_GetResult_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DiveToDepth_FeedbackMessage(type):
    """Metaclass of message 'DiveToDepth_FeedbackMessage'."""

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
                'fake_depth2_interfaces.action.DiveToDepth_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dive_to_depth__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dive_to_depth__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dive_to_depth__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__dive_to_depth__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dive_to_depth__feedback_message

            from fake_depth2_interfaces.action import DiveToDepth
            if DiveToDepth.Feedback.__class__._TYPE_SUPPORT is None:
                DiveToDepth.Feedback.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DiveToDepth_FeedbackMessage(metaclass=Metaclass_DiveToDepth_FeedbackMessage):
    """Message class 'DiveToDepth_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'fake_depth2_interfaces/DiveToDepth_Feedback',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['fake_depth2_interfaces', 'action'], 'DiveToDepth_Feedback'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_Feedback
        self.feedback = kwargs.get('feedback', DiveToDepth_Feedback())

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
        if self.goal_id != other.goal_id:
            return False
        if self.feedback != other.feedback:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def feedback(self):
        """Message field 'feedback'."""
        return self._feedback

    @feedback.setter
    def feedback(self, value):
        if __debug__:
            from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_Feedback
            assert \
                isinstance(value, DiveToDepth_Feedback), \
                "The 'feedback' field must be a sub message of type 'DiveToDepth_Feedback'"
        self._feedback = value


class Metaclass_DiveToDepth(type):
    """Metaclass of action 'DiveToDepth'."""

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
                'fake_depth2_interfaces.action.DiveToDepth')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__dive_to_depth

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from fake_depth2_interfaces.action import _dive_to_depth
            if _dive_to_depth.Metaclass_DiveToDepth_SendGoal._TYPE_SUPPORT is None:
                _dive_to_depth.Metaclass_DiveToDepth_SendGoal.__import_type_support__()
            if _dive_to_depth.Metaclass_DiveToDepth_GetResult._TYPE_SUPPORT is None:
                _dive_to_depth.Metaclass_DiveToDepth_GetResult.__import_type_support__()
            if _dive_to_depth.Metaclass_DiveToDepth_FeedbackMessage._TYPE_SUPPORT is None:
                _dive_to_depth.Metaclass_DiveToDepth_FeedbackMessage.__import_type_support__()


class DiveToDepth(metaclass=Metaclass_DiveToDepth):

    # The goal message defined in the action definition.
    from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_Goal as Goal
    # The result message defined in the action definition.
    from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_Result as Result
    # The feedback message defined in the action definition.
    from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_Feedback as Feedback

    class Impl:

        # The send_goal service using a wrapped version of the goal message as a request.
        from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_SendGoal as SendGoalService
        # The get_result service using a wrapped version of the result message as a response.
        from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_GetResult as GetResultService
        # The feedback message with generic fields which wraps the feedback message.
        from fake_depth2_interfaces.action._dive_to_depth import DiveToDepth_FeedbackMessage as FeedbackMessage

        # The generic service to cancel a goal.
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
        # The generic message for get the status of a goal.
        from action_msgs.msg._goal_status_array import GoalStatusArray as GoalStatusMessage

    def __init__(self):
        raise NotImplementedError('Action classes can not be instantiated')

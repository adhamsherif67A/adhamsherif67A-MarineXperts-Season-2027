// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from fake_depth2_interfaces:srv/CalibrateDepth.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "fake_depth2_interfaces/srv/detail/calibrate_depth__struct.h"
#include "fake_depth2_interfaces/srv/detail/calibrate_depth__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool fake_depth2_interfaces__srv__calibrate_depth__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[67];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("fake_depth2_interfaces.srv._calibrate_depth.CalibrateDepth_Request", full_classname_dest, 66) == 0);
  }
  fake_depth2_interfaces__srv__CalibrateDepth_Request * ros_message = _ros_message;
  {  // reset_to_zero
    PyObject * field = PyObject_GetAttrString(_pymsg, "reset_to_zero");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->reset_to_zero = (Py_True == field);
    Py_DECREF(field);
  }
  {  // requested_offset
    PyObject * field = PyObject_GetAttrString(_pymsg, "requested_offset");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->requested_offset = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * fake_depth2_interfaces__srv__calibrate_depth__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of CalibrateDepth_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("fake_depth2_interfaces.srv._calibrate_depth");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "CalibrateDepth_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  fake_depth2_interfaces__srv__CalibrateDepth_Request * ros_message = (fake_depth2_interfaces__srv__CalibrateDepth_Request *)raw_ros_message;
  {  // reset_to_zero
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->reset_to_zero ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "reset_to_zero", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // requested_offset
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->requested_offset);
    {
      int rc = PyObject_SetAttrString(_pymessage, "requested_offset", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "fake_depth2_interfaces/srv/detail/calibrate_depth__struct.h"
// already included above
// #include "fake_depth2_interfaces/srv/detail/calibrate_depth__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool fake_depth2_interfaces__srv__calibrate_depth__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[68];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("fake_depth2_interfaces.srv._calibrate_depth.CalibrateDepth_Response", full_classname_dest, 67) == 0);
  }
  fake_depth2_interfaces__srv__CalibrateDepth_Response * ros_message = _ros_message;
  {  // success
    PyObject * field = PyObject_GetAttrString(_pymsg, "success");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->success = (Py_True == field);
    Py_DECREF(field);
  }
  {  // message
    PyObject * field = PyObject_GetAttrString(_pymsg, "message");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->message, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // applied_offset
    PyObject * field = PyObject_GetAttrString(_pymsg, "applied_offset");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->applied_offset = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * fake_depth2_interfaces__srv__calibrate_depth__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of CalibrateDepth_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("fake_depth2_interfaces.srv._calibrate_depth");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "CalibrateDepth_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  fake_depth2_interfaces__srv__CalibrateDepth_Response * ros_message = (fake_depth2_interfaces__srv__CalibrateDepth_Response *)raw_ros_message;
  {  // success
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->success ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "success", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // message
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->message.data,
      strlen(ros_message->message.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "message", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // applied_offset
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->applied_offset);
    {
      int rc = PyObject_SetAttrString(_pymessage, "applied_offset", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

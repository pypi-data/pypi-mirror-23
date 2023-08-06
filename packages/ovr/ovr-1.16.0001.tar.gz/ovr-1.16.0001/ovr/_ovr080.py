"""
Python module "ovr"
Python bindings for Oculus Rift SDK version 0.8.0

Works on Windows only at the moment (just like Oculus Rift SDK...)
"""

import ctypes
from ctypes import *
import sys
import textwrap
import math
import platform


OVR_PTR_SIZE = sizeof(c_voidp) # distinguish 32 vs 64 bit python

# Load Oculus runtime library (only tested on Windows)
# 1) Figure out name of library to load
_libname = "OVRRT32_0_8" # 32-bit python
if OVR_PTR_SIZE == 8:
    _libname = "OVRRT64_0_8" # 64-bit python
if platform.system().startswith("Win"):
    _libname = "Lib"+_libname # i.e. "LibOVRRT32_0_8"
# Load library
try:
    libovr = CDLL(_libname)
except:
    print("Is Oculus Runtime 0.8 installed on this machine?")
    raise


ENUM_TYPE = c_int32 # Hopefully a close enough guess...


class HmdStruct(Structure):
    "Used as an opaque pointer to an OVR session."
    pass


# Signature of the logging callback function pointer type.
#
# \param[in] userData is an arbitrary value specified by the user of ovrInitParams.
# \param[in] level is one of the ovrLogLevel constants.
# \param[in] message is a UTF8-encoded null-terminated string.
# \see ovrInitParams ovrLogLevel, ovr_Initialize
#
# typedef void (OVR_CDECL* ovrLogCallback)(POINTER(c_uint) userData, int level, const char* message);
LogCallback = CFUNCTYPE(None, POINTER(c_uint), c_int, c_char_p)


def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p


def byref(obj):
    "Referencing None should result in None, at least for initialize method"
    b = None if obj is None else ctypes.byref(obj)
    return b

ovrFalse = c_char(chr(0)) # note potential conflict with Python built in symbols
ovrTrue = c_char(chr(1))

def toOvrBool(arg):
    # One tricky case:
    if arg == chr(0):
        return ovrFalse
    # Remainder are easy cases:
    if bool(arg):
        return ovrTrue
    else:
        return ovrFalse

### BEGIN Declarations from C header file OVR_Version.h ###


# Translated from header file OVR_Version.h line 21
PRODUCT_VERSION = 0 


# Translated from header file OVR_Version.h line 22
MAJOR_VERSION = 8 


# Translated from header file OVR_Version.h line 23
MINOR_VERSION = 0 


# Translated from header file OVR_Version.h line 24
PATCH_VERSION = 0 


# Translated from header file OVR_Version.h line 25
BUILD_NUMBER = 0 # This is the major version of the service that the DLL is compatible with.


# Translated from header file OVR_Version.h line 32
DLL_COMPATIBLE_MAJOR_VERSION = 8 


# Translated from header file OVR_Version.h line 33
FEATURE_VERSION = 0 # "Product.Major.Minor.Patch"


# Translated from header file OVR_Version.h line 50
DISPLAY_DRIVER_PRODUCT_VERSION = "1.2.8.0" # This is the product version for the Oculus Position Tracker Driver. A


# Translated from header file OVR_Version.h line 54
POSITIONAL_TRACKER_DRIVER_PRODUCT_VERSION = "1.0.14.0" # \brief file description for version info


### END Declarations from C header file OVR_Version.h ###


### BEGIN Declarations from C header file OVR_CAPI_Keys.h ###


# Translated from header file OVR_CAPI_Keys.h line 11
KEY_USER = "User" # string


# Translated from header file OVR_CAPI_Keys.h line 13
KEY_NAME = "Name" # string


# Translated from header file OVR_CAPI_Keys.h line 14
KEY_GENDER = "Gender" # string "Male", "Female", or "Unknown"


# Translated from header file OVR_CAPI_Keys.h line 15
KEY_PLAYER_HEIGHT = "PlayerHeight" # float meters


# Translated from header file OVR_CAPI_Keys.h line 16
KEY_EYE_HEIGHT = "EyeHeight" # float meters


# Translated from header file OVR_CAPI_Keys.h line 17
KEY_IPD = "IPD" # float meters


# Translated from header file OVR_CAPI_Keys.h line 18
KEY_NECK_TO_EYE_DISTANCE = "NeckEyeDistance" # float[2] meters


# Translated from header file OVR_CAPI_Keys.h line 19
KEY_EYE_RELIEF_DIAL = "EyeReliefDial" # int in range of 0-10


# Translated from header file OVR_CAPI_Keys.h line 20
KEY_EYE_TO_NOSE_DISTANCE = "EyeToNoseDist" # float[2] meters


# Translated from header file OVR_CAPI_Keys.h line 21
KEY_MAX_EYE_TO_PLATE_DISTANCE = "MaxEyeToPlateDist" # float[2] meters


# Translated from header file OVR_CAPI_Keys.h line 22
KEY_EYE_CUP = "EyeCup" # char[16] "A", "B", or "C"


# Translated from header file OVR_CAPI_Keys.h line 23
KEY_CUSTOM_EYE_RENDER = "CustomEyeRender" # bool


# Translated from header file OVR_CAPI_Keys.h line 25
KEY_CAMERA_POSITION_1 = "CenteredFromWorld" # double[7] ovrPosef quat rotation x, y, z, w, translation x, y, z


# Translated from header file OVR_CAPI_Keys.h line 27
KEY_CAMERA_POSITION_2 = "CenteredFromWorld2" # double[7] ovrPosef quat rotation x, y, z, w, translation x, y, z


# Translated from header file OVR_CAPI_Keys.h line 28
KEY_CAMERA_POSITION = KEY_CAMERA_POSITION_2 # Default measurements empirically determined at Oculus to make us happy


# Translated from header file OVR_CAPI_Keys.h line 36
DEFAULT_GENDER = "Unknown" 


# Translated from header file OVR_CAPI_Keys.h line 37
DEFAULT_PLAYER_HEIGHT = 1.778 


# Translated from header file OVR_CAPI_Keys.h line 38
DEFAULT_EYE_HEIGHT = 1.675 


# Translated from header file OVR_CAPI_Keys.h line 39
DEFAULT_IPD = 0.064 


# Translated from header file OVR_CAPI_Keys.h line 40
DEFAULT_NECK_TO_EYE_HORIZONTAL = 0.0805 


# Translated from header file OVR_CAPI_Keys.h line 41
DEFAULT_NECK_TO_EYE_VERTICAL = 0.075 


# Translated from header file OVR_CAPI_Keys.h line 42
DEFAULT_EYE_RELIEF_DIAL = 3 


# Translated from header file OVR_CAPI_Keys.h line 43
DEFAULT_CAMERA_POSITION = [0,0,0,1,0,0,0] 


# Translated from header file OVR_CAPI_Keys.h line 44
PERF_HUD_MODE = "PerfHudMode" # allowed values are defined in enum ovrPerfHudMode


# Translated from header file OVR_CAPI_Keys.h line 46
LAYER_HUD_MODE = "LayerHudMode" # allowed values are defined in enum ovrLayerHudMode


# Translated from header file OVR_CAPI_Keys.h line 48
LAYER_HUD_CURRENT_LAYER = "LayerHudCurrentLayer" # The layer to show 


# Translated from header file OVR_CAPI_Keys.h line 49
LAYER_HUD_SHOW_ALL_LAYERS = "LayerHudShowAll" # Hide other layers when the hud is enabled


# Translated from header file OVR_CAPI_Keys.h line 50
DEBUG_HUD_STEREO_MODE = "DebugHudStereoMode" # allowed values are defined in enum ovrDebugHudStereoMode


# Translated from header file OVR_CAPI_Keys.h line 52
DEBUG_HUD_STEREO_GUIDE_INFO_ENABLE = "DebugHudStereoGuideInfoEnable" # bool


# Translated from header file OVR_CAPI_Keys.h line 53
DEBUG_HUD_STEREO_GUIDE_SIZE = "DebugHudStereoGuideSize2f" # float[2]


# Translated from header file OVR_CAPI_Keys.h line 54
DEBUG_HUD_STEREO_GUIDE_POSITION = "DebugHudStereoGuidePosition3f" # float[3]


# Translated from header file OVR_CAPI_Keys.h line 55
DEBUG_HUD_STEREO_GUIDE_YAWPITCHROLL = "DebugHudStereoGuideYawPitchRoll3f" # float[3]


# Translated from header file OVR_CAPI_Keys.h line 56
DEBUG_HUD_STEREO_GUIDE_COLOR = "DebugHudStereoGuideColor4f" # float[4]


### END Declarations from C header file OVR_CAPI_Keys.h ###


### BEGIN Declarations from C header file OVR_ErrorCode.h ###


# Translated from header file OVR_ErrorCode.h line 21
# API call results are represented at the highest level by a single ovrResult.
Result = c_int32 


# Translated from header file OVR_ErrorCode.h line 33
def SUCCESS(result):
    return result >= 0


# Translated from header file OVR_ErrorCode.h line 44
def UNQUALIFIED_SUCCESS(result):
    return result == ovrSuccess


# Translated from header file OVR_ErrorCode.h line 51
def FAILURE(result):
    return not SUCCESS(result)


# Translated from header file OVR_ErrorCode.h line 57
SuccessType = ENUM_TYPE
# This is a general success result. Use OVR_SUCCESS to test for success.
Success = 0
# Returned from a call to SubmitFrame. The call succeeded, but what the app
# rendered will not be visible on the HMD. Ideally the app should continue
# calling SubmitFrame, but not do any rendering. When the result becomes
# ovrSuccess, rendering should continue as usual.
Success_NotVisible                 = 1000
Success_HMDFirmwareMismatch        = 4100   #< The HMD Firmware is out of date but is acceptable.
Success_TrackerFirmwareMismatch    = 4101   #< The Tracker Firmware is out of date but is acceptable.
Success_ControllerFirmwareMismatch = 4104   #< The controller firmware is out of date but is acceptable.


# Translated from header file OVR_ErrorCode.h line 75
ErrorType = ENUM_TYPE
# General errors #
Error_MemoryAllocationFailure    = -1000   #< Failure to allocate memory.
Error_SocketCreationFailure      = -1001   #< Failure to create a socket.
Error_InvalidSession             = -1002   #< Invalid ovrSession parameter provided.
Error_Timeout                    = -1003   #< The operation timed out.
Error_NotInitialized             = -1004   #< The system or component has not been initialized.
Error_InvalidParameter           = -1005   #< Invalid parameter provided. See error info or log for details.
Error_ServiceError               = -1006   #< Generic service error. See error info or log for details.
Error_NoHmd                      = -1007   #< The given HMD doesn't exist.
# Audio error range, reserved for Audio errors. #
Error_AudioReservedBegin         = -2000   #< First Audio error.
Error_AudioDeviceNotFound        = -2001   #< Failure to find the specified audio device.
Error_AudioComError              = -2002   #< Generic COM error.
Error_AudioReservedEnd           = -2999   #< Last Audio error.
# Initialization errors. #
Error_Initialize                 = -3000   #< Generic initialization error.
Error_LibLoad                    = -3001   #< Couldn't load LibOVRRT.
Error_LibVersion                 = -3002   #< LibOVRRT version incompatibility.
Error_ServiceConnection          = -3003   #< Couldn't connect to the OVR Service.
Error_ServiceVersion             = -3004   #< OVR Service version incompatibility.
Error_IncompatibleOS             = -3005   #< The operating system version is incompatible.
Error_DisplayInit                = -3006   #< Unable to initialize the HMD display.
Error_ServerStart                = -3007   #< Unable to start the server. Is it already running?
Error_Reinitialization           = -3008   #< Attempting to re-initialize with a different version.
Error_MismatchedAdapters         = -3009   #< Chosen rendering adapters between client and service do not match
Error_LeakingResources           = -3010   #< Calling application has leaked resources
Error_ClientVersion              = -3011   #< Client version too old to connect to service
Error_OutOfDateOS                = -3012   #< The operating system is out of date.
Error_OutOfDateGfxDriver         = -3013   #< The graphics driver is out of date.
Error_IncompatibleGPU            = -3014   #< The graphics hardware is not supported
Error_NoValidVRDisplaySystem     = -3015   #< No valid VR display system found.
# Hardware errors #
Error_InvalidBundleAdjustment    = -4000   #< Headset has no bundle adjustment data.
Error_USBBandwidth               = -4001   #< The USB hub cannot handle the camera frame bandwidth.
Error_USBEnumeratedSpeed         = -4002   #< The USB camera is not enumerating at the correct device speed.
Error_ImageSensorCommError       = -4003   #< Unable to communicate with the image sensor.
Error_GeneralTrackerFailure      = -4004   #< We use this to report various tracker issues that don't fit in an easily classifiable bucket.
Error_ExcessiveFrameTruncation   = -4005   #< A more than acceptable number of frames are coming back truncated.
Error_ExcessiveFrameSkipping     = -4006   #< A more than acceptable number of frames have been skipped.
Error_SyncDisconnected           = -4007   #< The tracker is not receiving the sync signal (cable disconnected?)
Error_TrackerMemoryReadFailure   = -4008   #< Failed to read memory from the tracker
Error_TrackerMemoryWriteFailure  = -4009   #< Failed to write memory from the tracker
Error_TrackerFrameTimeout        = -4010   #< Timed out waiting for a camera frame
Error_TrackerTruncatedFrame      = -4011   #< Truncated frame returned from tracker
Error_HMDFirmwareMismatch        = -4100   #< The HMD Firmware is out of date and is unacceptable.
Error_TrackerFirmwareMismatch    = -4101   #< The Tracker Firmware is out of date and is unacceptable.
Error_BootloaderDeviceDetected   = -4102   #< A bootloader HMD is detected by the service
Error_TrackerCalibrationError    = -4103   #< The tracker calibration is missing or incorrect
Error_ControllerFirmwareMismatch = -4104   #< The controller firmware is out of date and is unacceptable
# Synchronization errors #
Error_Incomplete                 = -5000   #<Requested async work not yet complete.
Error_Abandoned                  = -5001   #<Requested async work was abandoned and result is incomplete.
# Rendering errors #
Error_DisplayLost                = -6000   #<In the event of a system-wide graphics reset or cable unplug this is returned to the app
# Fatal errors #
Error_RuntimeException           = -7000   #< A runtime exception occurred. The application is required to shutdown LibOVR and re-initialize it before this error state will be cleared.


### END Declarations from C header file OVR_ErrorCode.h ###


### BEGIN Declarations from C header file OVR_CAPI_0_8_0.h ###


# Translated from header file OVR_CAPI_0_8_0.h line 264
Bool = c_char    #< Boolean type


# Translated from header file OVR_CAPI_0_8_0.h line 272
class Vector2i(Structure):
    "A 2D vector with integer components."
    _pack_ = 4
    _fields_ = [
        ("x", c_int), 
        ("y", c_int), 
    ]

    def __repr__(self):
        return "ovr.Vector2i(%s, %s)" % (self.x, self.y)

    def __len__(self):
        "number of items in this container"
        return len(self._fields_)

    def __getitem__(self, key):
        "access contained elements"
        if isinstance(key, slice):
            return [self[ii] for ii in range(*key.indices(len(self)))]
        else:
            return getattr(self, self._fields_[key][0])


# Translated from header file OVR_CAPI_0_8_0.h line 278
class Sizei(Structure):
    "A 2D size with integer components."
    _pack_ = 4
    _fields_ = [
        ("w", c_int), 
        ("h", c_int), 
    ]

    def __repr__(self):
        return "ovr.Sizei(%s, %s)" % (self.w, self.h)

    def __len__(self):
        "number of items in this container"
        return len(self._fields_)

    def __getitem__(self, key):
        "access contained elements"
        if isinstance(key, slice):
            return [self[ii] for ii in range(*key.indices(len(self)))]
        else:
            return getattr(self, self._fields_[key][0])


# Translated from header file OVR_CAPI_0_8_0.h line 284
class Recti(Structure):
    """
    A 2D rectangle with a position and size.
    All components are integers.
    """
    _pack_ = 4
    _fields_ = [
        ("Pos", Vector2i), 
        ("Size", Sizei), 
    ]

    def __repr__(self):
        return "ovr.Recti(%s, %s)" % (self.Pos, self.Size)


# Translated from header file OVR_CAPI_0_8_0.h line 292
class Quatf(Structure):
    "A quaternion rotation."
    _pack_ = 4
    _fields_ = [
        ("x", c_float), 
        ("y", c_float), 
        ("z", c_float), 
        ("w", c_float), 
    ]

    def __repr__(self):
        return "ovr.Quatf(%s, %s, %s, %s)" % (self.x, self.y, self.z, self.w)

    def __len__(self):
        "number of items in this container"
        return len(self._fields_)

    def __getitem__(self, key):
        "access contained elements"
        if isinstance(key, slice):
            return [self[ii] for ii in range(*key.indices(len(self)))]
        else:
            return getattr(self, self._fields_[key][0])

    def getEulerAngles(self, axis1=0, axis2=1, axis3=2, rotate_direction=1, handedness=1):
        assert(axis1 != axis2)
        assert(axis1 != axis3)
        assert(axis2 != axis3)
        Q = [ self.x, self.y, self.z ]  # Quaternion components x,y,z
        ww  = self.w*self.w;
        Q11 = Q[axis1]*Q[axis1]
        Q22 = Q[axis2]*Q[axis2]
        Q33 = Q[axis3]*Q[axis3]
        psign = -1.0
        # Determine whether even permutation
        if ((axis1 + 1) % 3 == axis2) and ((axis2 + 1) % 3 == axis3):
            psign = 1.0
        s2 = psign * 2.0 * (psign*self.w*Q[axis2] + Q[axis1]*Q[axis3])
        SingularityRadius = 1e-10
        D = rotate_direction # CCW rotation
        S = handedness # Right handed coordinate system
        if s2 < -1.0 + SingularityRadius:
            # South pole singularity
            a = 0.0
            b = -S*D*math.pi/2
            c = S*D*math.atan2(2.0*(psign*Q[axis1]*Q[axis2] + self.w*Q[axis3]),
                           ww + Q22 - Q11 - Q33 )
        elif s2 > 1.0 - SingularityRadius:
            # North pole singularity
            a = 0.0
            b = S*D*math.pi/2
            c = S*D*math.atan2(2.0*(psign*Q[axis1]*Q[axis2] + self.w*Q[axis3]),
                           ww + Q22 - Q11 - Q33)
        else:
            a = -S*D*math.atan2(-2.0*(self.w*Q[axis1] - psign*Q[axis2]*Q[axis3]),
                            ww + Q33 - Q11 - Q22)
            b = S*D*math.asin(s2)
            c = S*D*math.atan2(2.0*(self.w*Q[axis3] - psign*Q[axis1]*Q[axis2]),
                           ww + Q11 - Q22 - Q33)     
        return a, b, c


# Translated from header file OVR_CAPI_0_8_0.h line 298
class Vector2f(Structure):
    "A 2D vector with float components."
    _pack_ = 4
    _fields_ = [
        ("x", c_float), 
        ("y", c_float), 
    ]

    def __repr__(self):
        return "ovr.Vector2f(%s, %s)" % (self.x, self.y)

    def __len__(self):
        "number of items in this container"
        return len(self._fields_)

    def __getitem__(self, key):
        "access contained elements"
        if isinstance(key, slice):
            return [self[ii] for ii in range(*key.indices(len(self)))]
        else:
            return getattr(self, self._fields_[key][0])


# Translated from header file OVR_CAPI_0_8_0.h line 304
class Vector3f(Structure):
    "A 3D vector with float components."
    _pack_ = 4
    _fields_ = [
        ("x", c_float), 
        ("y", c_float), 
        ("z", c_float), 
    ]

    def __repr__(self):
        return "ovr.Vector3f(%s, %s, %s)" % (self.x, self.y, self.z)

    def __len__(self):
        "number of items in this container"
        return len(self._fields_)

    def __getitem__(self, key):
        "access contained elements"
        if isinstance(key, slice):
            return [self[ii] for ii in range(*key.indices(len(self)))]
        else:
            return getattr(self, self._fields_[key][0])


# Translated from header file OVR_CAPI_0_8_0.h line 310
class Matrix4f(Structure):
    "A 4x4 matrix with float elements."
    _pack_ = 4
    _fields_ = [
        ("M", (c_float * 4) * 4), 
    ]

    def __repr__(self):
        return "ovr.Matrix4f(%s)" % (self.M)

    def __len__(self):
        "number of items in this container"
        return 16

    def __getitem__(self, key):
        "access contained elements as a single flat list"
        i = int(key/4)
        j = key % 4
        return self.M[j][i]


# Translated from header file OVR_CAPI_0_8_0.h line 317
class Posef(Structure):
    "Position and orientation together."
    _pack_ = 4
    _fields_ = [
        ("Orientation", Quatf), 
        ("Position", Vector3f), 
    ]

    def __repr__(self):
        return "ovr.Posef(%s, %s)" % (self.Orientation, self.Position)


# Translated from header file OVR_CAPI_0_8_0.h line 324
class PoseStatef(Structure):
    """
    A full pose (rigid body) configuration with first and second derivatives.
    
    Body refers to any object for which ovrPoseStatef is providing data.
    It can be the HMD, Touch controller, camera or something else. The context 
    depends on the usage of the struct.
    """
    _pack_ = 8
    _fields_ = [
        ("ThePose", Posef),                #< Position and orientation.
        ("AngularVelocity", Vector3f),        #< Angular velocity in radians per second.
        ("LinearVelocity", Vector3f),         #< Velocity in meters per second.
        ("AngularAcceleration", Vector3f),    #< Angular acceleration in radians per second per second.
        ("LinearAcceleration", Vector3f),     #< Acceleration in meters per second per second.
        ("pad0", c_char * 4),       #< \internal struct pad.
        ("TimeInSeconds", c_double),          #< Absolute time of this state sample.
    ]

    def __repr__(self):
        return "ovr.PoseStatef(%s, %s, %s, %s, %s, %s)" % (self.ThePose, self.AngularVelocity, self.LinearVelocity, self.AngularAcceleration, self.LinearAcceleration, self.TimeInSeconds)


# Translated from header file OVR_CAPI_0_8_0.h line 340
class FovPort(Structure):
    """
    Describes the up, down, left, and right angles of the field of view.
    
    Field Of View (FOV) tangent of the angle units.
    \note For a standard 90 degree vertical FOV, we would
    have: { UpTan = tan(90 degrees / 2), DownTan = tan(90 degrees / 2) }.
    """
    _pack_ = 4
    _fields_ = [
        ("UpTan", c_float),     #< The tangent of the angle between the viewing vector and the top edge of the field of view.
        ("DownTan", c_float),   #< The tangent of the angle between the viewing vector and the bottom edge of the field of view.
        ("LeftTan", c_float),   #< The tangent of the angle between the viewing vector and the left edge of the field of view.
        ("RightTan", c_float),  #< The tangent of the angle between the viewing vector and the right edge of the field of view.
    ]

    def __repr__(self):
        return "ovr.FovPort(%s, %s, %s, %s)" % (self.UpTan, self.DownTan, self.LeftTan, self.RightTan)


# Translated from header file OVR_CAPI_0_8_0.h line 357
# Enumerates all HMD types that we support.
#
# The currently released developer kits are ovrHmd_DK1 and ovrHmd_DK2. The other enumerations are for internal use only.
HmdType = ENUM_TYPE
Hmd_None      = 0
Hmd_DK1       = 3
Hmd_DKHD      = 4
Hmd_DK2       = 6
Hmd_CB        = 8
Hmd_Other     = 9
Hmd_E3_2015   = 10
Hmd_ES06      = 11
Hmd_ES09      = 12


# Translated from header file OVR_CAPI_0_8_0.h line 375
# HMD capability bits reported by device.
#
# Set <B>(read/write)</B> flags through ovr_SetEnabledCaps()
HmdCaps = ENUM_TYPE
# Read-only flags.
HmdCap_DebugDevice             = 0x0010   #< <B>(read only)</B> Specifies that the HMD is a virtual debug device.
# Indicates to the developer what caps they can and cannot modify. These are processed by the client.
HmdCap_Writable_Mask       = 0x0000
HmdCap_Service_Mask        = 0x0000


# Translated from header file OVR_CAPI_0_8_0.h line 393
# Tracking capability bits reported by the device.
# Used with ovr_ConfigureTracking.
TrackingCaps = ENUM_TYPE
TrackingCap_Orientation      = 0x0010    #< Supports orientation tracking (IMU).
TrackingCap_MagYawCorrection = 0x0020    #< Supports yaw drift correction via a magnetometer or other means.
TrackingCap_Position         = 0x0040    #< Supports positional tracking.


# Translated from header file OVR_CAPI_0_8_0.h line 404
# Specifies which eye is being used for rendering.
# This type explicitly does not include a third "NoStereo" monoscopic option, as such is
# not required for an HMD-centered API.
EyeType = ENUM_TYPE
Eye_Left     = 0         #< The left eye, from the viewer's perspective.
Eye_Right    = 1         #< The right eye, from the viewer's perspective.
Eye_Count    = 2         #< \internal Count of enumerated elements.


# Translated from header file OVR_CAPI_0_8_0.h line 416
class GraphicsLuid(Structure):
    ""
    _pack_ = OVR_PTR_SIZE
    _fields_ = [
        # Public definition reserves space for graphics API-specific implementation
        ("Reserved", c_char * 8), 
    ]

    def __repr__(self):
        return "ovr.GraphicsLuid(%s)" % (self.Reserved)


# Translated from header file OVR_CAPI_0_8_0.h line 423
class HmdDesc(Structure):
    "This is a complete descriptor of the HMD."
    _pack_ = OVR_PTR_SIZE
    _fields_ = [
        ("Type", HmdType),                          #< The type of HMD.
        # skipping 64-bit only padding... # ("pad0", c_char * 4)),    #< \internal struct paddding.
        ("ProductName", c_char * 64),               #< UTF8-encoded product identification string (e.g. "Oculus Rift DK1").
        ("Manufacturer", c_char * 64),              #< UTF8-encoded HMD manufacturer identification string.
        ("VendorId", c_short),                      #< HID (USB) vendor identifier of the device.
        ("ProductId", c_short),                     #< HID (USB) product identifier of the device.
        ("SerialNumber", c_char * 24),              #< Sensor (and display) serial number.
        ("FirmwareMajor", c_short),                 #< Sensor firmware major version.
        ("FirmwareMinor", c_short),                 #< Sensor firmware minor version.
        ("CameraFrustumHFovInRadians", c_float),    #< External tracking camera frustum horizontal field-of-view (if present).
        ("CameraFrustumVFovInRadians", c_float),    #< External tracking camera frustum vertical field-of-view (if present).
        ("CameraFrustumNearZInMeters", c_float),    #< External tracking camera frustum near Z (if present).
        ("CameraFrustumFarZInMeters", c_float),     #< External tracking camera frustum far Z (if present).
        ("AvailableHmdCaps", c_uint),              #< Capability bits described by ovrHmdCaps which the HMD currently supports.
        ("DefaultHmdCaps", c_uint),                #< Capability bits described by ovrHmdCaps which are default for the current Hmd.
        ("AvailableTrackingCaps", c_uint),         #< Capability bits described by ovrTrackingCaps which the system currently supports.
        ("DefaultTrackingCaps", c_uint),           #< Capability bits described by ovrTrackingCaps which are default for the current system.
        ("DefaultEyeFov", FovPort * Eye_Count),   #< Defines the recommended FOVs for the HMD.
        ("MaxEyeFov", FovPort * Eye_Count),       #< Defines the maximum FOVs for the HMD.
        ("Resolution", Sizei),                    #< Resolution of the full HMD screen (both eyes) in pixels.
        ("DisplayRefreshRate", c_float),            #< Nominal refresh rate of the display in cycles per second at the time of HMD creation.
        # skipping 64-bit only padding... # ("pad1", c_char * 4)),    #< \internal struct paddding.
    ]

    def __repr__(self):
        return "ovr.HmdDesc(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (self.Type, self.ProductName, self.Manufacturer, self.VendorId, self.ProductId, self.SerialNumber, self.FirmwareMajor, self.FirmwareMinor, self.CameraFrustumHFovInRadians, self.CameraFrustumVFovInRadians, self.CameraFrustumNearZInMeters, self.CameraFrustumFarZInMeters, self.AvailableHmdCaps, self.DefaultHmdCaps, self.AvailableTrackingCaps, self.DefaultTrackingCaps, self.DefaultEyeFov, self.MaxEyeFov, self.Resolution, self.DisplayRefreshRate)


# Translated from header file OVR_CAPI_0_8_0.h line 451
# Used as an opaque pointer to an OVR session.
Session = POINTER(HmdStruct) 


# Translated from header file OVR_CAPI_0_8_0.h line 454
# Deprecated synonym for ovrSession, to be removed in a future SDK.
Hmd = POINTER(HmdStruct) 


# Translated from header file OVR_CAPI_0_8_0.h line 459
# Bit flags describing the current status of sensor tracking.
#  The values must be the same as in enum StatusBits
#
# \see ovrTrackingState
#
StatusBits = ENUM_TYPE
Status_OrientationTracked    = 0x0001    #< Orientation is currently tracked (connected and in use).
Status_PositionTracked       = 0x0002    #< Position is currently tracked (false if out of range).
Status_CameraPoseTracked     = 0x0004    #< Camera pose is currently tracked.
Status_PositionConnected     = 0x0020    #< Position tracking hardware is connected.
Status_HmdConnected          = 0x0080    #< HMD Display is available and connected.


# Translated from header file OVR_CAPI_0_8_0.h line 475
class SensorData(Structure):
    """
    Specifies a reading we can query from the sensor.
    
    \see ovrTrackingState
    """
    _pack_ = 4
    _fields_ = [
        ("Accelerometer", Vector3f),     #< Acceleration reading in meters/second^2.
        ("Gyro", Vector3f),              #< Rotation rate in radians/second.
        ("Magnetometer", Vector3f),      #< Magnetic field in Gauss.
        ("Temperature", c_float),       #< Temperature of the sensor in degrees Celsius.
        ("TimeInSeconds", c_float),     #< Time when the reported IMU reading took place in seconds. \see ovr_GetTimeInSeconds
    ]

    def __repr__(self):
        return "ovr.SensorData(%s, %s, %s, %s, %s)" % (self.Accelerometer, self.Gyro, self.Magnetometer, self.Temperature, self.TimeInSeconds)


# Translated from header file OVR_CAPI_0_8_0.h line 489
class TrackingState(Structure):
    """
    Tracking state at a given absolute time (describes predicted HMD pose, etc.).
    Returned by ovr_GetTrackingState.
    
    \see ovr_GetTrackingState
    """
    _pack_ = 8
    _fields_ = [
        # Predicted head pose (and derivatives) at the requested absolute time.
        # The look-ahead interval is equal to (HeadPose.TimeInSeconds - RawSensorData.TimeInSeconds).
        ("HeadPose", PoseStatef), 
        # Current pose of the external camera (if present).
        # This pose includes camera tilt (roll and pitch). For a leveled coordinate
        # system use LeveledCameraPose.
        ("CameraPose", Posef), 
        # Camera frame aligned with gravity.
        # This value includes position and yaw of the camera, but not roll and pitch.
        # It can be used as a reference point to render real-world objects in the correct location.
        ("LeveledCameraPose", Posef), 
        # The most recent calculated pose for each hand when hand controller tracking is present.
        # HandPoses[ovrHand_Left] refers to the left hand and HandPoses[ovrHand_Right] to the right hand.
        # These values can be combined with ovrInputState for complete hand controller information.
        ("HandPoses", PoseStatef * 2), 
        # The most recent sensor data received from the HMD.
        ("RawSensorData", SensorData), 
        # Tracking status described by ovrStatusBits.
        ("StatusFlags", c_uint), 
        # Hand status flags described by ovrStatusBits.
        # Only ovrStatus_OrientationTracked and ovrStatus_PositionTracked are reported.
        ("HandStatusFlags", c_uint * 2), 
        # Tags the vision processing results to a certain frame counter number.
        ("LastCameraFrameCounter", c_uint32), 
        ("pad0", c_char * 4),  #< \internal struct padding
    ]

    def __repr__(self):
        return "ovr.TrackingState(%s, %s, %s, %s, %s, %s, %s, %s)" % (self.HeadPose, self.CameraPose, self.LeveledCameraPose, self.HandPoses, self.RawSensorData, self.StatusFlags, self.HandStatusFlags, self.LastCameraFrameCounter)


# Translated from header file OVR_CAPI_0_8_0.h line 533
class EyeRenderDesc(Structure):
    """
    Rendering information for each eye. Computed by ovr_GetRenderDesc() based on the
    specified FOV. Note that the rendering viewport is not included
    here as it can be specified separately and modified per frame by
    passing different Viewport values in the layer structure.
    
    \see ovr_GetRenderDesc
    """
    _pack_ = 4
    _fields_ = [
        ("Eye", EyeType),                         #< The eye index to which this instance corresponds.
        ("Fov", FovPort),                         #< The field of view.
        ("DistortedViewport", Recti),           #< Distortion viewport.
        ("PixelsPerTanAngleAtCenter", Vector2f),   #< How many display pixels will fit in tan(angle) = 1.
        ("HmdToEyeViewOffset", Vector3f),          #< Translation of each eye.
    ]

    def __repr__(self):
        return "ovr.EyeRenderDesc(%s, %s, %s, %s, %s)" % (self.Eye, self.Fov, self.DistortedViewport, self.PixelsPerTanAngleAtCenter, self.HmdToEyeViewOffset)


# Translated from header file OVR_CAPI_0_8_0.h line 550
class TimewarpProjectionDesc(Structure):
    """
    Projection information for ovrLayerEyeFovDepth.
    
    Use the utility function ovrTimewarpProjectionDesc_FromProjection to
    generate this structure from the application's projection matrix.
    
    \see ovrLayerEyeFovDepth, ovrTimewarpProjectionDesc_FromProjection
    """
    _pack_ = 4
    _fields_ = [
        ("Projection22", c_float),      #< Projection matrix element [2][2].
        ("Projection23", c_float),      #< Projection matrix element [2][3].
        ("Projection32", c_float),      #< Projection matrix element [3][2].
    ]

    def __repr__(self):
        return "ovr.TimewarpProjectionDesc(%s, %s, %s)" % (self.Projection22, self.Projection23, self.Projection32)


# Translated from header file OVR_CAPI_0_8_0.h line 565
class ViewScaleDesc(Structure):
    """
    Contains the data necessary to properly calculate position info for various layer types.
    - HmdToEyeViewOffset is the same value pair provided in ovrEyeRenderDesc.
    - HmdSpaceToWorldScaleInMeters is used to scale player motion into in-application units.
      In other words, it is how big an in-application unit is in the player's physical meters.
      For example, if the application uses inches as its units then HmdSpaceToWorldScaleInMeters would be 0.0254.
      Note that if you are scaling the player in size, this must also scale. So if your application
      units are inches, but you're shrinking the player to half their normal size, then
      HmdSpaceToWorldScaleInMeters would be 0.0254*2.0.
    
    \see ovrEyeRenderDesc, ovr_SubmitFrame
    """
    _pack_ = 4
    _fields_ = [
        ("HmdToEyeViewOffset", Vector3f * Eye_Count),    #< Translation of each eye.
        ("HmdSpaceToWorldScaleInMeters", c_float),        #< Ratio of viewer units to meter units.
    ]

    def __repr__(self):
        return "ovr.ViewScaleDesc(%s, %s)" % (self.HmdToEyeViewOffset, self.HmdSpaceToWorldScaleInMeters)


# Translated from header file OVR_CAPI_0_8_0.h line 586
# These types are used to hide platform-specific details when passing
# render device, OS, and texture data to the API.
#
# The benefit of having these wrappers versus platform-specific API functions is
# that they allow application glue code to be portable. A typical example is an
# engine that has multiple back ends, such as GL and D3D. Portable code that calls
# these back ends can also use LibOVR. To do this, back ends can be modified
# to return portable types such as ovrTexture and ovrRenderAPIConfig.
RenderAPIType = ENUM_TYPE
RenderAPI_None         = 0          #< No API
RenderAPI_OpenGL       = 1          #< OpenGL
RenderAPI_Android_GLES = 2          #< OpenGL ES
RenderAPI_D3D11        = 5          #< DirectX 11.
RenderAPI_Count        = 4          #< \internal Count of enumerated elements.


# Translated from header file OVR_CAPI_0_8_0.h line 605
class TextureHeader(Structure):
    """
    API-independent part of a texture descriptor.
    
    ovrTextureHeader is a common struct present in all ovrTexture struct types.
    """
    _pack_ = 4
    _fields_ = [
        ("API", RenderAPIType),            #< The API type to which this texture belongs.
        ("TextureSize", Sizei),    #< Size of this texture in pixels.
    ]

    def __repr__(self):
        return "ovr.TextureHeader(%s, %s)" % (self.API, self.TextureSize)


# Translated from header file OVR_CAPI_0_8_0.h line 616
class Texture(Structure):
    """
    Contains platform-specific information about a texture.
    Aliases to one of ovrD3D11Texture or ovrGLTexture.
    
    \see ovrD3D11Texture, ovrGLTexture.
    """
    _pack_ = OVR_PTR_SIZE
    _fields_ = [
        ("Header", TextureHeader),                     #< API-independent header.
        # skipping 64-bit only padding... # ("pad0", c_char * 4)),     #< \internal struct padding
        ("PlatformData", POINTER(c_uint) * 8),            #< Specialized in ovrGLTextureData, ovrD3D11TextureData etc.
    ]

    def __repr__(self):
        return "ovr.Texture(%s, %s)" % (self.Header, self.PlatformData)


# Translated from header file OVR_CAPI_0_8_0.h line 629
class SwapTextureSet(Structure):
    """
    Describes a set of textures that act as a rendered flip chain.
    
    An ovrSwapTextureSet per layer is passed to ovr_SubmitFrame via one of the ovrLayer types.
    The TextureCount refers to the flip chain count and not an eye count.
    See the layer structs and functions for information about how to use ovrSwapTextureSet.
    
    ovrSwapTextureSets must be created by either the ovr_CreateSwapTextureSetD3D11 or
    ovr_CreateSwapTextureSetGL factory function, and must be destroyed by ovr_DestroySwapTextureSet.
    
    \see ovr_CreateSwapTextureSetD3D11, ovr_CreateSwapTextureSetGL, ovr_DestroySwapTextureSet.
    """
    _pack_ = OVR_PTR_SIZE
    _fields_ = [
        ("Textures", POINTER(Texture)),        #< Points to an array of ovrTextures.
        ("TextureCount", c_int),    #< The number of textures referenced by the Textures array.
        # CurrentIndex specifies which of the Textures will be used by the ovr_SubmitFrame call.
        # This is manually incremented by the application, typically in a round-robin manner.
        #
        # Before selecting a Texture as a rendertarget, the application should increment CurrentIndex by
        # 1 and wrap it back to 0 if CurrentIndex == TextureCount, so that it gets a fresh rendertarget,
        # one that is not currently being used for display. It can then render to Textures[CurrentIndex].
        #
        # After rendering, the application calls ovr_SubmitFrame using that same CurrentIndex value
        # to display the new rendertarget.
        #
        # The application can submit multiple frames with the same ovrSwapTextureSet and CurrentIndex
        # value if the rendertarget does not need to be updated, for example when displaying an
        # information display whose text has not changed since the previous frame.
        #
        # Multiple layers can use the same ovrSwapTextureSet at the same time - there is no need to
        # create a unique ovrSwapTextureSet for each layer. However, all the layers using a particular
        # ovrSwapTextureSet will share the same value of CurrentIndex, so they cannot use different
        # textures within the ovrSwapTextureSet.
        #
        # Once a particular Textures[CurrentIndex] has been sent to ovr_SubmitFrame, that texture
        # should not be rendered to until a subsequent ovr_SubmitFrame is made (either with a
        # different CurrentIndex value, or with a different ovrSwapTextureSet, or disabling the layer).
        ("CurrentIndex", c_int), 
    ]

    def __repr__(self):
        return "ovr.SwapTextureSet(%s, %s, %s)" % (self.Textures, self.TextureCount, self.CurrentIndex)


# Translated from header file OVR_CAPI_0_8_0.h line 674
# Describes button input types.
# Button inputs are combined; that is they will be reported as pressed if they are 
# pressed on either one of the two devices.
# The ovrButton_Up/Down/Left/Right map to both XBox D-Pad and directional buttons.
# The ovrButton_Enter and ovrButton_Return map to Start and Back controller buttons, respectively.
Button = ENUM_TYPE
Button_A         = 0x00000001
Button_B         = 0x00000002
Button_RThumb    = 0x00000004
Button_RShoulder = 0x00000008
Button_X         = 0x00000100
Button_Y         = 0x00000200
Button_LThumb    = 0x00000400  
Button_LShoulder = 0x00000800
# Navigation through DPad.
Button_Up        = 0x00010000
Button_Down      = 0x00020000
Button_Left      = 0x00040000
Button_Right     = 0x00080000
Button_Enter     = 0x00100000 # Start on XBox controller.
Button_Back      = 0x00200000 # Back on Xbox controller.     
Button_Private   = 0x00400000 | 0x00800000 | 0x01000000,


# Translated from header file OVR_CAPI_0_8_0.h line 703
# Describes touch input types.
# These values map to capacitive touch values reported ovrInputState::Touch.
# Some of these values are mapped to button bits for consistency.
Touch = ENUM_TYPE
Touch_A              = Button_A
Touch_B              = Button_B
Touch_RThumb         = Button_RThumb
Touch_RIndexTrigger  = 0x00000010
Touch_X              = Button_X
Touch_Y              = Button_Y
Touch_LThumb         = Button_LThumb
Touch_LIndexTrigger  = 0x00001000
# Finger pose state 
# Derived internally based on distance, proximity to sensors and filtering.
Touch_RIndexPointing = 0x00000020
Touch_RThumbUp       = 0x00000040    
Touch_LIndexPointing = 0x00002000
Touch_LThumbUp       = 0x00004000


# Translated from header file OVR_CAPI_0_8_0.h line 727
# Specifies which controller is connected; multiple can be connected at once.
ControllerType = ENUM_TYPE
ControllerType_None      = 0x00
ControllerType_LTouch    = 0x01
ControllerType_RTouch    = 0x02
ControllerType_Touch     = 0x03
ControllerType_XBox      = 0x10
ControllerType_All       = 0xff


# Translated from header file OVR_CAPI_0_8_0.h line 742
# Provides names for the left and right hand array indexes.
#
# \see ovrInputState, ovrTrackingState
# 
HandType = ENUM_TYPE
Hand_Left  = 0
Hand_Right = 1


# Translated from header file OVR_CAPI_0_8_0.h line 756
class InputState(Structure):
    """
    ovrInputState describes the complete controller input state, including Oculus Touch,
    and XBox gamepad. If multiple inputs are connected and used at the same time,
    their inputs are combined.
    """
    _fields_ = [
        # System type when the controller state was last updated.
        ("TimeInSeconds", c_double), 
        # Described by ovrControllerType. Indicates which ControllerTypes are present.
        ("ConnectedControllerTypes", c_uint), 
        # Values for buttons described by ovrButton.
        ("Buttons", c_uint), 
        # Touch values for buttons and sensors as described by ovrTouch.
        ("Touches", c_uint), 
        # Left and right finger trigger values (ovrHand_Left and ovrHand_Right), in the range 0.0 to 1.0f.
        ("IndexTrigger", c_float * 2),  
        # Left and right hand trigger values (ovrHand_Left and ovrHand_Right), in the range 0.0 to 1.0f.
        ("HandTrigger", c_float * 2), 
        # Horizontal and vertical thumbstick axis values (ovrHand_Left and ovrHand_Right), in the range -1.0f to 1.0f.
        ("Thumbstick", Vector2f * 2), 
    ]

    def __repr__(self):
        return "ovr.InputState(%s, %s, %s, %s, %s, %s, %s)" % (self.TimeInSeconds, self.ConnectedControllerTypes, self.Buttons, self.Touches, self.IndexTrigger, self.HandTrigger, self.Thumbstick)


# Translated from header file OVR_CAPI_0_8_0.h line 789
# Initialization flags.
#
# \see ovrInitParams, ovr_Initialize
#
InitFlags = ENUM_TYPE
# When a debug library is requested, a slower debugging version of the library will
# run which can be used to help solve problems in the library and debug application code.
Init_Debug          = 0x00000001
# When a version is requested, the LibOVR runtime respects the RequestedMinorVersion
# field and verifies that the RequestedMinorVersion is supported.
Init_RequestVersion = 0x00000004
# These bits are writable by user code.
Init_WritableBits   = 0x00ffffff


# Translated from header file OVR_CAPI_0_8_0.h line 810
# Logging levels
#
# \see ovrInitParams, ovrLogCallback
#
LogLevel = ENUM_TYPE
LogLevel_Debug    = 0 #< Debug-level log event.
LogLevel_Info     = 1 #< Info-level log event.
LogLevel_Error    = 2 #< Error-level log event.


# Translated from header file OVR_CAPI_0_8_0.h line 834
class InitParams(Structure):
    """
    Parameters for ovr_Initialize.
    
    \see ovr_Initialize
    """
    _pack_ = 8
    _fields_ = [
        # Flags from ovrInitFlags to override default behavior.
        # Use 0 for the defaults.
        ("Flags", c_uint32), 
        # Requests a specific minimum minor version of the LibOVR runtime.
        # Flags must include ovrInit_RequestVersion or this will be ignored
        # and OVR_MINOR_VERSION will be used.
        ("RequestedMinorVersion", c_uint32), 
        # User-supplied log callback function, which may be called at any time
        # asynchronously from multiple threads until ovr_Shutdown completes.
        # Use NULL to specify no log callback.
        ("LogCallback", LogCallback), 
        # User-supplied data which is passed as-is to LogCallback. Typically this
        # is used to store an application-specific pointer which is read in the
        # callback function.
        ("UserData", POINTER(c_uint)), 
        # Relative number of milliseconds to wait for a connection to the server
        # before failing. Use 0 for the default timeout.
        ("ConnectionTimeoutMS", c_uint32), 
        # skipping 64-bit only padding... # ("pad0", c_char * 4)),  #< \internal
    ]

    def __repr__(self):
        return "ovr.InitParams(%s, %s, %s, %s, %s)" % (self.Flags, self.RequestedMinorVersion, self.LogCallback, self.UserData, self.ConnectionTimeoutMS)


# Translated from header file OVR_CAPI_0_8_0.h line 906
libovr.ovr_Initialize.restype = Result
libovr.ovr_Initialize.argtypes = [POINTER(InitParams)]
def initialize(params):
    """
    Initializes LibOVR
    
    Initialize LibOVR for application usage. This includes finding and loading the LibOVRRT
    shared library. No LibOVR API functions, other than ovr_GetLastErrorInfo, can be called
    unless ovr_Initialize succeeds. A successful call to ovr_Initialize must be eventually
    followed by a call to ovr_Shutdown. ovr_Initialize calls are idempotent.
    Calling ovr_Initialize twice does not require two matching calls to ovr_Shutdown.
    If already initialized, the return value is ovr_Success.
    
    LibOVRRT shared library search order:
         -# Current working directory (often the same as the application directory).
         -# Module directory (usually the same as the application directory,
            but not if the module is a separate shared library).
         -# Application directory
         -# Development directory (only if OVR_ENABLE_DEVELOPER_SEARCH is enabled,
            which is off by default).
         -# Standard OS shared library search location(s) (OS-specific).
    
    \param params Specifies custom initialization options. May be NULL to indicate default options.
    \return Returns an ovrResult indicating success or failure. In the case of failure, use
            ovr_GetLastErrorInfo to get more information. Example failed results include:
        - ovrError_Initialize: Generic initialization error.
        - ovrError_LibLoad: Couldn't load LibOVRRT.
        - ovrError_LibVersion: LibOVRRT version incompatibility.
        - ovrError_ServiceConnection: Couldn't connect to the OVR Service.
        - ovrError_ServiceVersion: OVR Service version incompatibility.
        - ovrError_IncompatibleOS: The operating system version is incompatible.
        - ovrError_DisplayInit: Unable to initialize the HMD display.
        - ovrError_ServerStart:  Unable to start the server. Is it already running?
        - ovrError_Reinitialization: Attempted to re-initialize with a different version.
    
    <b>Example code</b>
        \code{.cpp}
            ovrResult result = ovr_Initialize(NULL);
            if(OVR_FAILURE(result)) {
                ovrErrorInfo errorInfo;
                ovr_GetLastErrorInfo(&errorInfo);
                DebugLog("ovr_Initialize failed: %s", errorInfo.ErrorString);
                return false;
            }
            [...]
        \endcode
    
    \see ovr_Shutdown
    """
    result = libovr.ovr_Initialize(byref(params))
    if FAILURE(result):
        raise Exception("Call to function initialize failed")    
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 954
libovr.ovr_Shutdown.restype = None
def shutdown():
    """
    Shuts down LibOVR
    
    A successful call to ovr_Initialize must be eventually matched by a call to ovr_Shutdown.
    After calling ovr_Shutdown, no LibOVR functions can be called except ovr_GetLastErrorInfo
    or another ovr_Initialize. ovr_Shutdown invalidates all pointers, references, and created objects
    previously returned by LibOVR functions. The LibOVRRT shared library can be unloaded by
    ovr_Shutdown.
    
    \see ovr_Initialize
    """
    result = libovr.ovr_Shutdown()
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 967
class ErrorInfo(Structure):
    """
    Provides information about the last error.
    \see ovr_GetLastErrorInfo
    """
    _fields_ = [
        ("Result", Result),                #< The result from the last API call that generated an error ovrResult.
        ("ErrorString", c_char * 512),      #< A UTF8-encoded null-terminated English string describing the problem. The format of this string is subject to change in future versions.
    ]

    def __repr__(self):
        return "ovr.ErrorInfo(%s, %s)" % (self.Result, self.ErrorString)


# Translated from header file OVR_CAPI_0_8_0.h line 976
libovr.ovr_GetLastErrorInfo.restype = None
libovr.ovr_GetLastErrorInfo.argtypes = [POINTER(ErrorInfo)]
def getLastErrorInfo():
    """
    Returns information about the most recent failed return value by the
    current thread for this library.
    
    This function itself can never generate an error.
    The last error is never cleared by LibOVR, but will be overwritten by new errors.
    Do not use this call to determine if there was an error in the last API
    call as successful API calls don't clear the last ovrErrorInfo.
    To avoid any inconsistency, ovr_GetLastErrorInfo should be called immediately
    after an API function that returned a failed ovrResult, with no other API
    functions called in the interim.
    
    \param[out] errorInfo The last ovrErrorInfo for the current thread.
    
    \see ovrErrorInfo
    """
    errorInfo = ErrorInfo()
    result = libovr.ovr_GetLastErrorInfo(byref(errorInfo))
    return errorInfo


# Translated from header file OVR_CAPI_0_8_0.h line 994
libovr.ovr_GetVersionString.restype = c_char_p
def getVersionString():
    """
    Returns the version string representing the LibOVRRT version.
    
    The returned string pointer is valid until the next call to ovr_Shutdown.
    
    Note that the returned version string doesn't necessarily match the current
    OVR_MAJOR_VERSION, etc., as the returned string refers to the LibOVRRT shared
    library version and not the locally compiled interface version.
    
    The format of this string is subject to change in future versions and its contents
    should not be interpreted.
    
    \return Returns a UTF8-encoded null-terminated version string.
    """
    result = libovr.ovr_GetVersionString()
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1010
libovr.ovr_TraceMessage.restype = c_int
libovr.ovr_TraceMessage.argtypes = [c_int, c_char_p]
def traceMessage(level, message):
    """
    Writes a message string to the LibOVR tracing mechanism (if enabled).
    
    This message will be passed back to the application via the ovrLogCallback if
    it was registered.
    
    \param[in] level One of the ovrLogLevel constants.
    \param[in] message A UTF8-encoded null-terminated string.
    \return returns the strlen of the message or a negative value if the message is too large.
    
    \see ovrLogLevel, ovrLogCallback
    """
    result = libovr.ovr_TraceMessage(level, message)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1031
libovr.ovr_GetHmdDesc.restype = HmdDesc
libovr.ovr_GetHmdDesc.argtypes = [Session]
def getHmdDesc(session):
    """
    Returns information about the current HMD.
    
    ovr_Initialize must have first been called in order for this to succeed, otherwise ovrHmdDesc::Type
    will be reported as ovrHmd_None.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create, else NULL in which
                   case this function detects whether an HMD is present and returns its info if so.
    
    \return Returns an ovrHmdDesc. If the hmd is NULL and ovrHmdDesc::Type is ovrHmd_None then 
            no HMD is present.
    """
    result = libovr.ovr_GetHmdDesc(session)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1045
libovr.ovr_Create.restype = Result
libovr.ovr_Create.argtypes = [POINTER(Session), POINTER(GraphicsLuid)]
def create():
    """
    Creates a handle to a VR session.
    
    Upon success the returned ovrSession must be eventually freed with ovr_Destroy when it is no longer needed.
    A second call to ovr_Create will result in an error return value if the previous Hmd has not been destroyed.
    
    \param[out] pSession Provides a pointer to an ovrSession which will be written to upon success.
    \param[out] luid Provides a system specific graphics adapter identifier that locates which
    graphics adapter has the HMD attached. This must match the adapter used by the application
    or no rendering output will be possible. This is important for stability on multi-adapter systems. An
    application that simply chooses the default adapter will not run reliably on multi-adapter systems.
    \return Returns an ovrResult indicating success or failure. Upon failure
            the returned pHmd will be NULL.
    
    <b>Example code</b>
        \code{.cpp}
            ovrSession session;
            ovrGraphicsLuid luid;
            ovrResult result = ovr_Create(&session, &luid);
            if(OVR_FAILURE(result))
               ...
        \endcode
    
    \see ovr_Destroy
    """
    pSession = Session()
    pLuid = GraphicsLuid()
    result = libovr.ovr_Create(byref(pSession), byref(pLuid))
    if FAILURE(result):
        raise Exception("Call to function create failed")    
    return pSession, pLuid


# Translated from header file OVR_CAPI_0_8_0.h line 1072
libovr.ovr_Destroy.restype = None
libovr.ovr_Destroy.argtypes = [Session]
def destroy(session):
    """
    Destroys the HMD.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \see ovr_Create
    """
    result = libovr.ovr_Destroy(session)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1080
class SessionStatus(Structure):
    """
    Specifies status information for the current session.
    
    \see ovr_GetSessionStatus
    """
    _fields_ = [
        ("HasVrFocus", Bool),    #< True if the process has VR focus and thus is visible in the HMD.
        ("HmdPresent", Bool),    #< True if an HMD is present.  
    ]

    def __repr__(self):
        return "ovr.SessionStatus(%s, %s)" % (self.HasVrFocus, self.HmdPresent)


# Translated from header file OVR_CAPI_0_8_0.h line 1091
libovr.ovr_GetSessionStatus.restype = Result
libovr.ovr_GetSessionStatus.argtypes = [Session, POINTER(SessionStatus)]
def getSessionStatus(session):
    """
    Returns status information for the application.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[out] sessionStatus Provides an ovrSessionStatus that is filled in.
    
    \return Returns an ovrResult indicating success or failure. In the case of 
            failure, use ovr_GetLastErrorInfo to get more information.
    """
    sessionStatus = SessionStatus()
    result = libovr.ovr_GetSessionStatus(session, byref(sessionStatus))
    if FAILURE(result):
        raise Exception("Call to function getSessionStatus failed")    
    return sessionStatus


# Translated from header file OVR_CAPI_0_8_0.h line 1102
libovr.ovr_GetEnabledCaps.restype = c_uint
libovr.ovr_GetEnabledCaps.argtypes = [Session]
def getEnabledCaps(session):
    """
    Returns ovrHmdCaps bits that are currently enabled.
    
    Note that this value is different from ovrHmdDesc::AvailableHmdCaps, which describes what
    capabilities are available for that HMD.
    
    \return Returns a combination of zero or more ovrHmdCaps.
    \see ovrHmdCaps
    """
    result = libovr.ovr_GetEnabledCaps(session)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1113
libovr.ovr_SetEnabledCaps.restype = None
libovr.ovr_SetEnabledCaps.argtypes = [Session, c_uint]
def setEnabledCaps(session, hmdCaps):
    """
    Modifies capability bits described by ovrHmdCaps that can be modified,
    such as ovrHmdCap_LowPersistance.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] hmdCaps A combination of 0 or more ovrHmdCaps.
    
    \see ovrHmdCaps
    """
    result = libovr.ovr_SetEnabledCaps(session, hmdCaps)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1137
libovr.ovr_GetTrackingCaps.restype = c_uint
libovr.ovr_GetTrackingCaps.argtypes = [Session]
def getTrackingCaps(session):
    """
    Returns the current tracking caps
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    
    \return Returns caps from ovrTrackingCaps.
    
    \see ovrTrackingCaps
    """
    result = libovr.ovr_GetTrackingCaps(session)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1148
libovr.ovr_ConfigureTracking.restype = Result
libovr.ovr_ConfigureTracking.argtypes = [Session, c_uint, c_uint]
def configureTracking(session, requestedTrackingCaps, requiredTrackingCaps):
    """
    Starts sensor sampling, enabling specified capabilities, described by ovrTrackingCaps.
    
    Use 0 for both requestedTrackingCaps and requiredTrackingCaps to disable tracking.
    ovr_ConfigureTracking can be called multiple times with the same or different values
    for a given ovrSession.
    
    ovr_Create automatically enables full tracking supported by the given device. This function
    is not needed unless the disabling of tracking features is required. 
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    
    \param[in] requestedTrackingCaps specifies support that is requested. The function will succeed
               even if these caps are not available (i.e. sensor or camera is unplugged). Support
               will automatically be enabled if the device is plugged in later. Software should
               check ovrTrackingState.StatusFlags for real-time status.
    
    \param[in] requiredTrackingCaps Specifies sensor capabilities required at the time of the call.
               If they are not available, the function will fail. Pass 0 if only specifying
               requestedTrackingCaps.
    
    \return Returns an ovrResult indicating success or failure. In the case of failure, use
            ovr_GetLastErrorInfo to get more information.
    
    \see ovrTrackingCaps, ovr_Create
    """
    result = libovr.ovr_ConfigureTracking(session, requestedTrackingCaps, requiredTrackingCaps)
    if FAILURE(result):
        raise Exception("Call to function configureTracking failed")    
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1177
libovr.ovr_RecenterPose.restype = None
libovr.ovr_RecenterPose.argtypes = [Session]
def recenterPose(session):
    """
    Re-centers the sensor position and orientation.
    
    This resets the (x,y,z) positional components and the yaw orientation component.
    The Roll and pitch orientation components are always determined by gravity and cannot
    be redefined. All future tracking will report values relative to this new reference position.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    """
    result = libovr.ovr_RecenterPose(session)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1188
libovr.ovr_GetTrackingState.restype = TrackingState
libovr.ovr_GetTrackingState.argtypes = [Session, c_double, Bool]
def getTrackingState(session, absTime, latencyMarker):
    """
    Returns tracking state reading based on the specified absolute system time.
    
    Pass an absTime value of 0.0 to request the most recent sensor reading. In this case
    both PredictedPose and SamplePose will have the same value.
    
    This may also be used for more refined timing of front buffer rendering logic, and so on.
    This may be called by multiple threads.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] absTime Specifies the absolute future time to predict the return
               ovrTrackingState value. Use 0 to request the most recent tracking state.
    \param[in] latencyMarker Specifies that this call is the point in time where
               the "App-to-Mid-Photon" latency timer starts from. If a given ovrLayer
               provides "SensorSampleTimestamp", that will override the value stored here.
    \return Returns the ovrTrackingState that is predicted for the given absTime.
    
    \see ovrTrackingState, ovr_GetEyePoses, ovr_GetTimeInSeconds
    """
    result = libovr.ovr_GetTrackingState(session, absTime, toOvrBool(latencyMarker))
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1209
libovr.ovr_GetInputState.restype = Result
libovr.ovr_GetInputState.argtypes = [Session, c_uint, POINTER(InputState)]
def getInputState(session, controllerTypeMask):
    """
    Returns the most recent input state for controllers, without positional tracking info.
    Developers can tell whether the same state was returned by checking the PacketNumber.
    
    \param[out] inputState Input state that will be filled in.
    \param[in] controllerTypeMask Specifies which controllers the input will be returned for.
               Described by ovrControllerType.
    \return Returns ovrSuccess if the new state was successfully obtained.
    
    \see ovrControllerType
    """
    inputState = InputState()
    result = libovr.ovr_GetInputState(session, controllerTypeMask, byref(inputState))
    if FAILURE(result):
        raise Exception("Call to function getInputState failed")    
    return inputState


# Translated from header file OVR_CAPI_0_8_0.h line 1222
libovr.ovr_SetControllerVibration.restype = Result
libovr.ovr_SetControllerVibration.argtypes = [Session, c_uint, c_float, c_float]
def setControllerVibration(session, controllerTypeMask, frequency, amplitude):
    """
    Turns on vibration of the given controller.
    
    To disable vibration, call ovr_SetControllerVibration with an amplitude of 0.
    Vibration automatically stops after a nominal amount of time, so if you want vibration 
    to be continuous over multiple seconds then you need to call this function periodically.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] controllerTypeMask Specifies controllers to apply the vibration to.
    \param[in] frequency Specifies a vibration frequency in the range of 0.0 to 1.0. 
               Currently the only valid values are 0.0, 0.5, and 1.0 and other values will
               be clamped to one of these.
    \param[in] amplitude Specifies a vibration amplitude in the range of 0.0 to 1.0.
    
    \return Returns ovrSuccess upon success.
    
    \see ovrControllerType
    """
    result = libovr.ovr_SetControllerVibration(session, controllerTypeMask, frequency, amplitude)
    if FAILURE(result):
        raise Exception("Call to function setControllerVibration failed")    
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1259
# Describes layer types that can be passed to ovr_SubmitFrame.
# Each layer type has an associated struct, such as ovrLayerEyeFov.
#
# \see ovrLayerHeader
#
LayerType = ENUM_TYPE
LayerType_Disabled              = 0         #< Layer is disabled.
LayerType_EyeFov                = 1         #< Described by ovrLayerEyeFov.
LayerType_EyeFovDepth           = 2         #< Described by ovrLayerEyeFovDepth.
LayerType_Quad                  = 3         #< Described by ovrLayerQuad. Was called ovrLayerType_QuadInWorld.
# enum 4 used to be ovrLayerType_QuadHeadLocked. Instead, use ovrLayerType_Quad with ovrLayerFlag_HeadLocked.
LayerType_EyeMatrix             = 5         #< Described by ovrLayerEyeMatrix.
LayerType_Direct                = 6         #< Described by ovrLayerDirect. Passthrough for debugging and custom rendering.


# Translated from header file OVR_CAPI_0_8_0.h line 1277
# Identifies flags used by ovrLayerHeader and which are passed to ovr_SubmitFrame.
#
# \see ovrLayerHeader
#
LayerFlags = ENUM_TYPE
# ovrLayerFlag_HighQuality mode costs performance, but looks better.
LayerFlag_HighQuality               = 0x01
# ovrLayerFlag_TextureOriginAtBottomLeft: the opposite is TopLeft.
# Generally this is false for D3D, true for OpenGL.
LayerFlag_TextureOriginAtBottomLeft = 0x02
# Mark this surface as "headlocked", which means it is specified
# relative to the HMD and moves with it, rather than being specified
# relative to sensor/torso space and remaining still while the head moves.
# ovrLayerType_QuadHeadLocked is now ovrLayerType_Quad plus this flag.
# However the flag can be applied to any layer type except ovrLayerType_Direct
# to achieve a similar effect.
LayerFlag_HeadLocked                = 0x04


# Translated from header file OVR_CAPI_0_8_0.h line 1301
class LayerHeader(Structure):
    """
    Defines properties shared by all ovrLayer structs, such as ovrLayerEyeFov.
    
    ovrLayerHeader is used as a base member in these larger structs.
    This struct cannot be used by itself except for the case that Type is ovrLayerType_Disabled.
    
    \see ovrLayerType, ovrLayerFlags
    """
    _pack_ = OVR_PTR_SIZE
    _fields_ = [
        ("Type", LayerType),    #< Described by ovrLayerType.
        ("Flags", c_uint),   #< Described by ovrLayerFlags.
    ]

    def __repr__(self):
        return "ovr.LayerHeader(%s, %s)" % (self.Type, self.Flags)


# Translated from header file OVR_CAPI_0_8_0.h line 1315
class LayerEyeFov(Structure):
    """
    Describes a layer that specifies a monoscopic or stereoscopic view.
    This is the kind of layer that's typically used as layer 0 to ovr_SubmitFrame,
    as it is the kind of layer used to render a 3D stereoscopic view.
    
    Three options exist with respect to mono/stereo texture usage:
       - ColorTexture[0] and ColorTexture[1] contain the left and right stereo renderings, respectively.
         Viewport[0] and Viewport[1] refer to ColorTexture[0] and ColorTexture[1], respectively.
       - ColorTexture[0] contains both the left and right renderings, ColorTexture[1] is NULL,
         and Viewport[0] and Viewport[1] refer to sub-rects with ColorTexture[0].
       - ColorTexture[0] contains a single monoscopic rendering, and Viewport[0] and
         Viewport[1] both refer to that rendering.
    
    \see ovrSwapTextureSet, ovr_SubmitFrame
    """
    _pack_ = OVR_PTR_SIZE
    _fields_ = [
        # Header.Type must be ovrLayerType_EyeFov.
        ("Header", LayerHeader), 
        # ovrSwapTextureSets for the left and right eye respectively.
        # The second one of which can be NULL for cases described above.
        ("ColorTexture", POINTER(SwapTextureSet) * Eye_Count), 
        # Specifies the ColorTexture sub-rect UV coordinates.
        # Both Viewport[0] and Viewport[1] must be valid.
        ("Viewport", Recti * Eye_Count), 
        # The viewport field of view.
        ("Fov", FovPort * Eye_Count), 
        # Specifies the position and orientation of each eye view, with the position specified in meters.
        # RenderPose will typically be the value returned from ovr_CalcEyePoses,
        # but can be different in special cases if a different head pose is used for rendering.
        ("RenderPose", Posef * Eye_Count), 
        # Specifies the timestamp when the source ovrPosef (used in calculating RenderPose)
        # was sampled from the SDK. Typically retrieved by calling ovr_GetTimeInSeconds
        # around the instant the application calls ovr_GetTrackingState
        # The main purpose for this is to accurately track app tracking latency.
        ("SensorSampleTime", c_double), 
    ]

    def __repr__(self):
        return "ovr.LayerEyeFov(%s, %s, %s, %s, %s, %s)" % (self.Header, self.ColorTexture, self.Viewport, self.Fov, self.RenderPose, self.SensorSampleTime)


# Translated from header file OVR_CAPI_0_8_0.h line 1359
class LayerEyeFovDepth(Structure):
    """
    Describes a layer that specifies a monoscopic or stereoscopic view,
    with depth textures in addition to color textures. This is typically used to support
    positional time warp. This struct is the same as ovrLayerEyeFov, but with the addition
    of DepthTexture and ProjectionDesc.
    
    ProjectionDesc can be created using ovrTimewarpProjectionDesc_FromProjection.
    
    Three options exist with respect to mono/stereo texture usage:
       - ColorTexture[0] and ColorTexture[1] contain the left and right stereo renderings, respectively.
         Viewport[0] and Viewport[1] refer to ColorTexture[0] and ColorTexture[1], respectively.
       - ColorTexture[0] contains both the left and right renderings, ColorTexture[1] is NULL,
         and Viewport[0] and Viewport[1] refer to sub-rects with ColorTexture[0].
       - ColorTexture[0] contains a single monoscopic rendering, and Viewport[0] and
         Viewport[1] both refer to that rendering.
    
    \see ovrSwapTextureSet, ovr_SubmitFrame
    """
    _pack_ = OVR_PTR_SIZE
    _fields_ = [
        # Header.Type must be ovrLayerType_EyeFovDepth.
        ("Header", LayerHeader), 
        # ovrSwapTextureSets for the left and right eye respectively.
        # The second one of which can be NULL for cases described above.
        ("ColorTexture", POINTER(SwapTextureSet) * Eye_Count), 
        # Specifies the ColorTexture sub-rect UV coordinates.
        # Both Viewport[0] and Viewport[1] must be valid.
        ("Viewport", Recti * Eye_Count), 
        # The viewport field of view.
        ("Fov", FovPort * Eye_Count), 
        # Specifies the position and orientation of each eye view, with the position specified in meters.
        # RenderPose will typically be the value returned from ovr_CalcEyePoses,
        # but can be different in special cases if a different head pose is used for rendering.
        ("RenderPose", Posef * Eye_Count), 
        # Specifies the timestamp when the source ovrPosef (used in calculating RenderPose)
        # was sampled from the SDK. Typically retrieved by calling ovr_GetTimeInSeconds
        # around the instant the application calls ovr_GetTrackingState
        # The main purpose for this is to accurately track app tracking latency.
        ("SensorSampleTime", c_double), 
        # Depth texture for positional timewarp.
        # Must map 1:1 to the ColorTexture.
        ("DepthTexture", POINTER(SwapTextureSet) * Eye_Count), 
        # Specifies how to convert DepthTexture information into meters.
        # \see ovrTimewarpProjectionDesc_FromProjection
        ("ProjectionDesc", TimewarpProjectionDesc), 
    ]

    def __repr__(self):
        return "ovr.LayerEyeFovDepth(%s, %s, %s, %s, %s, %s, %s, %s)" % (self.Header, self.ColorTexture, self.Viewport, self.Fov, self.RenderPose, self.SensorSampleTime, self.DepthTexture, self.ProjectionDesc)


# Translated from header file OVR_CAPI_0_8_0.h line 1414
class LayerEyeMatrix(Structure):
    """
    Describes a layer that specifies a monoscopic or stereoscopic view.
    This uses a direct 3x4 matrix to map from view space to the UV coordinates.
    It is essentially the same thing as ovrLayerEyeFov but using a much
    lower level. This is mainly to provide compatibility with specific apps.
    Unless the application really requires this flexibility, it is usually better
    to use ovrLayerEyeFov.
    
    Three options exist with respect to mono/stereo texture usage:
       - ColorTexture[0] and ColorTexture[1] contain the left and right stereo renderings, respectively.
         Viewport[0] and Viewport[1] refer to ColorTexture[0] and ColorTexture[1], respectively.
       - ColorTexture[0] contains both the left and right renderings, ColorTexture[1] is NULL,
         and Viewport[0] and Viewport[1] refer to sub-rects with ColorTexture[0].
       - ColorTexture[0] contains a single monoscopic rendering, and Viewport[0] and
         Viewport[1] both refer to that rendering.
    
    \see ovrSwapTextureSet, ovr_SubmitFrame
    """
    _pack_ = OVR_PTR_SIZE
    _fields_ = [
        # Header.Type must be ovrLayerType_EyeMatrix.
        ("Header", LayerHeader), 
        # ovrSwapTextureSets for the left and right eye respectively.
        # The second one of which can be NULL for cases described above.
        ("ColorTexture", POINTER(SwapTextureSet) * Eye_Count), 
        # Specifies the ColorTexture sub-rect UV coordinates.
        # Both Viewport[0] and Viewport[1] must be valid.
        ("Viewport", Recti * Eye_Count), 
        # Specifies the position and orientation of each eye view, with the position specified in meters.
        # RenderPose will typically be the value returned from ovr_CalcEyePoses,
        # but can be different in special cases if a different head pose is used for rendering.
        ("RenderPose", Posef * Eye_Count), 
        # Specifies the mapping from a view-space vector
        # to a UV coordinate on the textures given above.
        # P = (x,y,z,1)*Matrix
        # TexU  = P.x/P.z
        # TexV  = P.y/P.z
        ("Matrix", Matrix4f * Eye_Count), 
        # Specifies the timestamp when the source ovrPosef (used in calculating RenderPose)
        # was sampled from the SDK. Typically retrieved by calling ovr_GetTimeInSeconds
        # around the instant the application calls ovr_GetTrackingState
        # The main purpose for this is to accurately track app tracking latency.
        ("SensorSampleTime", c_double), 
    ]

    def __repr__(self):
        return "ovr.LayerEyeMatrix(%s, %s, %s, %s, %s, %s)" % (self.Header, self.ColorTexture, self.Viewport, self.RenderPose, self.Matrix, self.SensorSampleTime)


# Translated from header file OVR_CAPI_0_8_0.h line 1468
class LayerQuad(Structure):
    """
    Describes a layer of Quad type, which is a single quad in world or viewer space.
    It is used for both ovrLayerType_Quad. This type of layer represents a single
    object placed in the world and not a stereo view of the world itself.
    
    A typical use of ovrLayerType_Quad is to draw a television screen in a room
    that for some reason is more convenient to draw as a layer than as part of the main
    view in layer 0. For example, it could implement a 3D popup GUI that is drawn at a
    higher resolution than layer 0 to improve fidelity of the GUI.
    
    Quad layers are visible from both sides; they are not back-face culled.
    
    \see ovrSwapTextureSet, ovr_SubmitFrame
    """
    _pack_ = OVR_PTR_SIZE
    _fields_ = [
        # Header.Type must be ovrLayerType_Quad.
        ("Header", LayerHeader), 
        # Contains a single image, never with any stereo view.
        ("ColorTexture", POINTER(SwapTextureSet)), 
        # Specifies the ColorTexture sub-rect UV coordinates.
        ("Viewport", Recti), 
        # Position and orientation of the center of the quad. Position is specified in meters.
        ("QuadPoseCenter", Posef), 
        # Width and height (respectively) of the quad in meters.
        ("QuadSize", Vector2f), 
    ]

    def __repr__(self):
        return "ovr.LayerQuad(%s, %s, %s, %s, %s)" % (self.Header, self.ColorTexture, self.Viewport, self.QuadPoseCenter, self.QuadSize)


# Translated from header file OVR_CAPI_0_8_0.h line 1501
class LayerDirect(Structure):
    """
    Describes a layer which is copied to the HMD as-is. Neither distortion, time warp,
    nor vignetting is applied to ColorTexture before it's copied to the HMD. The application
    can, however implement these kinds of effects itself before submitting the layer.
    This layer can be used for application-based distortion rendering and can also be
    used for implementing a debug HUD that's viewed on the mirror texture.
    
    \see ovrSwapTextureSet, ovr_SubmitFrame
    """
    _pack_ = OVR_PTR_SIZE
    _fields_ = [
        # Header.Type must be ovrLayerType_EyeDirect.
        ("Header", LayerHeader), 
        # ovrSwapTextureSets for the left and right eye respectively.
        # The second one of which can be NULL for cases described above.
        ("ColorTexture", POINTER(SwapTextureSet) * Eye_Count), 
        # Specifies the ColorTexture sub-rect UV coordinates.
        # Both Viewport[0] and Viewport[1] must be valid.
        ("Viewport", Recti * Eye_Count), 
    ]

    def __repr__(self):
        return "ovr.LayerDirect(%s, %s, %s)" % (self.Header, self.ColorTexture, self.Viewport)


# Translated from header file OVR_CAPI_0_8_0.h line 1525
class Layer_Union(Union):
    """
    Union that combines ovrLayer types in a way that allows them
    to be used in a polymorphic way.
    """
    _fields_ = [
        ("Header", LayerHeader), 
        ("EyeFov", LayerEyeFov), 
        ("EyeFovDepth", LayerEyeFovDepth), 
        ("Quad", LayerQuad), 
        ("Direct", LayerDirect), 
    ]

    def __repr__(self):
        return "ovr.Layer_Union(%s, %s, %s, %s, %s)" % (self.Header, self.EyeFov, self.EyeFovDepth, self.Quad, self.Direct)


# Translated from header file OVR_CAPI_0_8_0.h line 1557
libovr.ovr_DestroySwapTextureSet.restype = None
libovr.ovr_DestroySwapTextureSet.argtypes = [Session, POINTER(SwapTextureSet)]
def destroySwapTextureSet(session, textureSet):
    """
    Destroys an ovrSwapTextureSet and frees all the resources associated with it.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] textureSet Specifies the ovrSwapTextureSet to destroy. If it is NULL then this function has no effect.
    
    \see ovr_CreateSwapTextureSetD3D11, ovr_CreateSwapTextureSetGL
    """
    result = libovr.ovr_DestroySwapTextureSet(session, byref(textureSet))
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1567
libovr.ovr_DestroyMirrorTexture.restype = None
libovr.ovr_DestroyMirrorTexture.argtypes = [Session, POINTER(Texture)]
def destroyMirrorTexture(session, mirrorTexture):
    """
    Destroys a mirror texture previously created by one of the mirror texture creation functions.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] mirrorTexture Specifies the ovrTexture to destroy. If it is NULL then this function has no effect.
    
    \see ovr_CreateMirrorTextureD3D11, ovr_CreateMirrorTextureGL
    """
    result = libovr.ovr_DestroyMirrorTexture(session, byref(mirrorTexture))
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1577
libovr.ovr_GetFovTextureSize.restype = Sizei
libovr.ovr_GetFovTextureSize.argtypes = [Session, EyeType, FovPort, c_float]
def getFovTextureSize(session, eye, fov, pixelsPerDisplayPixel):
    """
    Calculates the recommended viewport size for rendering a given eye within the HMD
    with a given FOV cone.
    
    Higher FOV will generally require larger textures to maintain quality.
    Apps packing multiple eye views together on the same texture should ensure there are
    at least 8 pixels of padding between them to prevent texture filtering and chromatic
    aberration causing images to leak between the two eye views.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] eye Specifies which eye (left or right) to calculate for.
    \param[in] fov Specifies the ovrFovPort to use.
    \param[in] pixelsPerDisplayPixel Specifies the ratio of the number of render target pixels
               to display pixels at the center of distortion. 1.0 is the default value. Lower
               values can improve performance, higher values give improved quality.
    \return Returns the texture width and height size.
    """
    result = libovr.ovr_GetFovTextureSize(session, eye, fov, pixelsPerDisplayPixel)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1596
libovr.ovr_GetRenderDesc.restype = EyeRenderDesc
libovr.ovr_GetRenderDesc.argtypes = [Session, EyeType, FovPort]
def getRenderDesc(session, eyeType, fov):
    """
    Computes the distortion viewport, view adjust, and other rendering parameters for
    the specified eye.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] eyeType Specifies which eye (left or right) for which to perform calculations.
    \param[in] fov Specifies the ovrFovPort to use.
    \return Returns the computed ovrEyeRenderDesc for the given eyeType and field of view.
    
    \see ovrEyeRenderDesc
    """
    result = libovr.ovr_GetRenderDesc(session, eyeType, fov)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1609
libovr.ovr_SubmitFrame.restype = Result
libovr.ovr_SubmitFrame.argtypes = [Session, c_longlong, POINTER(ViewScaleDesc), POINTER(POINTER(LayerHeader)), c_uint]
def submitFrame(session, frameIndex, viewScaleDesc, layerPtrList, layerCount):
    """
    Submits layers for distortion and display.
    
    ovr_SubmitFrame triggers distortion and processing which might happen asynchronously.
    The function will return when there is room in the submission queue and surfaces
    are available. Distortion might or might not have completed.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    
    \param[in] frameIndex Specifies the targeted application frame index, or 0 to refer to one frame
           after the last time ovr_SubmitFrame was called.
    
    \param[in] viewScaleDesc Provides additional information needed only if layerPtrList contains
           a ovrLayerType_Quad. If NULL, a default version is used based on the current configuration and a 1.0 world scale.
    
    \param[in] layerPtrList Specifies a list of ovrLayer pointers, which can include NULL entries to
           indicate that any previously shown layer at that index is to not be displayed.
           Each layer header must be a part of a layer structure such as ovrLayerEyeFov or ovrLayerQuad,
           with Header.Type identifying its type. A NULL layerPtrList entry in the array indicates the
            absence of the given layer.
    
    \param[in] layerCount Indicates the number of valid elements in layerPtrList. The maximum
           supported layerCount is not currently specified, but may be specified in a future version.
    
    - Layers are drawn in the order they are specified in the array, regardless of the layer type.
    
    - Layers are not remembered between successive calls to ovr_SubmitFrame. A layer must be
      specified in every call to ovr_SubmitFrame or it won't be displayed.
    
    - If a layerPtrList entry that was specified in a previous call to ovr_SubmitFrame is
      passed as NULL or is of type ovrLayerType_Disabled, that layer is no longer displayed.
    
    - A layerPtrList entry can be of any layer type and multiple entries of the same layer type
      are allowed. No layerPtrList entry may be duplicated (i.e. the same pointer as an earlier entry).
    
    <b>Example code</b>
        \code{.cpp}
            ovrLayerEyeFov  layer0;
            ovrLayerQuad    layer1;
              ...
            ovrLayerHeader* layers[2] = { &layer0.Header, &layer1.Header };
            ovrResult result = ovr_SubmitFrame(hmd, frameIndex, nullptr, layers, 2);
        \endcode
    
    \return Returns an ovrResult for which OVR_SUCCESS(result) is false upon error and true
            upon one of the possible success values:
        - ovrSuccess: rendering completed successfully.
        - ovrSuccess_NotVisible: rendering completed successfully but was not displayed on the HMD,
          usually because another application currently has ownership of the HMD. Applications receiving
          this result should stop rendering new content, but continue to call ovr_SubmitFrame periodically
          until it returns a value other than ovrSuccess_NotVisible.
        - ovrError_DisplayLost: The session has become invalid (such as due to a device removal)
          and the shared resources need to be released (ovr_DestroySwapTextureSet), the session needs to
          destroyed (ovr_Destroy) and recreated (ovr_Create), and new resources need to be created
          (ovr_CreateSwapTextureSetXXX). The application's existing private graphics resources do not
          need to be recreated unless the new ovr_Create call returns a different GraphicsLuid.
    
    \see ovr_GetPredictedDisplayTime, ovrViewScaleDesc, ovrLayerHeader
    """
    layerPtrList = (POINTER(LayerHeader) * len(layerPtrList))(*[ctypes.pointer(i) for i in layerPtrList])
    result = libovr.ovr_SubmitFrame(session, frameIndex, byref(viewScaleDesc), byref(layerPtrList), layerCount)
    if FAILURE(result):
        raise Exception("Call to function submitFrame failed")    
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1680
libovr.ovr_GetPredictedDisplayTime.restype = c_double
libovr.ovr_GetPredictedDisplayTime.argtypes = [Session, c_longlong]
def getPredictedDisplayTime(session, frameIndex):
    """
    Gets the time of the specified frame midpoint.
    
    Predicts the time at which the given frame will be displayed. The predicted time 
    is the middle of the time period during which the corresponding eye images will 
    be displayed. 
    
    The application should increment frameIndex for each successively targeted frame,
    and pass that index to any relevent OVR functions that need to apply to the frame
    identified by that index.
    
    This function is thread-safe and allows for multiple application threads to target
    their processing to the same displayed frame.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] frameIndex Identifies the frame the caller wishes to target.
               A value of zero returns the next frame index.
    \return Returns the absolute frame midpoint time for the given frameIndex.
    \see ovr_GetTimeInSeconds
    """
    result = libovr.ovr_GetPredictedDisplayTime(session, frameIndex)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1702
libovr.ovr_GetTimeInSeconds.restype = c_double
def getTimeInSeconds():
    """
    Returns global, absolute high-resolution time in seconds.
    
    The time frame of reference for this function is not specified and should not be
    depended upon.
    
    \return Returns seconds as a floating point value.
    \see ovrPoseStatef, ovrSensorData, ovrFrameTiming
    """
    result = libovr.ovr_GetTimeInSeconds()
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1713
# Performance HUD enables the HMD user to see information critical to
# the real-time operation of the VR application such as latency timing,
# and CPU & GPU performance metrics
#
#     App can toggle performance HUD modes as such:
#     \code{.cpp}
#         ovrPerfHudMode PerfHudMode = ovrPerfHud_LatencyTiming;
#         ovr_SetInt(Hmd, OVR_PERF_HUD_MODE, (int)PerfHudMode);
#     \endcode
#
PerfHudMode = ENUM_TYPE
PerfHud_Off                = 0  #< Turns off the performance HUD
PerfHud_LatencyTiming      = 1  #< Shows latency related timing info
PerfHud_RenderTiming       = 2  #< Shows CPU & GPU timing info
PerfHud_PerfHeadroom       = 3  #< Shows available performance headroom in a "consumer-friendly" way
PerfHud_VersionInfo        = 4  #< Shows SDK Version Info
PerfHud_Count = PerfHud_VersionInfo + 1                   #< \internal Count of enumerated elements.


# Translated from header file OVR_CAPI_0_8_0.h line 1734
# Layer HUD enables the HMD user to see information about a layer
#
#     App can toggle layer HUD modes as such:
#     \code{.cpp}
#         ovrLayerHudMode LayerHudMode = ovrLayerHud_Info;
#         ovr_SetInt(Hmd, OVR_LAYER_HUD_MODE, (int)LayerHudMode);
#     \endcode
#
LayerHudMode = ENUM_TYPE
LayerHud_Off = 0 #< Turns off the layer HUD
LayerHud_Info = 1 #< Shows info about a specific layer


# Translated from header file OVR_CAPI_0_8_0.h line 1751
# Debug HUD is provided to help developers gauge and debug the fidelity of their app's
# stereo rendering characteristics. Using the provided quad and crosshair guides, 
# the developer can verify various aspects such as VR tracking units (e.g. meters),
# stereo camera-parallax properties (e.g. making sure objects at infinity are rendered
# with the proper separation), measuring VR geometry sizes and distances and more.
#
#     App can toggle the debug HUD modes as such:
#     \code{.cpp}
#         ovrDebugHudStereoMode DebugHudMode = ovrDebugHudStereo_QuadWithCrosshair;
#         ovr_SetInt(Hmd, OVR_DEBUG_HUD_STEREO_MODE, (int)DebugHudMode);
#     \endcode
#
# The app can modify the visual properties of the stereo guide (i.e. quad, crosshair)
# using the ovr_SetFloatArray function. For a list of tweakable properties,
# see the OVR_DEBUG_HUD_STEREO_GUIDE_* keys in the OVR_CAPI_Keys.h header file.
DebugHudStereoMode = ENUM_TYPE
DebugHudStereo_Off                 = 0  #< Turns off the Stereo Debug HUD
DebugHudStereo_Quad                = 1  #< Renders Quad in world for Stereo Debugging
DebugHudStereo_QuadWithCrosshair   = 2  #< Renders Quad+crosshair in world for Stereo Debugging
DebugHudStereo_CrosshairAtInfinity = 3  #< Renders screen-space crosshair at infinity for Stereo Debugging
DebugHudStereo_Count = DebugHudStereo_CrosshairAtInfinity + 1                    #< \internal Count of enumerated elements


# Translated from header file OVR_CAPI_0_8_0.h line 1780
libovr.ovr_ResetBackOfHeadTracking.restype = None
libovr.ovr_ResetBackOfHeadTracking.argtypes = [Session]
def resetBackOfHeadTracking(session):
    """
    Should be called when the headset is placed on a new user.
    Previously named ovrHmd_ResetOnlyBackOfHeadTrackingForConnectConf.
    
    This may be removed in a future SDK version.
    """
    result = libovr.ovr_ResetBackOfHeadTracking(session)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1788
libovr.ovr_ResetMulticameraTracking.restype = None
libovr.ovr_ResetMulticameraTracking.argtypes = [Session]
def resetMulticameraTracking(session):
    """
    Should be called when a tracking camera is moved.
    
    This may be removed in a future SDK version.
    """
    result = libovr.ovr_ResetMulticameraTracking(session)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1804
libovr.ovr_GetBool.restype = Bool
libovr.ovr_GetBool.argtypes = [Session, c_char_p, Bool]
def getBool(session, propertyName, defaultVal):
    """
    Reads a boolean property.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] propertyName The name of the property, which needs to be valid for only the call.
    \param[in] defaultVal specifes the value to return if the property couldn't be read.
    \return Returns the property interpreted as a boolean value. Returns defaultVal if
            the property doesn't exist.
    """
    result = libovr.ovr_GetBool(session, propertyName, toOvrBool(defaultVal))
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1813
libovr.ovr_SetBool.restype = Bool
libovr.ovr_SetBool.argtypes = [Session, c_char_p, Bool]
def setBool(session, propertyName, value):
    """
    Writes or creates a boolean property.
    If the property wasn't previously a boolean property, it is changed to a boolean property.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] propertyName The name of the property, which needs to be valid only for the call.
    \param[in] value The value to write.
    \return Returns true if successful, otherwise false. A false result should only occur if the property
            name is empty or if the property is read-only.
    """
    result = libovr.ovr_SetBool(session, propertyName, toOvrBool(value))
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1824
libovr.ovr_GetInt.restype = c_int
libovr.ovr_GetInt.argtypes = [Session, c_char_p, c_int]
def getInt(session, propertyName, defaultVal):
    """
    Reads an integer property.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] propertyName The name of the property, which needs to be valid only for the call.
    \param[in] defaultVal Specifes the value to return if the property couldn't be read.
    \return Returns the property interpreted as an integer value. Returns defaultVal if
            the property doesn't exist.
    """
    result = libovr.ovr_GetInt(session, propertyName, defaultVal)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1833
libovr.ovr_SetInt.restype = Bool
libovr.ovr_SetInt.argtypes = [Session, c_char_p, c_int]
def setInt(session, propertyName, value):
    """
    Writes or creates an integer property.
    
    If the property wasn't previously a boolean property, it is changed to an integer property.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] propertyName The name of the property, which needs to be valid only for the call.
    \param[in] value The value to write.
    \return Returns true if successful, otherwise false. A false result should only occur if the property
            name is empty or if the property is read-only.
    """
    result = libovr.ovr_SetInt(session, propertyName, value)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1845
libovr.ovr_GetFloat.restype = c_float
libovr.ovr_GetFloat.argtypes = [Session, c_char_p, c_float]
def getFloat(session, propertyName, defaultVal):
    """
    Reads a float property.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] propertyName The name of the property, which needs to be valid only for the call.
    \param[in] defaultVal specifes the value to return if the property couldn't be read.
    \return Returns the property interpreted as an float value. Returns defaultVal if
            the property doesn't exist.
    """
    result = libovr.ovr_GetFloat(session, propertyName, defaultVal)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1854
libovr.ovr_SetFloat.restype = Bool
libovr.ovr_SetFloat.argtypes = [Session, c_char_p, c_float]
def setFloat(session, propertyName, value):
    """
    Writes or creates a float property.
    If the property wasn't previously a float property, it's changed to a float property.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] propertyName The name of the property, which needs to be valid only for the call.
    \param[in] value The value to write.
    \return Returns true if successful, otherwise false. A false result should only occur if the property
            name is empty or if the property is read-only.
    """
    result = libovr.ovr_SetFloat(session, propertyName, value)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1865
libovr.ovr_GetFloatArray.restype = c_uint
libovr.ovr_GetFloatArray.argtypes = [Session, c_char_p, POINTER(c_float), c_uint]
def getFloatArray(session, propertyName, values, valuesCapacity):
    """
    Reads a float array property.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] propertyName The name of the property, which needs to be valid only for the call.
    \param[in] values An array of float to write to.
    \param[in] valuesCapacity Specifies the maximum number of elements to write to the values array.
    \return Returns the number of elements read, or 0 if property doesn't exist or is empty.
    """
    result = libovr.ovr_GetFloatArray(session, propertyName, byref(values), valuesCapacity)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1875
libovr.ovr_SetFloatArray.restype = Bool
libovr.ovr_SetFloatArray.argtypes = [Session, c_char_p, POINTER(c_float), c_uint]
def setFloatArray(session, propertyName, values, valuesSize):
    """
    Writes or creates a float array property.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] propertyName The name of the property, which needs to be valid only for the call.
    \param[in] values An array of float to write from.
    \param[in] valuesSize Specifies the number of elements to write.
    \return Returns true if successful, otherwise false. A false result should only occur if the property
            name is empty or if the property is read-only.
    """
    result = libovr.ovr_SetFloatArray(session, propertyName, byref(values), valuesSize)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1887
libovr.ovr_GetString.restype = c_char_p
libovr.ovr_GetString.argtypes = [Session, c_char_p, c_char_p]
def getString(session, propertyName, defaultVal):
    """
    Reads a string property.
    Strings are UTF8-encoded and null-terminated.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] propertyName The name of the property, which needs to be valid only for the call.
    \param[in] defaultVal Specifes the value to return if the property couldn't be read.
    \return Returns the string property if it exists. Otherwise returns defaultVal, which can be specified as NULL.
            The return memory is guaranteed to be valid until next call to ovr_GetString or
            until the HMD is destroyed, whichever occurs first.
    """
    result = libovr.ovr_GetString(session, propertyName, defaultVal)
    return result


# Translated from header file OVR_CAPI_0_8_0.h line 1899
libovr.ovr_SetString.restype = Bool
libovr.ovr_SetString.argtypes = [Session, c_char_p, c_char_p]
def setString(session, propertyName, value):
    """
    Writes or creates a string property.
    Strings are UTF8-encoded and null-terminated.
    
    \param[in] session Specifies an ovrSession previously returned by ovr_Create.
    \param[in] propertyName The name of the property, which needs to be valid only for the call.
    \param[in] value The string property, which only needs to be valid for the duration of the call.
    \return Returns true if successful, otherwise false. A false result should only occur if the property
            name is empty or if the property is read-only.
    """
    result = libovr.ovr_SetString(session, propertyName, value)
    return result


### END Declarations from C header file OVR_CAPI_0_8_0.h ###


### BEGIN Declarations from C header file OVR_CAPI_GL.h ###


# Translated from header file OVR_CAPI_GL.h line 10
# We avoid gl.h #includes here which interferes with some users' use of alternatives and typedef GLuint manually.
GLuint = c_uint 


# Translated from header file OVR_CAPI_GL.h line 19
class GLTextureData(Structure):
    "Used to pass GL eye texture data to ovr_EndFrame."
    _fields_ = [
        ("Header", TextureHeader),     #< General device settings.
        ("TexId", GLuint),      #< The OpenGL name for this texture.
    ]

    def __repr__(self):
        return "ovr.GLTextureData(%s, %s)" % (self.Header, self.TexId)


# Translated from header file OVR_CAPI_GL.h line 29
class GLTexture(Union):
    "Contains OpenGL-specific texture information."
    _fields_ = [
        ("Texture", Texture),    #< General device settings.
        ("OGL", GLTextureData),        #< OpenGL-specific settings.
    ]

    def __repr__(self):
        return "ovr.GLTexture(%s, %s)" % (self.Texture, self.OGL)


# Translated from header file OVR_CAPI_GL.h line 43
libovr.ovr_CreateSwapTextureSetGL.restype = Result
libovr.ovr_CreateSwapTextureSetGL.argtypes = [Session, GLuint, c_int, c_int, POINTER(POINTER(SwapTextureSet))]
def createSwapTextureSetGL(session, format_, width, height):
    """
    Creates a Texture Set suitable for use with OpenGL.
    
    Multiple calls to ovr_CreateSwapTextureSetD3D11 for the same ovrHmd are supported, but applications
    cannot rely on switching between ovrSwapTextureSets at runtime without a performance penalty.
    
    \param[in]  session Specifies an ovrSession previously returned by ovr_Create.
    \param[in]  format Specifies the texture format.
    \param[in]  width Specifies the requested texture width.
    \param[in]  height Specifies the requested texture height.
    \param[out] outTextureSet Specifies the created ovrSwapTextureSet, which will be valid upon a successful return value, else it will be NULL.
                This texture set must be eventually destroyed via ovr_DestroySwapTextureSet before destroying the HMD with ovr_Destroy.
    
    \return Returns an ovrResult indicating success or failure. In the case of failure, use 
            ovr_GetLastErrorInfo to get more information.
    
    \note The \a format provided should be thought of as the format the distortion compositor will use when reading the contents of the
    texture. To that end, it is highly recommended that the application requests swap-texture-set formats that are in sRGB-space (e.g. GL_SRGB_ALPHA8)
    as the distortion compositor does sRGB-correct rendering. Furthermore, the app should then make sure "glEnable(GL_FRAMEBUFFER_SRGB);"
    is called before rendering into these textures. Even though it is not recommended, if the application would like to treat the
    texture as a linear format and do linear-to-gamma conversion in GLSL, then the application can avoid calling "glEnable(GL_FRAMEBUFFER_SRGB);",
    but should still pass in GL_SRGB_ALPHA8 (not GL_RGBA) for the \a format. Failure to do so will cause the distortion compositor
    to apply incorrect gamma conversions leading to gamma-curve artifacts.
    
    \see ovr_DestroySwapTextureSet
    """
    outTextureSet = POINTER(SwapTextureSet)()
    result = libovr.ovr_CreateSwapTextureSetGL(session, format_, width, height, byref(outTextureSet))
    if FAILURE(result):
        raise Exception("Call to function createSwapTextureSetGL failed")    
    return outTextureSet


# Translated from header file OVR_CAPI_GL.h line 73
libovr.ovr_CreateMirrorTextureGL.restype = Result
libovr.ovr_CreateMirrorTextureGL.argtypes = [Session, GLuint, c_int, c_int, POINTER(POINTER(Texture))]
def createMirrorTextureGL(session, format_, width, height):
    """
    Creates a Mirror Texture which is auto-refreshed to mirror Rift contents produced by this application.
    
    A second call to ovr_CreateMirrorTextureGL for a given ovrHmd before destroying the first one
    is not supported and will result in an error return.
    
    \param[in]  session Specifies an ovrSession previously returned by ovr_Create.
    \param[in]  format Specifies the texture format.
    \param[in]  width Specifies the requested texture width.
    \param[in]  height Specifies the requested texture height.
    \param[out] outMirrorTexture Specifies the created ovrSwapTexture, which will be valid upon a successful return value, else it will be NULL.
                This texture must be eventually destroyed via ovr_DestroyMirrorTexture before destroying the HMD with ovr_Destroy.
    
    \return Returns an ovrResult indicating success or failure. In the case of failure, use 
            ovr_GetLastErrorInfo to get more information.
    
    \note The \a format provided should be thought of as the format the distortion compositor will use when writing into the mirror
    texture. It is highly recommended that mirror textures are requested as GL_SRGB_ALPHA8 because the distortion compositor
    does sRGB-correct rendering. If the application requests a non-sRGB format (e.g. GL_RGBA) as the mirror texture,
    then the application might have to apply a manual linear-to-gamma conversion when reading from the mirror texture.
    Failure to do so can result in incorrect gamma conversions leading to gamma-curve artifacts and color banding.
    
    \see ovr_DestroyMirrorTexture
    """
    outMirrorTexture = POINTER(Texture)()
    result = libovr.ovr_CreateMirrorTextureGL(session, format_, width, height, byref(outMirrorTexture))
    if FAILURE(result):
        raise Exception("Call to function createMirrorTextureGL failed")    
    return outMirrorTexture


### END Declarations from C header file OVR_CAPI_GL.h ###


### BEGIN Declarations from C header file OVR_CAPI_Util.h ###


# Translated from header file OVR_CAPI_Util.h line 17
# Enumerates modifications to the projection matrix based on the application's needs.
#
# \see ovrMatrix4f_Projection
#
ProjectionModifier = ENUM_TYPE
# Use for generating a default projection matrix that is:
# * Left-handed.
# * Near depth values stored in the depth buffer are smaller than far depth values.
# * Both near and far are explicitly defined.
# * With a clipping range that is (0 to w).
Projection_None = 0x00
# Enable if using right-handed transformations in your application.
Projection_RightHanded = 0x01
# After the projection transform is applied, far values stored in the depth buffer will be less than closer depth values.
# NOTE: Enable only if the application is using a floating-point depth buffer for proper precision.
Projection_FarLessThanNear = 0x02
# When this flag is used, the zfar value pushed into ovrMatrix4f_Projection() will be ignored
# NOTE: Enable only if ovrProjection_FarLessThanNear is also enabled where the far clipping plane will be pushed to infinity.
Projection_FarClipAtInfinity = 0x04
# Enable if the application is rendering with OpenGL and expects a projection matrix with a clipping range of (-w to w).
# Ignore this flag if your application already handles the conversion from D3D range (0 to w) to OpenGL.
Projection_ClipRangeOpenGL = 0x08


# Translated from header file OVR_CAPI_Util.h line 47
class DetectResult(Structure):
    """
    Return values for ovr_Detect.
    
    \see ovr_Detect
    """
    _pack_ = 8
    _fields_ = [
        # Is ovrFalse when the Oculus Service is not running.
        #   This means that the Oculus Service is either uninstalled or stopped.
        #   IsOculusHMDConnected will be ovrFalse in this case.
        # Is ovrTrue when the Oculus Service is running.
        #   This means that the Oculus Service is installed and running.
        #   IsOculusHMDConnected will reflect the state of the HMD.
        ("IsOculusServiceRunning", Bool), 
        # Is ovrFalse when an Oculus HMD is not detected.
        #   If the Oculus Service is not running, this will be ovrFalse.
        # Is ovrTrue when an Oculus HMD is detected.
        #   This implies that the Oculus Service is also installed and running.
        ("IsOculusHMDConnected", Bool), 
        ("pad0", c_char * 6),  #< \internal struct padding
    ]

    def __repr__(self):
        return "ovr.DetectResult(%s, %s)" % (self.IsOculusServiceRunning, self.IsOculusHMDConnected)


# Translated from header file OVR_CAPI_Util.h line 74
libovr.ovr_Detect.restype = DetectResult
libovr.ovr_Detect.argtypes = [c_int]
def detect(timeoutMsec):
    """
    Detects Oculus Runtime and Device Status
    
    Checks for Oculus Runtime and Oculus HMD device status without loading the LibOVRRT
    shared library.  This may be called before ovr_Initialize() to help decide whether or
    not to initialize LibOVR.
    
    \param[in] timeoutMsec Specifies a timeout to wait for HMD to be attached or 0 to poll.
    
    \return Returns an ovrDetectResult object indicating the result of detection.
    
    \see ovrDetectResult
    """
    result = libovr.ovr_Detect(timeoutMsec)
    return result


# Translated from header file OVR_CAPI_Util.h line 95
libovr.ovrMatrix4f_Projection.restype = Matrix4f
libovr.ovrMatrix4f_Projection.argtypes = [FovPort, c_float, c_float, c_uint]
def matrix4f_Projection(fov, znear, zfar, projectionModFlags):
    """
    Used to generate projection from ovrEyeDesc::Fov.
    
    \param[in] fov Specifies the ovrFovPort to use.
    \param[in] znear Distance to near Z limit.
    \param[in] zfar Distance to far Z limit.
    \param[in] projectionModFlags A combination of the ovrProjectionModifier flags.
    
    \return Returns the calculated projection matrix.
    
    \see ovrProjectionModifier
    """
    result = libovr.ovrMatrix4f_Projection(fov, znear, zfar, projectionModFlags)
    return result


# Translated from header file OVR_CAPI_Util.h line 109
libovr.ovrTimewarpProjectionDesc_FromProjection.restype = TimewarpProjectionDesc
libovr.ovrTimewarpProjectionDesc_FromProjection.argtypes = [Matrix4f, c_uint]
def timewarpProjectionDesc_FromProjection(projection, projectionModFlags):
    """
    Extracts the required data from the result of ovrMatrix4f_Projection.
    
    \param[in] projection Specifies the project matrix from which to extract ovrTimewarpProjectionDesc.
    \param[in] projectionModFlags A combination of the ovrProjectionModifier flags.
    \return Returns the extracted ovrTimewarpProjectionDesc.
    \see ovrTimewarpProjectionDesc
    """
    result = libovr.ovrTimewarpProjectionDesc_FromProjection(projection, projectionModFlags)
    return result


# Translated from header file OVR_CAPI_Util.h line 119
libovr.ovrMatrix4f_OrthoSubProjection.restype = Matrix4f
libovr.ovrMatrix4f_OrthoSubProjection.argtypes = [Matrix4f, Vector2f, c_float, c_float]
def matrix4f_OrthoSubProjection(projection, orthoScale, orthoDistance, hmdToEyeViewOffsetX):
    """
    Generates an orthographic sub-projection.
    
    Used for 2D rendering, Y is down.
    
    \param[in] projection The perspective matrix that the orthographic matrix is derived from.
    \param[in] orthoScale Equal to 1.0f / pixelsPerTanAngleAtCenter.
    \param[in] orthoDistance Equal to the distance from the camera in meters, such as 0.8m.
    \param[in] hmdToEyeViewOffsetX Specifies the offset of the eye from the center.
    
    \return Returns the calculated projection matrix.
    """
    result = libovr.ovrMatrix4f_OrthoSubProjection(projection, orthoScale, orthoDistance, hmdToEyeViewOffsetX)
    return result


# Translated from header file OVR_CAPI_Util.h line 135
libovr.ovr_CalcEyePoses.restype = None
libovr.ovr_CalcEyePoses.argtypes = [Posef, Vector3f * 2, Posef * 2]
def calcEyePoses(headPose, hmdToEyeViewOffset, outEyePoses):
    """
    Computes offset eye poses based on headPose returned by ovrTrackingState.
    
    \param[in] headPose Indicates the HMD position and orientation to use for the calculation.
    \param[in] hmdToEyeViewOffset Can be ovrEyeRenderDesc.HmdToEyeViewOffset returned from 
               ovr_GetRenderDesc. For monoscopic rendering, use a vector that is the average 
               of the two vectors for both eyes.
    \param[out] outEyePoses If outEyePoses are used for rendering, they should be passed to 
                ovr_SubmitFrame in ovrLayerEyeFov::RenderPose or ovrLayerEyeFovDepth::RenderPose.
    """
    result = libovr.ovr_CalcEyePoses(headPose, hmdToEyeViewOffset, outEyePoses)
    return result


# Translated from header file OVR_CAPI_Util.h line 149
libovr.ovr_GetEyePoses.restype = None
libovr.ovr_GetEyePoses.argtypes = [Session, c_longlong, Bool, Vector3f * 2, Posef * 2, POINTER(TrackingState)]
def getEyePoses(session, frameIndex, latencyMarker, hmdToEyeViewOffset, outEyePoses):
    """
    Returns the predicted head pose in outHmdTrackingState and offset eye poses in outEyePoses. 
    
    This is a thread-safe function where caller should increment frameIndex with every frame
    and pass that index where applicable to functions called on the rendering thread.
    Assuming outEyePoses are used for rendering, it should be passed as a part of ovrLayerEyeFov.
    The caller does not need to worry about applying HmdToEyeViewOffset to the returned outEyePoses variables.
    
    \param[in]  hmd Specifies an ovrHmd previously returned by ovr_Create.
    \param[in]  frameIndex Specifies the targeted frame index, or 0 to refer to one frame after 
                the last time ovr_SubmitFrame was called.
    \param[in]  hmdToEyeViewOffset Can be ovrEyeRenderDesc.HmdToEyeViewOffset returned from 
                ovr_GetRenderDesc. For monoscopic rendering, use a vector that is the average 
                of the two vectors for both eyes.
    \param[in]  latencyMarker Specifies that this call is the point in time where
                the "App-to-Mid-Photon" latency timer starts from. If a given ovrLayer
                provides "SensorSampleTimestamp", that will override the value stored here.
    \param[out] outEyePoses The predicted eye poses.
    \param[out] outHmdTrackingState The predicted ovrTrackingState. May be NULL, in which case it is ignored.
    """
    outHmdTrackingState = TrackingState()
    result = libovr.ovr_GetEyePoses(session, frameIndex, toOvrBool(latencyMarker), hmdToEyeViewOffset, outEyePoses, byref(outHmdTrackingState))
    return outHmdTrackingState


### END Declarations from C header file OVR_CAPI_Util.h ###


# Run test program
if __name__ == "__main__":
    # Transcribed from initial example at 
    # https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-sensor/
    initialize(None)
    hmd, luid = create()
    desc = getHmdDesc(hmd)
    print(desc.Resolution)
    print(desc.ProductName)
    # Start the sensor which provides the Rift's pose and motion.
    configureTracking(hmd, 
        TrackingCap_Orientation | # requested capabilities
        TrackingCap_MagYawCorrection |
        TrackingCap_Position, 
        0) # required capabilities
    # Query the HMD for the current tracking state.
    ts  = getTrackingState(hmd, getTimeInSeconds())
    if ts.StatusFlags & (Status_OrientationTracked | Status_PositionTracked):
        pose = ts.HeadPose
        print(pose.ThePose)
        # TODO:

    destroy(hmd)
    shutdown()

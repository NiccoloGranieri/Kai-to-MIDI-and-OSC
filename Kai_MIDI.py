"""
Example program for receiving gesture events and accelerometer readings from Kai
"""

import os
import time
import configparser
import rtmidi

from KaiSDK.WebSocketModule import WebSocketModule
from KaiSDK.DataTypes import KaiCapabilities
import KaiSDK.Events as Events

midiout = rtmidi.MidiOut()

available_ports = midiout.get_ports()
if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")

PYR_Range = (360 - 0)  
PYR_MIDI = (127 - 0)

# Event listener functions
def gestureEvent(ev):
    pass
    # gestureString = ev.gesture
    # if (str(gestureString) == "Gesture.swipeUp"):
    #     print(1)
    #     cc_gestureOne_On = [0xB0, 0, 127]
    #     cc_gestureOne_Off = [0xB0, 0, 0]
    #     midiout.send_message(cc_gestureOne_On)
    #     time.sleep(1.0)
    #     midiout.send_message(cc_gestureOne_Off)
    # elif (str(gestureString) == "Gesture.swipeDown"):
    #     print(2)
    #     cc_gestureTwo_On = [0xB0, 1, 127]
    #     cc_gestureTwo_Off = [0xB0, 1, 0]
    #     midiout.send_message(cc_gestureTwo_On)
    #     time.sleep(1.0)
    #     midiout.send_message(cc_gestureTwo_Off)
    # elif (str(gestureString) == "Gesture.swipeLeft"):
    #     print(3)
    #     cc_gestureThree_On = [0xB0, 2, 127]
    #     cc_gestureThree_Off = [0xB0, 2, 0]
    #     midiout.send_message(cc_gestureThree_On)
    #     time.sleep(1.0)
    #     midiout.send_message(cc_gestureThree_Off)
    # elif (str(gestureString) == "Gesture.swipeRight"):
    #     print(4)
    #     cc_gestureFour_On = [0xB0, 3, 127]
    #     cc_gestureFour_Off = [0xB0, 3, 0]
    #     midiout.send_message(cc_gestureFour_On)
    #     time.sleep(1.0)
    #     midiout.send_message(cc_gestureFour_Off)
    
def pyrEv(ev):
    pos_Pitch = ev.pitch + 179
    pos_Yaw = ev.yaw + 179
    pos_Roll = ev.roll + 179

    MIDI_Pitch = (((pos_Pitch - 0) * PYR_MIDI) / PYR_Range) + 0
    MIDI_Yaw = (((pos_Yaw - 0) * PYR_MIDI) / PYR_Range) + 0
    MIDI_Roll = (((pos_Roll - 0) * PYR_MIDI) / PYR_Range) + 0

    cc_Pitch = [0xB0, 4, MIDI_Pitch]
    midiout.send_message(cc_Pitch)
    cc_Yaw = [0xB0, 5, MIDI_Yaw]
    midiout.send_message(cc_Yaw)
    cc_Roll = [0xB0, 6, MIDI_Roll]
    midiout.send_message(cc_Roll)

def quatEv(ev):
    MIDI_QuatW = int((ev.quaternion.w + 1) * 63)
    MIDI_QuatX = int((ev.quaternion.x + 1) * 63)
    MIDI_QuatY = int((ev.quaternion.y + 1) * 63)
    MIDI_QuatZ = int((ev.quaternion.z + 1) * 63)

    cc_QuatW = [0xB0, 7, MIDI_QuatW]
    midiout.send_message(cc_QuatW)
    cc_QuatX = [0xB0, 8, MIDI_QuatX]
    midiout.send_message(cc_QuatX)
    cc_QuatY = [0xB0, 9, MIDI_QuatY]
    midiout.send_message(cc_QuatY)
    cc_QuatZ = [0xB0, 10, MIDI_QuatZ]
    midiout.send_message(cc_QuatZ)

def fingersEv(ev):
    MIDI_LittleF = ev.littleFinger * 127
    MIDI_RingF = ev.ringFinger * 127
    MIDI_MiddleF = ev.middleFinger * 127
    MIDI_IndexF = ev.indexFinger * 127

    cc_LittleF = [0xB0, 11, MIDI_LittleF]
    midiout.send_message(cc_LittleF)
    cc_RingF = [0xB0, 12, MIDI_RingF]
    midiout.send_message(cc_RingF)
    cc_MiddleF = [0xB0, 13, MIDI_MiddleF]
    midiout.send_message(cc_MiddleF)
    cc_IndexF = [0xB0, 14, MIDI_IndexF]
    midiout.send_message(cc_IndexF)



# Use your module's ID and secret here
config = configparser.ConfigParser()
config.read("config.ini")

moduleID = "12345"
moduleSecret = "qwerty"

# Create a WS module and connect to the SDK
module = WebSocketModule()
success = module.connect(moduleID, moduleSecret)

if not success:
    print("Unable to authenticate with Kai SDK")
    exit(1)

# Set the default Kai to record gestures and accelerometer readings
module.setCapabilities(module.DefaultKai, KaiCapabilities.GestureData | KaiCapabilities.PYRData | KaiCapabilities.QuaternionData | KaiCapabilities.FingerShortcutData)

# Register event listeners
module.DefaultKai.register_event_listener(Events.GestureEvent, gestureEvent)
module.DefaultKai.register_event_listener(Events.PYREvent, pyrEv)
module.DefaultKai.register_event_listener(Events.QuaternionEvent, quatEv)
module.DefaultKai.register_event_listener(Events.FingerShortcutEvent, fingersEv)

#time.sleep(30) # Delay for testing purposes

# Save Kai battery by unsetting capabilities which are not required anymore
# module.unsetCapabilities(module.DefaultKai, KaiCapabilities.AccelerometerData)

#time.sleep(30)

#module.close()

# ws://localhost:2203

# {"type": "authentication", "moduleId": "test", "moduleSecret": "qwerty"}

# {"type": "setCapabilities", "fingerShortcutData": true}
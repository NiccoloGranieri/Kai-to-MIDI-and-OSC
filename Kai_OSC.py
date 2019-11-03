"""
Example program for receiving gesture events and accelerometer readings from Kai
"""

import os
import time
import configparser

from KaiSDK.WebSocketModule import WebSocketModule
from KaiSDK.DataTypes import KaiCapabilities
import KaiSDK.Events as Events

from pythonosc.dispatcher import Dispatcher
from pythonosc.udp_client import SimpleUDPClient

dispatcher = Dispatcher()

client = SimpleUDPClient("127.0.0.1", 1337)

def gestureEvent(ev):
    gestureString = ev.gesture
    if (str(gestureString) == "Gesture.swipeUp"):
        client.send_message("/gesture", 1)
        print("down")
    elif (str(gestureString) == "Gesture.swipeDown"):
        client.send_message("/gesture", 2)
    elif (str(gestureString) == "Gesture.swipeLeft"):
        client.send_message("/gesture", 3)
    elif (str(gestureString) == "Gesture.swipeRight"):
        client.send_message("/gesture", 4)

def pyrEv(ev):
    client.send_message("/pitch", ev.pitch)
    client.send_message("/yaw", ev.yaw)
    client.send_message("/roll", ev.roll)

def quatEv(ev):
    client.send_message("/quatW", ev.quaternion.w)
    client.send_message("/quatX", ev.quaternion.x)
    client.send_message("/quatY", ev.quaternion.y)
    client.send_message("/quatZ", ev.quaternion.z)

def fingersEv(ev):
    print("Happening")
    client.send_message("/littleFinger", ev.littleFinger)
    client.send_message("/ringFinger", ev.ringFinger)
    client.send_message("/middleFinger", ev.middleFinger)
    client.send_message("/indexFinger", ev.indexFinger)



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

# module.DefaultKai.register_event_listener(Events.AccelerometerEvent, accelerometerEv)
# module.DefaultKai.register_event_listener(Events.GyroscopeEvent, gyroscopeEv)
# module.DefaultKai.register_event_listener(Events.MagnetometerEvent, magnetEv)

#time.sleep(30) # Delay for testing purposes

# Save Kai battery by unsetting capabilities which are not required anymore
# module.unsetCapabilities(module.DefaultKai, KaiCapabilities.AccelerometerData)

#time.sleep(30)

#module.close()

# ws://localhost:2203

# {"type": "authentication", "moduleId": "test", "moduleSecret": "qwerty"}

# {"type": "setCapabilities", "fingerShortcutData": true}
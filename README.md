# Kai-to-MIDI-and-OSC

<<<<<<< Updated upstream
Python application that collects gestural data from the [Kai Gesture Controller](https://vicara.co) and parses it as MIDI and/or OSC data.
=======
A collection of scripts that gather gestural data from the [Kai Gesture Controller](https://vicara.co) and parse it as MIDI and/or OSC data.

## Setup instructions

In order to use the following scripts you need to clone this repositories with submodules:

`git clone https://github.com/NiccoloGranieri/Kai-to-MIDI-and-OSC --recurse-submodules`

To run this script you will need Python 3 alongside the [Kai Control Center](https://vicara.co/downloads.html). If you're unsure whether you have python 3 installed on your machine, type `python3` in your terminal window. If your terminal comes back with a "command not found" message, follow [this link](https://programwithus.com/learn-to-code/install-python3-mac/) to install Python 3 on your machine.

NOTE: This script has been developed and tested solely on macOS. While it should run on Windows, it has not been tested at this stage and comes with no guarantee.

Once Python 3 is installed, you will have to install some python libraries through your terminal. Run the following commands with the word `sudo` in front to give administrative access for installation purposes:

- `sudo python3 setup.py install` from the kai-python submodule folder
- `sudo pip3 install python-rtmidi`
- `sudo pip3 install python-osc`

Once all of the above libraries are installed you will have to navigate to the kai-python folder and install the Kai SDK. To do so, first navigate to the kai python:

`cd Users/_path_to_this_folder_/Kai-to-MIDI-and-OSC/kai-python`

then run:

`sudo setup.py install`

## Use

To use this script you will have to:

1. Plug-in the dongle
2. Switch on the Kai making sure that the connection is established
3. Run one of the scripts

## Troubleshooting

If the kai seems to be not sending any data but is succesfully connected and recognised in the Kai Control Center.app, simply kill the script (typing `ctrl + C` in the terminal window) and relaunch it.

## Kai_OSC

The Kai_OSC script sends data in the following format:

#### Gestures

Gestures are recognised and converted in an integer that defines the type of gesture recognised.

- Swipe Up: `/gesture 1`
- Swipe Down: `/gesture 2`
- Swipe Left: `/gesture 3`
- Swipe Right: `/gesture 4`

#### Pitch, Yaw, Roll

Pitch, Yaw and Roll are sent as an integer of varying range.

- `/pitch int(-79, 79)`
- `/yaw int(-179, 179)`
- `/roll int(-179, 179)`

#### Quaternion Data

Quaternion data is send as a floating point varying between -1 and 1.

- `/quatW float`
- `/quatX float`
- `/quatY float`
- `/quatZ float`

#### Fingers Data

The data coming from the infrared sensors is sent as a single boolean message per finger.

- `/littleFinger bool(0-1)`
- `/ringFinger bool(0-1)`
- `/middleFinger bool(0-1)`
- `/indexFinger bool(0-1)`
>>>>>>> Stashed changes

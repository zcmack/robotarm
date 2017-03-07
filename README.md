# robotarm
###An exercise to control a robot arm to stack blocks in python



Developed on OSX using Python 2.7.12, use Python 3 at your own risk

To start the application, navigate to the project in a terminal and execute:
`python stacker.py`


### Available Commands:

* size [n] - Adjusts the number of slots, resizing if necessary. Program must start with this to be valid.
* add [slot] - Adds a block to the specified slot.
* mv [slot1] [slot2] - Moves a block from slot1 to slot2.
* rm [slot] - Removes a block from the slot.
* replay [n] - Replays the last n commands.
* undo [n] - Undo the last n commands.

The code has additional documentation regarding behavior of these commands inline.

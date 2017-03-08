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


###Additional info / Lessons Learned

My decision to use python made this exercise interesting. I have only worked on very small efforts in the past that have used python and would consider myself a beginner. The criteria for this exercise indicated I should use no additional libraries other than what is standard in the language and for sake of creating a program easily launched on any platform from the command line, I chose python. I'm very happy I didn't choose bash. :)

In retrospect, I would have prioritized writing unit tests, and probably would have done so for replay and undo as soon as possible. Addressing the commands in sequential order left me refactoring to better support these functions later in the exercise and testing manually felt very silly. One unplanned benefit of python was the versatility of the list object to support functions traditionally associated with a stack or queue.

If I were to make additional improvements, I would further refactor this code to isolate the state machine operations from the command line interface to better separate concerns. The goal was accomplished as-is using python but I could definitely stand to learn a bit more about how a program is traditionally structured if I was to use the language more frequently.



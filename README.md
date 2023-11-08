# ECE3011_T08_TeamProject

ECE 3011 Capstone Design Project.

Implementing Microbit software architecture to control educational device for 1st and 2nd grade public school teacher lesson plans.

The main script to run the robot needs to be compiled to a .hex file and dropped onto the microbit drive when plugged in to via micro-usb to USB

After cloning repository to local, to access main script to run robot:

```
cd ECE3011_T08_TeamProject/source
```

Download this file or copy this file over to a python script shell, recommended editor/compiler is the micro:bit Python Editor, linked below:
https://python.microbit.org/v/3/reference/display

After uploading code to compiler, click "Save" in the bottom left corner of the screen.
This will comile the python script to .hex to be used on the microbit.

Hex file can then be flashed onto Microbit for final use.

To access libraries written and used:
```
cd ECE3011_T08_TeamProject/source/digital
```
Within here you can view the 7 segment libraries, servo libraries, and additional self written python libary functions for bridging C++.

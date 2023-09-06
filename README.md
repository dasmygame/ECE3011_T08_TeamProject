# ECE3011_T08_TeamProject

ECE 3011 Capstone Design Project.

Implementing Microbit software architecture to control educational device for 1st and 2nd grade public school teacher lesson plans.

The source/examples folder contains a selection of subsystems demonstrating the capabilities and usage of the device.
To select a sample, simply copy the .cpp files from the relevant folder into the source/ folder.

e.g. to select the "digital" example:

```
cp source/examples/digital/* source
```

and then to compile your sample:

```
yt clean
yt build
```

The HEX file for you micro:bit with then be generated and stored in build\bbc-microbit-classic-gcc\source\microbit-samples-combined.hex

Hex file can then be flashed onto Microbit for final use.

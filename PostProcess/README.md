This python script is used to post process gcode generation in Prusaslicer 2.5.0. It's function is to rebuild the M106 part cooling fan commands so they correctly turn on (and off) the correct fan.

Prusaslicer does not currently (and as Prusa Research do not produce a multi extruder IDEX machine) is not likely to do so.

This script could also be used in SuperSlicer which is a fork of Prusaslicer - although I've not tested it yet

For users of Cura, one redeeming benefit is that it get the IDEX fan commands correct so fan post processing is not needed - although Cura is lacking in some other areas. If you are a Cura expert, take a look at BCN3D's equivalent setup for their Sigmax IDEX printers

In Prusa Slicer, in the Print Settings tab, under Output Options, enter the path of the Python script into the bottom section.

You will need to have Python3 installed on your system along with any necessary Python modules.

Test manually at first to ensure the paths are setup correctly.

    <path>/python3 idex_fan_m106.py gcodefilename.gcode

It will overwrite the gcode file and you should see something like this:

    M107 P0
    M106 P1 S234
    T1

appearing around the toolchange commands.

If all you're getting is:

    M106 S234

Then it's not working correctly.

This is still a work in progress. I need to test the actual gcode generated extensively.

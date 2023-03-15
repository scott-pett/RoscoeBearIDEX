#!/opt/homebrew/bin/python3

#
# PrusaSlicer PostProcess script to modify M106 part cooling fan commands
# to control a fan on each extruder.
#
# Works OK on a twin extruder IDEX printer by turning off the previous fan and
# setting the correct fan for the extruder just before the tool change
# All other commands are passed through to the output gcode file.
#
# Seems to work OK on single extruder printers - as it basically ignores M106
# commands without a consecutive Tool Change command.
#
# Thanks to Bob George's bumpfan.py script for the basic bones of the script
# with a few tweaks to work with Prusaslicer 2.5.0 and port to Python3
#
# Tested on PrusaSlicer 2.5.0 14/3/23
#

# Get the stuff we need
#
import sys, re, os

# Read the entire g-code file into memory buffer
#
sourceFile=sys.argv[1]
with open(sourceFile, "r") as inputfile:
    lines = inputfile.readlines()
    inputfile.close()

# We must use the source file path as the output file other Prusaslicer will
# just output the original file. Must be something to do with nodes.
# Unfortunately, PS doesn't really tell you what's going on.
#
with open(sourceFile, "w") as of:
    for lIndex in range(len(lines)):
        oline = lines[lIndex]
        # Should search for IDEX mode to see if we need to do anything at all
        # i.e. grep M605 S1 or something.
        # Bail, if not an IDEX printer
        # However - seems to work OK on single extruder printer by doing nothing
        # Parse gcode line
        parts = oline.split(';', 1)
        if len(parts) > 0:
            # Parse command for M106 at the beginning of the line
            command = parts[0].strip()
            if command:
                stringMatch = re.search ('^M106', command)
                if stringMatch:
                    #
                    # get the fan command itself
                    fan_command = command.split(' ', 1)
                    print(fan_command)
                    #
                    # and the fan speed setting
                    fan_speed = fan_command[1]
                    print(fan_speed)
                    #
                    # Now try to find a toolchange command at the beginning of the next line:
                    tline = lines[lIndex + 1]
                    stringMatch = re.search ('^T', tline)
                    if stringMatch:
                        fan_index = tline[1]
                        #
                        # generate the new M106 fan command i.e. M106 P(fan_index) S(fan_speed)
                        newfanline=('M106 P' + fan_index + ' ' + fan_speed + '\n')
                        print(newfanline)
                        #
                        # command the other fan off
                        if fan_index == "1" :
                            of.write('M107 P0\n')
                        elif fan_index == "0" :
                            of.write('M107 P1\n')
                        else:
                            print('no fan index!')
                        #
                        # and write out the new fan command
                        of.write(str(newfanline))
                    else:
                        # if none of the above happens  Write original line
#                       # Not sure how many of these we need so we'll keep all of them
                        of.write(oline)
                else:    
                    of.write(oline)
            else:
                of.write(
                    oline)
        else:
            of.write(oline)

of.close()

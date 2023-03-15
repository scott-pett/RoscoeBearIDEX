# Roscoe Bear IDEX 3D Printer

<image>

This is a remix of the Bear frame upgrade to the Prusa MK3S.

Make it wider, taller and use most of the original plastic parts to create a much wider printer to make room for a 300mm x 200mm bed and two independant extruders. Print height is currently 230mm, but I'm hoping to improve on that slightly without spending too much money.

# History
The design has been ongoing since 2017 or so and there is now a working prototype albeit lacking in certain features. The prototype has done useful work, but mainly as a single extruder print :-)

Looking back at some of the design files, things have change greeatly from the earliest concept.

# Electronics and Firmware
The printer currently runs Marlin 2.1.x and uses a BTT Octopus control board wiht TMC2130 and TMC2208 stepper dreivers along with an ancient Full Graphics Display. A Raspberry Pi 3B+ acts as an Octoprint host and provides WiFi network connectivity.

## Klipper as an option
Of course, Klipper firmware could be used but I feel there would be few advantages except perhaps that of input shaping which has some better capabilities than Marlin2 current has. I doubt there would be much speed advantage being a "bed-slinger" although firmware updates would be more convenient that loading a microSD card into the slot after compiling Marlin in VScode - Horses for Courses

# IDEX Carriages
The main departure from the Prusa Bear is of course the X and U carriages (AKA: X and X2) which need to allow for the extra U (X2) stepper motor, belt and idler. For the moment this takes the form of a taller X carriage to make room for it all.

# Extruders
The X and U extruders are basically Prusa MK3S but with the wiring harness exiting the top of the units - there's not enough room betwee all the belts to provide the Prusaesque wiring egress.
The left hand extruder cassies a PINDA2 probe for Z homing. This currently runs successfully at 3.3 volts with the spring steel flexplate. The righthand extruder being offset in the Marlin config to allow for any differences. At the moment, this means that the printer will only work in IDEX mode 1 - Auto Park. Mirroring and Cloning (modes 2 and 3) will not be highly successful.
Filmanet runout on both extruders is supported as per the Prusa setup.

X, U and Y endstops are handled by the TMC2130 drivers (TMC2209 as an alternative). Z endstop is as stated a PINDA2 probe.

The heated bed is a generic 300 x 200mm MK2-B (I think) with a flexplate print surface.

# Work To Do
1. Adjustable height for the U carriage and extruder
2. Purge buckets - or a far more reliable purge tower control.
3. Move to Prusaslicer from Cura to improve print quality.
4. Twin part fan control which Prusaslicer doesn't generate
5. Shorten the height of the X and U carriage to increase the evailable print height.
6. Switch to a PEI sheet from the exisitng.
7. Finalize the Marlin2 config files.

# Alternatives

1. Control board could be a Spider board - 7 steppers are required for IDEX with two independant Z motors.
2. I did originally use an MKS RUMBA32 clone, but this only has support for six steppers and you have to do without the automatic Gantry levelling. However this can be hacked reasonably well with a gcode script.
3. Stepper drivers could be TMC2209 for STallguard on X, U and Y axis with TMC2208 for the extruders and Z motors. Although TMC have moved on now with driver options. You could always modify the enstop arrangement to something more tradiitonal if that is you required.
4. Heated bed - In order to keep the weight down I have used a lightweight bed with flexible spring steel sheet carrying a BuildTaK print surface. Of course a glass sheet and blue tape could be used if that is your preference. My favourite, especially for PETG is a textured PEI surface which will be a future upgrade, once I find one - or when the BuildTak surface wears out.
5. Extruder options are of course to used E3D Revo 6 hotend or with some work a Stealthburner hotend with Clockwork 1 or 2 extruder and blingie RGB LEDs on it. - up to you really. There is a lot of work involved in getting the Stealburner to fit onto the exisitng carriage arrangement.
6. Many other ideas as they occur.


# Summary 
This is very much a work in progress and is a long way behind things like the BCN3D Sigma and Voron IDEX work that is going on. As a "bed-slinger" its is never going to be as fast as either of the above, but is a fairly simple build from a frame point of view. The Prusa extruders are fairly easy to build and maintain and there's plenty of life left in the E3D V6 ecosystem. Especially with the new innovative Revo 6 nozzles.

If you have questions or ideas, please contact me.

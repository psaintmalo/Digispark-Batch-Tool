# Digispark_Batch_Tool

This is a simple tool to quickly add commands for a digispark to do batch processes by emulating a keyboard

To use it simple open the python file and follow the instructions, as of v0.4, .bat to .ino file conversion is not supported, but is planned for the future. After finishing you may copy the lines from the file and paste them into to the setup void of a blank arduino project.

The creation of the automatic addition of the void is also planned so the file may be saved as an .ino and opened directly

Current commands are:
  - WIN_R   Opens the windows run box
  - SHORT   Lets you make short cuts of Win/Ctrl + one letter
  - ENTER   Presses enter
  - DELETE  Deletes the file and ends the program
  - STOP    Closes the program
  - READ    Will read the file
  - HELP    Will show this list on the program
  - To make the digispark type something as a keyboard would into the computer, you will need to type it in lower case
  - To add a delay between certain commands, just type the amount of ms of the delay
  
The delay after the commands WIN_R and ENTER can be adjusted on the settings.py file, by default it is 0ms. 

For any help regarding to how to setup the computer to use the Digispark, here is a link which explains it pretty well
https://youtu.be/fGmGBa-4cYQ?t=14s

Also, remember to use the Arduino IDE 1.8.5 as later ones wont work with the digispark.

# Digispark_Batch_Tool

This is a simple tool to quickly add simple comands for a digispark to do batch processes

To use it simple open the python file and type the file name you would want to use, as of v0.3, only the typing it self will be 
created, so you may inset this into the void setup of a blank arduino file.

In future version the whole arduino file will be made.

Current comands are:
  - WIN_R   Opens the windows run box
  - ENTER   Presses enter
  - DELETE   Wipes the file
  - STOP   Closes the program
  - READ    Will read the file
  - HELP    Will show this list on the program
  - To make the digispark type something as a keyboard would into the computer, you will need to type it in lower case
  - To add a delay between certain commands, just type the amount of ms of the delay
  
The delay after the commands WIN_R and ENTER can be adjusted on the settings.py file, by default it is 0ms

For any help regarding to how to setup the computer to use the Digispark, here is a link which explains it prety well
https://youtu.be/fGmGBa-4cYQ?t=14s

Also, remember to use the Arduino IDE 1.8.5 as later ones wont work with the digispark.

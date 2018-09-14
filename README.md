# Digispark_Batch_Tool

This is a simple tool to quickly add commands for a digispark to do batch processes by emulating a keyboard

Current commands are:
 Delay *time*       - Adds a delay between lines (in ms)

 Enter              - Presses enter key

 Type *text*        - Makes the Digispark type as a keyboard
 Command *command*  - Lets you use one of he defined commands
 Command_list       - Lists the available commands
 Print File         - Prints the file
 Undo / Undo *n*    - Deletes the last line / n lines
 Manual             - Lets you type the brackets of DigiKeyboard() manually, should be (*key*, *modifier*)
 Manual line        - Lets you type a line manually
 Short              - Short lets you create commands with Win (Gui)/Ctrl and keys. e.g. short gui A | short ctrl F12
 Clear              - Clears all the lines
 Delete             - Deletes the file
 Finish             - Stops the program. ** Always do it if ino_file = 1 **
 Keys               - Prints a table with all keys and modifiers
 Help               - Shows this list


As of v1.0, .bat to .ino file conversion is not supported, but is planned for the future.

For any help regarding to how to setup the computer to use the Digispark, here is a link which explains it pretty well
https://youtu.be/fGmGBa-4cYQ?t=14s

The latest tested arduino IDE compatible with Digispark is 1.8.5

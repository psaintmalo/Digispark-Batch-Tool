from pathlib import Path

import os


def command_list():
    print("WIN_R")
    print("ENTER")
    print("TYPE")
    print("DELAY")
    print("BLANK - Wipes the document and you can continue writing")
    print("LIST - Show's this list")
    print("BREAK - Finishes the program")


def appender(file, command, f_name):

    if command == "WIN_R":
        file.write("  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);\n")
        file.write("  DigiKeyboard.delay(100);\n")
    elif command == "ENTER":
        file.write("  DigiKeyboard.sendKeyStroke(KEY_ENTER);\n")
        file.write("  DigiKeyboard.delay(500);\n")
    elif command == "TYPE":
        text = input("Type:")
        file.write('  DigiKeyboard.println("' + text + '");\n')
    elif command == "DELAY":
        delay_timer = input("")
        file.write('  DigiKeyboard.delay(' + delay_timer + ');\n')
    elif command == "LIST":
        command_list()
    elif command == "BLANK":
        os.remove(f_name)
        f = open(f_name, "w+")
    elif command == "READ":
        with open(f_name) as f:
            lines = f.readlines()
            for line in lines:
                print(line)
    else:
        print("Please type it again")

name = input("Name your file:")
my_file = Path(name)
if my_file.is_file():
    replace = input("Do you want to replace the file? Y/N")
    if replace == "Y":
        os.remove(name)
        f = open(name, "w+")
else:
    f = open(name, "w+")
command_list()
while 1:
    command = input(":")
    if command == "BREAK":
        break
    appender(f, command, name)

import os
from files.general import *


# def auto_delay_check():
#     if auto_delay_toggle:
#         if enter_delay != "0" and win_r_delay != "0":
#             print("Automated delay is on")
#         else:
#             print("Automated delay is off")
#
#
# def auto_delay(my_file):
#     my_file = open(my_file.name, "a")
#     my_file.write("  DigiKeyboard.delay(" + enter_delay + ");\n")
#     my_file.close()


def appender(command, rest, my_file):

    my_file = open(my_file.name, "a")

    if command.lower() == "type":
        my_file.write('  DigiKeyboard.println("' + rest + '");\n')

    elif command.lower() == "delay":
        if rest.isdigit():
            my_file.write('  DigiKeyboard.delay(' + rest + ');\n')
        else:
            print("Delay should be a number")

    elif command.lower() == "undo":
        my_file = open(my_file.name, "r")
        lines = my_file.readlines()
        my_file.close()
        my_file = open(my_file.name, "w")

        if rest == "":
            my_file.writelines([item for item in lines[:-1]])

        else:
            my_file.writelines([item for item in lines[:-int(rest)]])

    elif command.lower() == "enter":
        my_file.write('  DigiKeyboard.sendKeyStroke(KEY_ENTER);\n')

    elif command.lower() == "manual":
        second, sub_remainder = sub_command(rest)

        if second == "line":
            my_file.write("  " + sub_remainder)

        else:
            my_file.write('  DigiKeyboard.sendKeyStroke(' + rest + ');\n')

    elif command.lower() == "short":  # REVIEW THIS CODE
        sub_com, key = sub_command(rest)

        if sub_com.lower() != "gui" and sub_com.lower() != "ctrl":
            print("Please type Ctrl or Gui (for windows/cmd)")

        else:
            if sub_com.lower() == "gui":
                modifier = "MOD_GUI_LEFT"

            elif sub_com.lower() == "ctrl":
                modifier = "MOD_CONTROL_LEFT"

            # noinspection PyUnboundLocalVariable
            my_file.write("  DigiKeyboard.sendKeyStroke(KEY_" + key.upper() + ", " + modifier + ");\n")

    elif command.lower() == "keys":
        keys_file = open("files/key_table", "r")
        print(keys_file.read())

    elif command.lower() == "command":
        if rest.lower() == "win_r":
            my_file.write('  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);\n')

        elif rest.lower() == "ctrl_w":
            my_file.write('  DigiKeyboard.sendKeyStroke(KEY_W, MOD_CONTROL_LEFT);\n')

        elif rest.lower() == "alt_f4":
            my_file.write('  DigiKeyboard.sendKeyStroke(KEY_F4, MOD_ALT_LEFT);\n')

    elif command.lower() == "command_list":
        commands_file = open("files/commands", "r")
        print(commands_file.read())

    elif command.lower() == "help":
        help_file = open("files/help_file", "r")
        print(help_file.read())

    elif command.lower() == "print" and rest.lower() == "file":
        my_file = open(my_file.name, "r")
        print("")
        print(my_file.read())
        my_file.close()

    elif command.lower() == "clear":
        my_file.close()
        os.remove(my_file.name)
        my_file = open(my_file.name, "w+")
        print("File cleared")

    elif command.lower() == "delete":
        my_file.close()
        os.remove(my_file.name)
        quit(0)

    elif command.lower() == "quit":
        my_file.close()
        quit(0)

    else:
        print("Please try again")

    my_file.close()

import os


def command_list():
    print("")
    print("Commands are case sensitive!")
    print("")
    print("WIN_R - Opens the run box on windows")
    print("ENTER")
    print("BLANK - Wipes the document and you can continue writing")
    print("STOP - Saves the file and closes the program")
    print("To add a delay, just type the number (in ms)")
    print("To make the digispark type something, you must write it in lower case")
    print("HELP - Show's this list")
    print("")


def appender(file, command, f_name):

    if command.isdigit():
        file.write('  DigiKeyboard.delay(' + command + ');\n')

    elif command.isupper():
        if command == "WIN_R":
            file.write("  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);\n")

        elif command == "ENTER":
            file.write("  DigiKeyboard.sendKeyStroke(KEY_ENTER);\n")

        elif command == "DELETE":
            file.close()
            os.remove(f_name)
            file = open(f_name, "w+")
            file.close()
            print("Deleted")

        elif command == "READ":
            file.close()
            with open(f_name) as f:
                lines = f.readlines()
                for line in lines:
                    print(line)

        elif command == "HELP":
            command_list()

        else:
            print(command + " isn't a known command, please type it again. Type HELP for information of the commands")

    elif command.islower():
        file.write('  DigiKeyboard.println("' + command + '");\n')

    else:
        print("Commands are case sensitive! For information of the commands type HELP")


def auto_delays(command, f_name, ENTER_DELAY, WIN_R_DELAY):
    if command == "ENTER":
        file = open(f_name, "a")
        file.write("  DigiKeyboard.delay(" + ENTER_DELAY + ");\n")
    elif command == "WIN_R":
        file = open(f_name, "a")
        file.write("  DigiKeyboard.delay(" + WIN_R_DELAY + ");\n")

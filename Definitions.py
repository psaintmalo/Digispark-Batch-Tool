import os


def command_list():
    print("")
    print("Commands are case sensitive!")
    print("")
    print("WIN_R - Opens the run box on windows")
    print("ENTER")
    print("BLANK - Wipes the document and you can continue writing")
    print("BREAK - Saves the file")
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
            file.write("  DigiKeyboard.delay(100);\n")

        elif command == "ENTER":
            file.write("  DigiKeyboard.sendKeyStroke(KEY_ENTER);\n")
            file.write("  DigiKeyboard.delay(500);\n")

        elif command == "BLANK":
            os.remove(f_name)
            f = open(f_name, "w+")

        elif command == "READ":
            with open(f_name) as f:
                lines = f.readlines()
                for line in lines:
                    print(line)

        elif command == "HELP":
            command_list()

    elif command.islower():
        file.write('  DigiKeyboard.println("' + command + '");\n')

    else:
        print("Commands are case sensitive! For help type HELP")

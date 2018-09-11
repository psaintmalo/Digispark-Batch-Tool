import os


def command_list():
    print("")
    print("Commands are case sensitive!")
    print("")
    print("WIN_R - Opens the run box on windows")
    print("SHORT - Lets you press shortcuts")
    print("ENTER")
    print("CLEAR - Wipes the document and you can continue from scrath")
    print("STOP - Saves the file and closes the program")
    print("DELETE - Deletes the file and closes the program")
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

        elif command == "SHORT":
            print("Windows key - 1")
            print("Control key - 2")
            key = input("Select key: ")
            if key == "1":
                second_key = input("Please type the other key (a-z): ")
                file.write("  DigiKeyboard.sendKeyStroke(KEY_" + second_key.upper() + ", MOD_GUI_LEFT);\n")
            elif key == "2":
                second_key = input("Please type the other key (a-z): ")
                file.write("  DigiKeyboard.sendKeyStroke(KEY_" + second_key.upper() + ", MOD_CONTROL_LEFT);\n")

        elif command == "CLEAR":
            clear_c = input("Are you sure you want to clear the file? Y/N ")
            if clear_c == "Y":
                file.close()
                os.remove(f_name)
                file = open(f_name, "w+")
                print("File cleared")

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


def auto_delays(command, file, ENTER_DELAY, WIN_R_DELAY):
    if command == "ENTER":
        file.write("  DigiKeyboard.delay(" + str(ENTER_DELAY) + ");\n")

    elif command == "WIN_R":
        file.write("  DigiKeyboard.delay(" + str(WIN_R_DELAY) + ");\n")

from pathlib import Path
from Definitions import *
from settings import *

f = ""
predetermined_delay = 1
if ENTER_DELAY == "0" and WIN_R_DELAY == "0":
    print("There are no predetermined delays, please add them manually or configure them on the settings file")
    predetermined_delay = 0
else:
    print(ENTER_DELAY + "ms delay for enter, " + WIN_R_DELAY + "ms for WIN_R and file extension " + file_extension)

name = input("Name your file: ")
file_name = name + file_extension
my_file = Path(file_name)
if my_file.is_file():
    replace = input("Do you want to replace the file? Y/N ")
    if replace == "Y":
        os.remove(file_name)
        f = open(file_name, "w+")
        f.close()

command_list()

while 1:
    f = open(file_name, "a")
    command = input("--> ")
    if command == "STOP":
        break
    elif command == "DELETE":
        confirmation = input("Are you sure you want to delete the file? Y/N ")
        if confirmation == "Y":
            f.close()
            os.remove(file_name)
            print("File Deleted")
            break
    else:
        appender(f, command, file_name)
    f = open(file_name, "a")
    if predetermined_delay:
        auto_delays(command, f, ENTER_DELAY, WIN_R_DELAY)
    f.close()

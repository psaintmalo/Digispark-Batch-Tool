from pathlib import Path
from Definitions import *
from settings import *

f = ""
predetermined_delay = 1
if ENTER_DELAY == 0 and WIN_R_DELAY == 0:
    print("There are no predetermined delays, please add them manually or configure them on the settings file")
    predetermined_delay = 0
name = input("Name your file: ")
file_name = name + ".txt"
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
    appender(f, command, file_name)
    if predetermined_delay != 0:
        auto_delays(command, file_name, ENTER_DELAY, WIN_R_DELAY)
    f.close()

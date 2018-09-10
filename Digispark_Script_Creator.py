from pathlib import Path
from Definitions import *

f = ""
name = input("Name your file:")
my_file = Path(name)
if my_file.is_file():
    replace = input("Do you want to replace the file? Y/N ")
    if replace == "Y":
        os.remove(name)
        f = open(name, "w+")
    else:
        f = open(name, "a")


command_list()

while 1:
    command = input(":")
    if command == "BREAK":
        break
    appender(f, command, name)

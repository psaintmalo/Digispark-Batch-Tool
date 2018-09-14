from time import sleep
import os
from pathlib import Path
from files.settings import *


def file_creator(m_file):

    if m_file.is_file():
        replace_file = input("This file already exists, do you want to replace it? Y/N ")

        if replace_file.upper() == "Y":
            os.remove(m_file)
            my_file = open(m_file, "w+")
            my_file.close()

        else:
            my_file = open(m_file, "a")
            my_file.close()
            print("")
            print("Lines will be appended to the bottom of the file, to avoid any writing into this file type quit now")
            print("")

    else:
        my_file = open(m_file, "w+")
        my_file.close()

    return my_file


def file_start():
    file_name = input("Name your file: ")
    sleep(0.1)

    if ino_file:
        file_n_e = file_name + ".ino"
        my_file = Path(file_n_e)
        return file_creator(my_file), 1

    else:
        file_n_e = file_name + file_extension
        my_file = Path(file_n_e)
        return file_creator(my_file), 0


def line_prepender(filename, line):
    with open(filename.name, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def ino_appender(my_file):
    line_prepender(my_file, "void setup() {")
    my_file = open(my_file.name, "a")
    ino_last = open("files/blank_ino", "r")
    my_file.write(ino_last.read())

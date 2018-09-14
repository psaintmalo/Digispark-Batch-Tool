from files.file_manager import *
from files.commands import *

check_settings()
# auto_delay_check()
my_file, ino = file_start()
print("Work file = " + my_file.name)

while 1:  # Main Loop
    user_input = input(": ")
    first, rest = word_divider(user_input)
    if first.lower() == "finish":
        break
    appender(first, rest, my_file)
    # auto_delay(my_file)

if ino:
    ino_appender(my_file)

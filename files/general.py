from files.settings import *


def check_settings():
    errors = 0
    # if not isinstance(enter_delay, str) and enter_delay.isnumeric():
    #     print("The entered value for enter_delay is not valid, it should be a number between ")
    #     errors += 1
    #
    # if not isinstance(win_r_delay, str):
    #     print("The entered value for win_r_delay is not valid, it should be a number between ")
    #     errors += 1
    #
    # if (not isinstance(auto_delay_toggle, int)) or (auto_delay_toggle != 1 and auto_delay_toggle != 0):
    #     print("The entered value for auto_delay is not valid")
    #     errors += 1

    if (not isinstance(ino_file, int)) or (ino_file != 1 and ino_file != 0):
        print("The entered value for ino_file is not valid")
        errors += 1

    if errors != 0:
        print("")
        print("Please check the settings file and fix the value(s)")
        quit(2)


def word_divider(words):
    first = ""
    remainder = ""
    char_count = 1

    for char in words:
        if char != " ":
            first += char
            char_count += 1

        else:
            remainder = words[char_count:]
            break

    return first, remainder


def sub_command(remainder):
    second = ""
    sub_remainder = ""
    char_count = 1

    for char in remainder:
        if char != " ":
            second += char
            char_count += 1

        else:
            sub_remainder = remainder[char_count:]
            break
    return second, sub_remainder

"""
COMP.CS.100 Programming 1
Code Template
"""

import sys


def read_message():
    line = "empty"
    lines = []
    while line.strip() != "":
        line = input()
        lines.append(line)

    return '\n'.join(lines)

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    print("The same, shouting:")
    print(msg.upper(), end="")

if __name__ == "__main__":
    main()

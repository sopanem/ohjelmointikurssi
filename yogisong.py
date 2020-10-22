"""
COMP.CS.100 Programming 1
Code template for the hottest hit song Yogi Bear
"""

def repeat_name(name, count):
    for i in range(1, count+1):
        print(f"{name}, {name} Bear")

def verse(line, name):
    print(line)
    print(f"{name}, {name}")
    print(line)
    repeat_name(name, 3)
    print(line)
    print(f"{name}, {name} Bear")
    print("")

def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()

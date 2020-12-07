
"""
COMP.CS.100 Programming 1
Code Template
"""
def encrypt(c):
    is_upper = c >= 'A' and c <= 'Z'
    c = c.lower()
    if c >= 'a' and c <= 'z':
        ch = chr(((ord(c) - ord('a') + 13) % (ord('z') - ord('a') + 1)) + ord('a'))
        if is_upper:
            return ch.upper()
        return ch
    return c

def row_encryption(row):
    result = ""
    for c in row:
        result += encrypt(c)
    return result

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = input("")

    print("The same, shouting:")

    print(row_encryption(msg))

if __name__ == "__main__":
    main()
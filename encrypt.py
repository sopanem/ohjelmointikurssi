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
    row_encryption(c)

if __name__ == '__main__':
    main()

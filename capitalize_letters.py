def capitalize_initial_letters(text):
    result = []
    for n in text.split(" "):
        if len(n) < 1:
            continue
        result.append(n[0].upper() + n[1:].lower())
    return " ".join(result)

def main():
    capitalize_initial_letters(text)

if __name__ == '__main__':
    main()

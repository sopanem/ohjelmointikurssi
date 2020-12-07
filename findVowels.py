def main():
    vowels = ["a", "e", "i", "o", "u", "y", "ä", "ö"]
    word = input("Enter a word: ")

    vowel_tmp = 0
    consonant_tmp = 0

    for i in word:
        if i.lower() in vowels:
            vowel_tmp += 1

        else:
            consonant_tmp += 1

    print(
        f"The word {word} contains {vowel_tmp} vowels and {consonant_tmp} consonants")


if __name__ == '__main__':
    main()

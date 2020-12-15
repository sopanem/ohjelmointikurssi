"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                translated = english_spanish[word]
                print(f"{word}in Spanish is {translated}")

            print(f"The word {word} could not be found from the dictionary.")

        elif command == "A":
            in_en = input("Give the word to be added in English: ")
            in_span = input("Give the word to be added in Spanish: ")
            english_spanish[in_en] = in_span

        elif command == "R":
            to_remove = input("Give the word to be removed: ")
            del english_spanish[to_remove]

        elif command == "P":
            full_dict = sorted(english_spanish)
            for line in full_dict:
                print(line, full_dict[line])

        # Translate whole sentence, if word is not in dictionary, print it in English.
        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")
            print("The text, translated by the dictionary:")

            # Check words from given sentence and translate those using dictionary
            tmp = sentence.split()
            words_tmp_list = []
            # TODO

            for word in tmp:
                if word not in english_spanish:
                    words_tmp_list.append(word)

                else:
                    translated_word = english_spanish[word]
                    words_tmp_list.append(translated_word)

            print("".join(words_tmp_list))

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()

VOYELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def main():
    text = input("Type: ")
    answer = shorten(text)
    print(answer)


def shorten(text):
    new_text = ''
    for letter in text:
        if letter not in VOYELS:
            new_text += letter
        else:
            new_text += ''

    return new_text


if __name__ == "__main__":
    main()

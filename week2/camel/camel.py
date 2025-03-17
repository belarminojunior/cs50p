def main():
    text_input = input("CamelCase: ")
    new_text = toPythonCase(text_input)
    print(new_text)


def toPythonCase(text):
    new_text = ''
    for i in text:
        if (str(i).isupper()):
            new_text += '_' + str(i).lower()
        else:
            new_text += str(i)

    return new_text


if __name__ == "__main__":
    main()

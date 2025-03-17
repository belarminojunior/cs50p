import emoji


def main():
    request = input()
    output = emoji.emojize(request)
    print(output)


if __name__ == '__main__':
    main()

def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


def is_valid(s):
    sliced = ''

    if len(s) < 2 or len(s) > 6:
        return False

    if not str(s).isalnum():
        return False

    for i in range(2, len(s)):
        if not str(s[i]).isnumeric():
            continue
        else:
            sliced = s[i::]
            break

    if sliced.startswith('0') or not str(sliced).isnumeric():
        return False

    return True


if __name__ == "__main__":
    main()

def einstein(m, c=3*10**8):
    return m * c**2


def main():
    m = int(input('m: '))
    print('E:', einstein(m))


main()

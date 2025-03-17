import random
import sys


def main():
    while True:
        try:
            level = random.randint(1, int(input('Level: ')))
            if level > 0:
                break
        except ValueError:
            pass

    while True:
        try:
            guess = int(input('Guess: '))
            if guess < level:
                print('Too small!')
            elif guess > level:
                print('Too large!')
            else:
                print('Just right!')
                break
        except ValueError:
            pass


if __name__ == '__main__':
    main()

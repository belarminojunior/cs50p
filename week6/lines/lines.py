import sys


def main():
    if len(sys.argv) <= 1:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        if not str(sys.argv[1]).endswith('.py'):
            sys.exit('Not a Python file')
        else:
            print(get_lines_of_code(sys.argv[1]))


def get_lines_of_code(file):
    lines_counter = 0

    try:
        with open(file, 'r') as f:
            for line in f:
                if not (line.lstrip().startswith('#') or line.strip() == ''):
                    lines_counter += 1
            return lines_counter
    except FileNotFoundError:
        sys.exit('File does not exist!')


if __name__ == '__main__':
    main()

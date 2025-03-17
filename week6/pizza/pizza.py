import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) <= 1:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        if not str(sys.argv[1]).endswith('.csv'):
            sys.exit('Not a CSV file')
        else:
            print_table(sys.argv[1])


def print_table(file):
    try:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            print(tabulate(csv_reader, headers='firstrow', tablefmt='grid'))

    except FileNotFoundError:
        sys.exit('File does not exist!')


if __name__ == '__main__':
    main()

import sys
import csv


def main():
    if len(sys.argv) <= 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        if not (sys.argv[1].endswith('.csv') or sys.argv[2].endswith('.csv')):
            sys.exit('Not a CSV file')
        else:
            read_files(sys.argv[1], sys.argv[2])


def read_files(file1, file2):
    try:
        f = open(file1)
    except FileNotFoundError:
        sys.exit(f'Could not read {file1}')
    else:
        list_of_dict = []
        with f as file:
            reader = csv.DictReader(file)
            for row in reader:
                x, y = row['name'].split(', ')
                list_of_dict.append(
                    {'first': y, 'last': x, 'house': row['house']})

        with open(file2, 'w') as file:
            writer = csv.DictWriter(
                file, fieldnames=['first', 'last', 'house'])

            writer.writeheader()
            for i in range(len(list_of_dict)):
                writer.writerow(
                    {'first': list_of_dict[i]['first'], 'last': list_of_dict[i]['last'], 'house': list_of_dict[i]['house']})


if __name__ == '__main__':
    main()

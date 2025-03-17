MONTHS = ['January', 'February', 'March',
          'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def main():
    while True:
        try:
            date = input('Date (MM/DD/YYYY) || (Month DD, YYYY): ').strip()
            if date[0].isdigit():
                month, day, year = map(int, date.split('/'))

                if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
                    print(f'{year:04}', f'{month:02}', f'{day:02}', sep='-')
                    break
            else:
                month, day, year = date.split(' ')
                month = month.capitalize()
                day = int(day.replace(',', ''))
                year = int(year)

                if month in MONTHS and 1 <= day <= 31 and year > 0:
                    print(f'{year:04}',
                          f'{MONTHS.index(month) + 1:02}', f'{day:02}', sep='-')
                    break

        except ValueError:
            pass
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()

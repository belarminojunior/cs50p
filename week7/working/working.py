import re


def main():
    print(convert(input('Hours: ')))


def convert(hours):
    regex = '(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)'
    match = re.search(r"^" + regex + " to " + regex +
                      "$", hours, re.IGNORECASE)

    if match:
        from_time = make_standard(match.group(
            1), match.group(2), match.group(3))
        time = make_standard(match.group(
            4), match.group(5), match.group(6))
        return f'{from_time} to {time}'
    else:
        raise ValueError


def make_standard(hour, min, x):  # x stands for AM or PM
    if hour == '12':
        if x == 'AM':
            hour = '00'
        else:
            hour = '12'
    else:
        if x == 'AM':
            hour = f'{int(hour):02}'
        else:
            hour = f'{int(hour)+12}'

    if min == None:
        minute = '00'
    else:
        minute = f'{int(min):02}'

    return f'{hour}:{minute}'


if __name__ == '__main__':
    main()

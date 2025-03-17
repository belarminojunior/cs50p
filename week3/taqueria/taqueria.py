foods = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    price = 0
    print('-----MENU-----')
    for key in foods.items():
        print(key)

    while True:
        try:
            item = input("Item: ").title().strip()
            price = price + foods[item]
            print(f"Total: ${price:.2f}")
        except EOFError:
            print()
            break
        except KeyError:
            pass


if __name__ == "__main__":
    main()

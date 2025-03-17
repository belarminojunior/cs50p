COINS = [5, 10, 25]


def main():
    AMOUNT_DUE = 50
    while AMOUNT_DUE > 0:
        print(f"Amount Due: {AMOUNT_DUE}")

        coin = int(input("Insert Coin: "))

        if coin in COINS:
            AMOUNT_DUE -= coin

    print(f"Change Owed: {abs(AMOUNT_DUE)}")


main()

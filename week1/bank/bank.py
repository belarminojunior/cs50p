greeting = input("Greeting: ").casefold()

if greeting.__contains__("hello".casefold()):
    print("$0")
elif greeting.startswith('h'):
    print("$20")
else:
    print("$100")

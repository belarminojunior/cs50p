x, expr, y = input("Expression: ").strip().split(" ")

x = float(x)
y = float(y)

if expr == "+":
    print(x + y)
elif expr == "-":
    print(x - y)
elif expr == "/":
    print(x / y)
elif expr == "*":
    print(x * y)

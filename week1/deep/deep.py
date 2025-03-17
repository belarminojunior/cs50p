ans = input(
    "What's the Answer to the Great Question of Life, the Universe, and Everything? ").casefold().strip()

if ans == "42" or ans == "Forty two".casefold() or ans == "Forty-Two".casefold():
    print("Yes")
else:
    print("No")

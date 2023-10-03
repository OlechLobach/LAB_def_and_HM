def display_square(side_length, symbol, filled):
    if filled:
        for _ in range(side_length):
            print(symbol * side_length)
    else:
        print(symbol * side_length)
        for _ in range(side_length - 2):
            print(symbol + " " * (side_length - 2) + symbol)
        print(symbol * side_length)
side_length = int(input("введіть число"))
symbol = "*"
filled = False
display_square(side_length, symbol, filled)
filled = True
display_square(side_length, symbol, filled)

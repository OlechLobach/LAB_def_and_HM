def display_line(length, direction, symbol):
    if direction == "horizontal":
        print(symbol * length)
    elif direction == "vertical":
        for _ in range(length):
            print(symbol)
    else:
        print("Неправильний напрямок. Виберіть 'horizontal' або 'vertical'.")
length_h = 5
direction_h = "horizontal"
symbol_h = "_"
display_line(length_h, direction_h, symbol_h)
length_v = 3
direction_v = "vertical"
symbol_v = "|"
display_line(length_v, direction_v, symbol_v)

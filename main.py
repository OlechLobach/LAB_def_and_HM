def display_line(length, direction, symbol):
    if direction == "horizontal":
        print(symbol * length)
    elif direction == "vertical":
        for _ in range(length):
            print(symbol)
    else:
        print("Неправильний напрямок. Виберіть 'horizontal' або 'vertical'.")
length_h = int(input('введіть довжину лінії'))
length_v = int(input('введіть висоту лінії'))


direction_v = "vertical"
symbol_v = "#"
display_line(length_v, direction_v, symbol_v)
direction_h = "horizontal"
symbol_h = "*"
display_line(length_h, direction_h, symbol_h)







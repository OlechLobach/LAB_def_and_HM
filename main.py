def count_digits(number):
    num_str = str(number)
    count = len(num_str)
    return count
num = int(input("введіть число"))
digit_count = count_digits(num)
print(f"Кількість цифр у числі {num} дорівнює {digit_count}")


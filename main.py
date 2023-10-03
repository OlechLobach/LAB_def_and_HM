def calculate_product(start, end):
    if start > end:
        start, end = end, start
    product = 1
    for num in range(start, end + 1):
        product *= num
    return product
start_num = int(input("введіть початкове число"))
end_num = int(input("введіть кінцеве число"))
result = calculate_product(start_num, end_num)
print(f"Добуток чисел від {start_num} до {end_num} дорівнює {result}")

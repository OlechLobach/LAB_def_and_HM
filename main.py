def find_min(num1, num2, num3, num4, num5):
    min_value = min(num1, num2, num3, num4, num5)
    return min_value

# Приклад виклику функції з числами
num1 = int(input('введіть перше число'))
num2 = int(input('введіть друге число'))
num3 = int(input('введіть третє число'))
num4 = int(input('введіть четверте число'))
num5 = int(input('введіть п`яте число'))

min_number = find_min(num1, num2, num3, num4, num5)
print(f"Мінімальне число: {min_number}")

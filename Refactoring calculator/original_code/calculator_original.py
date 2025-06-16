num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

print(f"\nСума: {num1} + {num2} = {sum_result}")
print(f"Різниця: {num1} - {num2} = {difference_result}")
print(f"Добуток: {num1} * {num2} = {product_result}")

if num2 != 0:
    division_result = num1 / num2
    print(f"Частка: {num1} / {num2} = {division_result}")
else:
    print("Частка: ділення на нуль неможливе")
numbers = []

print("Please enter five numbers:")
for i in range(1, 6):
    number = float(input(f"Input a number {i}: "))
    numbers.append(number)

print(f"\nOriginal list: {numbers}")

numbers.sort(reverse=True)

print(f"Sorted from highest to lowest: {numbers}")
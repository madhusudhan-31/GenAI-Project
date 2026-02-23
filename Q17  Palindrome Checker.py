

value = input("Enter word/number: ")

print("\nOriginal:", value)

reversed_value = value[::-1]
print("Reversed:", reversed_value)


if value.lower() == reversed_value.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT a palindrome")
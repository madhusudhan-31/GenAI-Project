# Program to calculate Sum, Average, Max, Min

count = int(input("How many numbers? "))

numbers = []

for i in range(1, count + 1):
    num = float(input(f"Enter number {i}: "))
    numbers.append(num)

# Calculations
total = sum(numbers)
average = total / count
maximum = max(numbers)
minimum = min(numbers)

# Display Results
print("\n=== RESULTS ===")
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
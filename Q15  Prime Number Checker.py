# Prime Number Program

# =======================
# Part 1: Check Single Number
# =======================

num = int(input("Enter a number: "))

if num < 0:
    print(num, "is NOT a prime number (Negative numbers are not prime).")

elif num == 0:
    print("0 is NOT a prime number.")

elif num == 1:
    print("1 is NOT a prime number.")

elif num == 2:
    print("2 is a PRIME number.")

else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a PRIME number")
    else:
        print(num, "is NOT a prime number")

# =======================
# Part 2: Prime Numbers in Range
# =======================

start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

for number in range(start, end + 1):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                break
        else:
            print(number, end=", ")

print()
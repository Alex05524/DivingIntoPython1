def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Get user input
number = int(input("Enter a number: "))

# Check if the number is prime or composite
if number < 0 or number > 100000:
    print("Number out of range.")
else:
    if is_prime(number):
        print("Prime number.")
    else:
        print("Composite number.")
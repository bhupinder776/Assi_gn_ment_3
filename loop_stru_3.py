def is_prime(number):
    # Handle edge cases
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    # Check for factors from 5 to the square root of the number
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True


def main():
    try:
        user_input = int(input("Enter an integer to check if it is a prime number: "))
        if is_prime(user_input):
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Call the main function to run the program
main()

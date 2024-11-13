# Function to double the number
def double_number(num):
    return num * 2

# Main program
while True:
    user_input = input("Enter a number: ")

    try:
        number = float(user_input)
        doubled_number = double_number(number)
        print(f"Doubled number: {doubled_number}")

        if doubled_number >= 100:
            print("The number is now 100 or greater. Exiting the program.")
            break
    except ValueError:
        print("Please enter a valid number.")

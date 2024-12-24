def show_questions():
    print("Select a question to see the output:")
    print("1. Add two numbers")
    print("2. Find remainder when a number is divided by z")
    print("3. Check the type of a variable")
    print("4. Compare two numbers")
    print("5. Find the average of two numbers")
    print("6. Calculate the square of a number")

def add_two_numbers():
    a = 10
    b = 29
    print(a + b)

def find_remainder():
    a = 10
    z = 3
    c = a % z
    print(c)

def check_type():
    a = input("Enter a number: a")
    t = type(a)
    print(t)

def compare_numbers():
    a = 34
    b = 80
    print(a > b)

def average_of_two_numbers():
    a = int(input("Enter a number: a"))
    b = int(input("Enter a number: b"))
    print("The average of these two numbers is: ", (a + b) / 2)

def square_of_number():
    a = int(input("Enter a number: a"))
    print("The square of the number is: ", a * a)

# Main function to display questions and execute the selected option
def main():
    show_questions()
    choice = int(input("Enter the number of the question you want to see: "))
    
    if choice == 1:
        add_two_numbers()
    elif choice == 2:
        find_remainder()
    elif choice == 3:
        check_type()
    elif choice == 4:
        compare_numbers()
    elif choice == 5:
        average_of_two_numbers()
    elif choice == 6:
        square_of_number()
    else:
        print("Invalid choice!")

# Run the program
main()

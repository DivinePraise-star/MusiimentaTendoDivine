# Assignment 1: Bill Split Calculator

def get_numeric_input(prompt):
    """
    Gets a numeric input from the user, with validation.
    It ensures the user enters a positive number.
    """
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_tip_percentage():
    """
    Gets the tip percentage from the user.
    Offers predefined options or a custom value.
    """
    print("\nChoose a tip percentage:")
    print("1. 10%")
    print("2. 15%")
    print("3. 20%")
    print("4. Custom")

    while True:
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            return 10.0
        elif choice == '2':
            return 15.0
        elif choice == '3':
            return 20.0
        elif choice == '4':
            return get_numeric_input("Enter custom tip percentage: ")
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

def calculate_bill(total_bill, num_people, tip_percent):
    """
    Calculates the tip amount, total bill with tip, and amount per person.
    Returns a dictionary with the calculated values.
    """
    tip_amount = total_bill * (tip_percent / 100)
    total_with_tip = total_bill + tip_amount
    amount_per_person = total_with_tip / num_people
    
    return {
        "tip_amount": tip_amount,
        "total_with_tip": total_with_tip,
        "amount_per_person": amount_per_person
    }

def display_receipt(bill_details, total_bill, num_people, tip_percent):
    """
    Displays a formatted receipt with all the calculations.
    """
    print("\n--- Receipt ---")
    print(f"Total Bill: ${total_bill:.2f}")
    print(f"Number of People: {int(num_people)}")
    print(f"Tip Percentage: {tip_percent}%")
    print("-" * 15)
    print(f"Tip Amount: ${bill_details['tip_amount']:.2f}")
    print(f"Total Bill with Tip: ${bill_details['total_with_tip']:.2f}")
    print("-" * 15)
    print(f"Each person's share: ${bill_details['amount_per_person']:.2f}")
    print("--- End of Receipt ---")

def main():
    """
    Main function to run the Bill Split Calculator.
    """
    print("--- Bill Split Calculator ---")
    
    # 1. Ask for inputs
    bill_amount = get_numeric_input("Enter the total bill amount: $")
    number_of_people = get_numeric_input("Enter the number of people: ")
    tip_percentage = get_tip_percentage()
    
    # 2. Calculate
    calculations = calculate_bill(bill_amount, number_of_people, tip_percentage)
    
    # 3. Output
    display_receipt(calculations, bill_amount, number_of_people, tip_percentage)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()

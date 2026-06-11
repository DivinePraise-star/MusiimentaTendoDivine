# A simple database of users, their passwords, and their roles
users = {
    "admin": {"password": "admin_password", "role": "Admin"},
    "customer1": {"password": "customer1_password", "role": "Customer"},
    "cashier1": {"password": "cashier1_password", "role": "Cashier"}
}

def login():
    """
    Handles the user login process.
    """
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username]["password"] == password:
            print(f"Welcome, {username}! \nYou are logged in as {users[username]['role']}.")
            return users[username]["role"], username
        else:
            print("Invalid username or password. Please try again.")

def calculate_final_price():
    """
    Calculates the final price of a product after discounts and taxes.
    """
    try:
        subtotal = float(input("Enter the subtotal amount: $"))
    except ValueError:
        print("Invalid subtotal. Please enter a number.")
        return

    location = input("Enter your location (e.g., 'Uganda', 'Kenya', 'Other'): ")
    coupon_code = input("Enter coupon code (or leave blank): ")

    # Determine tax rate based on location
    if location.upper() == 'UGANDA':
        tax_rate = 0.18  # 18% tax for Uganda
    elif location.upper() == 'KENYA':
        tax_rate = 0.16  # 16% tax for Kenya
    else:
        tax_rate = 0.05  # 5% for other locations

    # Determine discount based on coupon code and subtotal
    discount_rate = 0
    if coupon_code == "SAVE10" and subtotal >= 50:
        discount_rate = 0.10  # 10% discount
    elif coupon_code == "SAVE20" and subtotal >= 100:
        discount_rate = 0.20  # 20% discount
    elif coupon_code:
        print("Invalid or expired coupon code.")

    # Calculate final price
    discount_amount = subtotal * discount_rate
    price_after_discount = subtotal - discount_amount
    tax_amount = price_after_discount * tax_rate
    final_price = price_after_discount + tax_amount

    print(f"\n--- Receipt ---")
    print(f"Subtotal: ${subtotal:.2f}")
    if discount_amount > 0:
        print(f"Discount ({int(discount_rate * 100)}%): -${discount_amount:.2f}")
    print(f"Tax ({int(tax_rate * 100)}%): +${tax_amount:.2f}")
    print(f"Final Price: ${final_price:.2f}")
    print(f"---------------")


def view_all_users():
    """
    Allows the admin to view all users and their roles.
    """
    print("\n--- All Users ---")
    for username, details in users.items():
        print(f"Username: {username}, Role: {details['role']}")
    print("-----------------\n")

# Main part of the program
if __name__ == "__main__":
    user_role, current_user = login()

    if user_role == "Admin":
        print("\nWelcome, Admin!")
        while True:
            print("Admin Menu:")
            print("1. Calculate Final Price")
            print("2. View All Users")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                calculate_final_price()
            elif choice == '2':
                view_all_users()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
    
    elif user_role == "Customer":
        print("\nWelcome, Customer!")
        calculate_final_price()
        
    elif user_role == "Cashier":
        print("\nWelcome, Cashier!")
        calculate_final_price()
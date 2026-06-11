#   ASSIGNMENT 1: Bill Split Calculator
#   Author:     Musiimenta Tendo Divine, 24/U/07405/PS
#   Description: Splits a restaurant bill
#                among people, including tip.

print("====================================")
print("      BILL SPLIT CALCULATOR")
print("====================================\n")

# ---- Step 1: Ask for inputs ----

# Ask for total bill amount
while True:
    try:
        bill_amount = float(input("Enter the total bill amount (UGX): "))
        if bill_amount <= 0:
            print("Please enter a positive amount.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a number.")

print("\nGreat! Now, let's get the number of people.")
# Ask for number of people
while True:
    try:
        num_people = int(input("Enter the number of people splitting the bill: "))
        if num_people <= 0:
            print("Please enter at least 1 person.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a whole number.")

print("\nAlmost done! Now for the tip.")

# Ask for tip percentage
print("\nChoose tip percentage:")
print("  1. 10%")
print("  2. 15%")
print("  3. 20%")
print("  4. Custom")

while True:
    tip_choice = input("Enter your choice (1/2/3/4): ")
    
    if tip_choice == "1":
        tip_percent = 10
        break
    elif tip_choice == "2":
        tip_percent = 15
        break
    elif tip_choice == "3":
        tip_percent = 20
        break
    elif tip_choice == "4":
        try:
            tip_percent = float(input("Enter your custom tip percentage: "))
            if tip_percent < 0:
                print("Tip cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a number.")
    else:
        print("Please choose 1, 2, 3, or 4.")

# ---- Step 2: Do the calculations ----

tip_amount = (tip_percent / 100) * bill_amount
total_bill = bill_amount + tip_amount
amount_per_person = total_bill / num_people

# ---- Step 3: Print the formatted receipt ----

print("\n====================================")
print("           RECEIPT SUMMARY")
print("====================================")
print(f"  Original Bill:      UGX {bill_amount:,.2f}")
print(f"  Tip ({tip_percent}%):          UGX {tip_amount:,.2f}")
print(f"  Total Bill:         UGX {total_bill:,.2f}")
print(f"  Number of People:   {num_people}")
print("------------------------------------")
print(f"  Each Person Pays:   UGX {amount_per_person:,.2f}")
print("====================================")
print("\nThank you! Enjoy your meal!")
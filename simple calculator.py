# Assignment: Menu-Driven Calculator

def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """This function divides two numbers"""
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def get_numbers():
    """Gets two numbers from the user and handles errors"""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def main():
    """Main function to run the calculator"""
    print("--- Simple Calculator ---")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice(1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            num1, num2 = get_numbers()

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
        
        elif choice == '5':
            print("Thank you for using the calculator!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

#Version 2: GUI Calculator using Tkinter
    # Assignment: Create a menu-driven(GUI) calculator
import tkinter as tk

# --- Functions for Calculator Logic ---

def on_button_click(char):
    """
    Appends the clicked character to the display entry.
    """
    display.insert(tk.END, char)

def clear_display():
    """
    Clears the entire display entry.
    """
    display.delete(0, tk.END)

def calculate_result():
    """
    Calculates the expression in the display and shows the result.
    Handles errors like division by zero or invalid syntax.
    """
    try:
        # Get the expression from the display
        expression = display.get()
        # Evaluate the expression and get the result
        result = eval(expression)
        # Clear the display before showing the result
        clear_display()
        # Insert the result into the display
        display.insert(0, str(result))
    except ZeroDivisionError:
        clear_display()
        display.insert(0, "Error: Div by 0")
    except Exception:
        clear_display()
        display.insert(0, "Error: Invalid")

# --- GUI Setup ---

# 1. Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400") # Set the size of the window
window.resizable(False, False) # Make the window not resizable
window.configure(bg="#f0f0f0") # Set a light grey background color

# 2. Create the display entry widget
display = tk.Entry(
    window, 
    width=14, 
    font=("Arial", 24), 
    borderwidth=2, 
    relief="solid",
    justify="right" # Align text to the right
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# 3. Define the button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# 4. Create and place the buttons on the grid
row_val = 1
col_val = 0
for button_text in buttons:
    if button_text == '=':
        # Create the '=' button with a different command
        tk.Button(
            window, 
            text=button_text, 
            width=5, 
            height=2,
            font=("Arial", 14),
            command=calculate_result
        ).grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        # Create all other buttons
        tk.Button(
            window, 
            text=button_text, 
            width=5, 
            height=2,
            font=("Arial", 14),
            command=lambda char=button_text: on_button_click(char)
        ).grid(row=row_val, column=col_val, padx=5, pady=5)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# 5. Create the 'Clear' button separately
clear_button = tk.Button(
    window, 
    text="C", 
    width=23, 
    height=2,
    font=("Arial", 14),
    command=clear_display
)
clear_button.grid(row=row_val, column=0, columnspan=4, padx=5, pady=5)

# 6. Start the main event loop
window.mainloop()
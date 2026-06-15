# Assignment 4: Create a menu-driven(GUI) calculator
import tkinter as tk

# --- Color Palette ---
WINDOW_BG = "#2a2d36"       # Dark blue-grey
DISPLAY_BG = "#1d1f26"      # Very dark blue-grey
BUTTON_BG = "#3b3e47"       # Lighter blue-grey
OPERATOR_BG = "#ff9f0a"     # Orange
TEXT_COLOR = "#ffffff"      # White
FONT_MAIN = ("Helvetica", 24)
FONT_BUTTONS = ("Helvetica", 14, "bold")

# --- Functions for Calculator Logic ---

def on_button_click(char):
    """Appends the clicked character to the display entry."""
    display.insert(tk.END, char)

def clear_display():
    """Clears the entire display entry."""
    display.delete(0, tk.END)

def calculate_result():
    """Calculates the expression in the display and shows the result."""
    try:
        expression = display.get()
        result = eval(expression)
        clear_display()
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
window.title("Modern Calculator")
window.geometry("320x480")
window.resizable(False, False)
window.configure(bg=WINDOW_BG)

# 2. Create the display entry widget
display = tk.Entry(
    window, 
    font=FONT_MAIN, 
    bg=DISPLAY_BG, 
    fg=TEXT_COLOR,
    borderwidth=0,
    relief="flat",
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, padx=20, pady=(20, 10), ipady=10)

# 3. Define the button layout
buttons = [
    ('Clear', 1, 0, 2), ('/', 1, 2, 1), ('*', 1, 3, 1),
    ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2, 1), ('-', 2, 3, 1),
    ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2, 1), ('+', 3, 3, 1),
    ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2, 1), ('=', 4, 3, 2),
    ('0', 5, 0, 2), ('.', 5, 2, 1)
]

# 4. Create and place the buttons on the grid
for (text, row, col, span) in buttons:
    # Determine button color
    if text in "/*-+=":
        bg_color = OPERATOR_BG
    else:
        bg_color = BUTTON_BG

    # Determine command
    if text == 'Clear':
        command = clear_display
    elif text == '=':
        command = calculate_result
    else:
        command = lambda char=text: on_button_click(char)

    # Create the button
    button = tk.Button(
        window,
        text=text,
        font=FONT_BUTTONS,
        bg=bg_color,
        fg=TEXT_COLOR,
        borderwidth=0,
        relief="flat",
        activebackground=bg_color,
        activeforeground=TEXT_COLOR,
        command=command
    )
    
    # Place the button on the grid
    button.grid(row=row, column=col, columnspan=span, sticky="nsew", padx=5, pady=5)

# 5. Configure grid weights to make buttons expand
for i in range(1, 6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# 6. Start the main event loop
window.mainloop()
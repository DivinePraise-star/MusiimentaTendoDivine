# Assignment 3: Real world application of loop control statements

# This program simulates a guessing game for the 2026 World Cup winner.
# It uses a while loop and loop control statements (break, continue, pass).

print("--- Guess the 2026 World Cup Winner! ---")
print("Enter 'quit' to exit the game at any time.")

# The secret winning country for our simulation
correct_country = "france"

while True:
    # Get user input
    guess = input("\nWhich country do you think will win? ")

    # Clean up the input by making it lowercase and removing whitespace
    cleaned_guess = guess.lower().strip()

    # --- Loop Control Statements ---

    # 1. Use 'continue' for empty input
    if not cleaned_guess:
        print("You didn't enter a country. Please try again.")
        continue

    # Allow the user to exit the game
    if cleaned_guess == 'quit':
        print("Thanks for playing!")
        break

    # 2. Use 'pass' for a specific, neutral case.
    # If the user guesses a strong team, we just 'pass' and let the loop continue
    # without giving a special hint.
    if cleaned_guess in ["spain", "brazil", "germany", "argentina"]:
        pass
    
    # 3. Use 'break' when the correct answer is guessed
    if cleaned_guess == correct_country:
        print(f"Wow, you guessed it! {correct_country.title()} will win the 2026 World Cup!")
        print("Congratulations on the correct prediction!")
        break
    else:
        # This block runs if the guess was wrong and wasn't a 'pass' case
        print(f"Not quite! {guess.title()} is a good team, but will not win in this World Cup of 2026.")

print("\n--- Game Over ---")

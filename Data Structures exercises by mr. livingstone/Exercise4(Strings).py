# Exercise 4: Strings

# 1. Concatenate an integer and a string.
print("--- Question 1 ---")
my_integer = 25
my_string = "My age is: "
# We must convert the integer to a string before concatenating.
concatenated_string = my_string + str(my_integer)
print(f"The integer is: {my_integer}")
print(f"The string is: '{my_string}'")
print(f"The concatenated result is: '{concatenated_string}'")
print("-" * 20)


# 2. Output the string without spaces at the beginning, in the middle, and at the end.
print("--- Question 2 ---")
txt = "      Hello,       Uganda!       "
print(f"Original string: '{txt}'")
# .strip() removes leading/trailing spaces. .replace() removes internal spaces.
cleaned_txt = txt.strip().replace(" ", "")
# A more robust way to handle multiple spaces in the middle:
words = txt.split()
cleaned_txt_robust = " ".join(words)
print(f"String with all spaces removed: '{cleaned_txt}'")
print(f"String with only middle spaces normalized: '{cleaned_txt_robust}'")
print("-" * 20)


# 3. Convert the value of ‘txt’ to uppercase.
print("--- Question 3 ---")
uppercase_txt = txt.upper()
print(f"Original string: '{txt}'")
print(f"Uppercase string: '{uppercase_txt}'")
print("-" * 20)


# 4. Replace character ‘U’ with ‘V’ in the string.
print("--- Question 4 ---")
replaced_txt = txt.replace('U', 'V')
print(f"Original string: '{txt}'")
print(f"String with 'U' replaced by 'V': '{replaced_txt}'")
print("-" * 20)


# 5. Return a range of characters in the 2nd, 3rd, and 4th position.
print("--- Question 5 ---")
y = "I am proudly Ugandan"
# Slicing from index 1 up to (but not including) index 4
substring = y[1:4]
print(f"The original string is: '{y}'")
print(f"The characters in the 2nd, 3rd, and 4th position are: '{substring}'")
print("-" * 20)


# 6. Correct the piece of code that will give an error.
print("--- Question 6 ---")
# Original problematic code: x = "All "Data Scientists" are cool!"
# To fix it, we can use single quotes for the outer string, or escape the inner double quotes.

# Solution 1: Using single quotes
x1 = 'All "Data Scientists" are cool!'
print(f"Corrected string (using single quotes): {x1}")

# Solution 2: Escaping the inner double quotes
x2 = "All \"Data Scientists\" are cool!"
print(f"Corrected string (using escaped quotes): {x2}")
print("-" * 20)

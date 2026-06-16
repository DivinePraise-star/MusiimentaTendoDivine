# Exercise 1: Lists

# 1. Create a list with 5 items (names of people) and output the 2nd item.
print("--- Question 1 ---")
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(f"The original list is: {names}")
print(f"The 2nd item is: {names[1]}")
print("-" * 20)


# 2. Change the value of the first item to a new value.
print("--- Question 2 ---")
print(f"Original first item: {names[0]}")
names[0] = "Alex"
print(f"The new first item is: {names[0]}")
print(f"The updated list is: {names}")
print("-" * 20)


# 3. Add a sixth item to the list.
print("--- Question 3 ---")
names.append("Frank")
print(f"A sixth item ('Frank') has been added.")
print(f"The updated list is: {names}")
print("-" * 20)


# 4. Add “Bathel” as the 3rd item in your list.
print("--- Question 4 ---")
# The insert() method takes the index and the value. Index 2 is the 3rd position.
names.insert(2, "Bathel")
print(f"'Bathel' has been added as the 3rd item.")
print(f"The updated list is: {names}")
print("-" * 20)


# 5. Remove the 4th item from the list.
print("--- Question 5 ---")
# The pop() method removes an item at a specific index. Index 3 is the 4th position.
removed_item = names.pop(3)
print(f"The 4th item ('{removed_item}') has been removed.")
print(f"The updated list is: {names}")
print("-" * 20)


# 6. Use negative indexing to print the last item in your list.
print("--- Question 6 ---")
last_item = names[-1]
print(f"The last item in the list is: {last_item}")
print("-" * 20)


# 7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th, and 5th items.
print("--- Question 7 ---")
new_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
# Slicing from index 2 up to (but not including) index 5
sub_list = new_list[2:5]
print(f"The new list is: {new_list}")
print(f"The 3rd, 4th, and 5th items are: {sub_list}")
print("-" * 20)


# 8. Write a list of countries and make a copy of it.
print("--- Question 8 ---")
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda"]
countries_copy = countries.copy()
print(f"Original list of countries: {countries}")
print(f"Copied list of countries: {countries_copy}")
print("-" * 20)


# 9. Loop through the list of countries.
print("--- Question 9 ---")
print("Looping through the list of countries:")
for country in countries:
    print(country)
print("-" * 20)


# 10. Write a list of animal names and sort them in both descending and ascending order.
print("--- Question 10 ---")
animals = ["Zebra", "Lion", "Elephant", "Antelope", "Giraffe"]
print(f"Original list of animals: {animals}")

# Ascending order
animals.sort()
print(f"Sorted in ascending order: {animals}")

# Descending order
animals.sort(reverse=True)
print(f"Sorted in descending order: {animals}")
print("-" * 20)


# 11. Using the list above, output only animal names with the letter ‘a’ in them.
print("--- Question 11 ---")
animals_with_a = []
for animal in animals:
    if 'a' in animal.lower(): # .lower() makes the check case-insensitive
        animals_with_a.append(animal)
print(f"Animals with the letter 'a': {animals_with_a}")
print("-" * 20)


# 12. Write two lists, one containing your first names and the other your second names. Join the two lists.
print("--- Question 12 ---")
first_names = ["Tendo", "Divine"]
second_names = ["Grace", "Musiimenta"]
full_names = first_names + second_names
print(f"First names: {first_names}")
print(f"Second names: {second_names}")
print(f"Joined list: {full_names}")
print("-" * 20)

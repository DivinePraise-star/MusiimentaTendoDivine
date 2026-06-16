# Exercise 3: Sets

# 1. Use the set() constructor to create a set of 3 of your favorite beverages.
print("--- Question 1 ---")
beverages = set(["Coffee", "Tea", "Water"])
print(f"My favorite beverages are: {beverages}")
print("-" * 20)


# 2. Use the correct method to add 2 more items to the beverages set.
print("--- Question 2 ---")
# The update() method is used to add multiple items to a set.
beverages.update(["Juice", "Soda"])
print(f"Two more beverages have been added.")
print(f"The updated set is: {beverages}")
print("-" * 20)


# 3. Check if "microwave" is present in the given set.
print("--- Question 3 ---")
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print(f"The set is: {mySet}")
if "microwave" in mySet:
    print("Yes, 'microwave' is present in the set.")
else:
    print("No, 'microwave' is not present in the set.")
print("-" * 20)


# 4. Remove “kettle” from the set above.
print("--- Question 4 ---")
# The remove() method will raise an error if the item is not found.
mySet.remove("kettle")
print(f"'kettle' has been removed.")
print(f"The updated set is: {mySet}")
print("-" * 20)


# 5. Loop through the set above.
print("--- Question 5 ---")
print("Looping through the items in the set:")
for item in mySet:
    print(item)
print("-" * 20)


# 6. Add elements from a list to a set.
print("--- Question 6 ---")
my_set = {1, 2, 3, 4}
my_list = [5, 6]
print(f"Original set: {my_set}")
print(f"List to add: {my_list}")
my_set.update(my_list)
print(f"Updated set after adding list elements: {my_set}")
print("-" * 20)


# 7. Join two sets, one containing ages and the other first names.
print("--- Question 7 ---")
ages = {25, 30, 35}
first_names = {"Alice", "Bob", "Charlie"}
# The union() method or the | operator can be used to join sets.
joined_set = ages.union(first_names)
print(f"Ages set: {ages}")
print(f"First names set: {first_names}")
print(f"Joined set: {joined_set}")
print("-" * 20)

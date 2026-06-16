# Exercise 5: Dictionaries

# 1. Print the value of the shoe size.
print("--- Question 1 ---")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
shoe_size = Shoes["size"]
print(f"The dictionary is: {Shoes}")
print(f"The shoe size is: {shoe_size}")
print("-" * 20)


# 2. Change the value “Nick” to “Adidas”.
print("--- Question 2 ---")
Shoes["brand"] = "Adidas"
print(f"The brand has been changed to 'Adidas'.")
print(f"The updated dictionary is: {Shoes}")
print("-" * 20)


# 3. Add a key/value pair "type": "sneakers".
print("--- Question 3 ---")
Shoes["type"] = "sneakers"
print(f"The key/value pair 'type': 'sneakers' has been added.")
print(f"The updated dictionary is: {Shoes}")
print("-" * 20)


# 4. Return a list of all the keys in the dictionary.
print("--- Question 4 ---")
keys_list = list(Shoes.keys())
print(f"The keys in the dictionary are: {keys_list}")
print("-" * 20)


# 5. Return a list of all the values in the dictionary.
print("--- Question 5 ---")
values_list = list(Shoes.values())
print(f"The values in the dictionary are: {values_list}")
print("-" * 20)


# 6. Check if the key “size” exists in the dictionary.
print("--- Question 6 ---")
if "size" in Shoes:
    print("Yes, the key 'size' exists in the dictionary.")
else:
    print("No, the key 'size' does not exist in the dictionary.")
print("-" * 20)


# 7. Loop through the dictionary.
print("--- Question 7 ---")
print("Looping through the dictionary items:")
for key, value in Shoes.items():
    print(f"  {key}: {value}")
print("-" * 20)


# 8. Remove “color” from the dictionary.
print("--- Question 8 ---")
Shoes.pop("color")
print(f"The key 'color' has been removed.")
print(f"The updated dictionary is: {Shoes}")
print("-" * 20)


# 9. Empty the dictionary.
print("--- Question 9 ---")
Shoes.clear()
print(f"The dictionary has been emptied.")
print(f"The dictionary is now: {Shoes}")
print("-" * 20)


# 10. Write a dictionary of your choice and make a copy of it.
print("--- Question 10 ---")
my_dict = {
    "course": "Data Science",
    "duration": "8 weeks",
    "institution": "Refactory"
}
my_dict_copy = my_dict.copy()
print(f"Original dictionary: {my_dict}")
print(f"Copied dictionary: {my_dict_copy}")
print("-" * 20)


# 11. Show nested dictionaries.
print("--- Question 11 ---")
# A nested dictionary is a dictionary within a dictionary.
students = {
    "student1": {
        "name": "Alice",
        "age": 24
    },
    "student2": {
        "name": "Bob",
        "age": 22
    }
}
print("Example of a nested dictionary:")
print(students)
# Accessing items in a nested dictionary
print(f"Student 1's name is: {students['student1']['name']}")
print("-" * 20)

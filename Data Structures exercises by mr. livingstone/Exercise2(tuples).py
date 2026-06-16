# Exercise 2: Tuples

# 1. Output your favorite phone brand from the tuple.
print("--- Question 1 ---")
x = ("samsung", "iphone", "tecno", "redmi")
# Let's say "samsung" is the favorite
favorite_phone = x[0]
print(f"The tuple is: {x}")
print(f"My favorite phone brand is: {favorite_phone}")
print("-" * 20)


# 2. Use negative indexing to print the 2nd last item.
print("--- Question 2 ---")
second_last_item = x[-2]
print(f"The 2nd last item is: {second_last_item}")
print("-" * 20)


# 3. Update “iphone” to “itel”.
print("--- Question 3 ---")
# Tuples are immutable, so we convert to a list, change it, and convert back.
phone_list = list(x)
phone_list[1] = "itel"
x = tuple(phone_list)
print(f"'iphone' has been updated to 'itel'.")
print(f"The updated tuple is: {x}")
print("-" * 20)


# 4. Add “Huawei” to the tuple.
print("--- Question 4 ---")
# Again, convert to a list to add an item.
phone_list = list(x)
phone_list.append("Huawei")
x = tuple(phone_list)
print(f"'Huawei' has been added.")
print(f"The updated tuple is: {x}")
print("-" * 20)


# 5. Loop through the tuple.
print("--- Question 5 ---")
print("Looping through the phone brands:")
for phone in x:
    print(phone)
print("-" * 20)


# 6. Remove/delete the first item in the tuple.
print("--- Question 6 ---")
# Convert to a list, remove the item, and convert back.
phone_list = list(x)
removed_item = phone_list.pop(0)
x = tuple(phone_list)
print(f"The first item ('{removed_item}') has been removed.")
print(f"The updated tuple is: {x}")
print("-" * 20)


# 7. Using the tuple() constructor, create a tuple of cities in Uganda.
print("--- Question 7 ---")
cities_list = ["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"]
cities_tuple = tuple(cities_list)
print(f"A tuple of cities in Uganda: {cities_tuple}")
print("-" * 20)


# 8. Unpack the tuple.
print("--- Question 8 ---")
# We can unpack the cities_tuple created above.
city1, city2, city3, city4, city5 = cities_tuple
print("Unpacking the tuple into variables:")
print(f"city1: {city1}")
print(f"city2: {city2}")
print(f"city3: {city3}")
# ...and so on.
print("-" * 20)


# 9. Use a range of indexes to print the 2nd, 3rd, and 4th cities.
print("--- Question 9 ---")
# Slicing from index 1 up to (but not including) index 4
sub_cities = cities_tuple[1:4]
print(f"The 2nd, 3rd, and 4th cities are: {sub_cities}")
print("-" * 20)


# 10. Join two tuples of first and second names.
print("--- Question 10 ---")
first_names = ("Divine", "Chris", "Patel")
second_names = ("Musiimenta", "Wabwire", "Kumar")
full_names = first_names + second_names
print(f"First names: {first_names}")
print(f"Second names: {second_names}")
print(f"Joined tuple: {full_names}")
print("-" * 20)


# 11. Create a tuple of colors and multiply it by 3.
print("--- Question 11 ---")
colors = ("Red", "Green", "Blue")
multiplied_colors = colors * 3
print(f"Original colors tuple: {colors}")
print(f"Multiplied by 3: {multiplied_colors}")
print("-" * 20)


# 12. Return the number of times 8 appears in the tuple.
print("--- Question 12 ---")
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_of_8 = thistuple.count(8)
print(f"The tuple is: {thistuple}")
print(f"The number 8 appears {count_of_8} times.")
print("-" * 20)

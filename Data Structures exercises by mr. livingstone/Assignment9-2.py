class Restaurant:
    """A class to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the restaurant's name and cuisine type."""
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

# Create three different instances from the class
restaurant1 = Restaurant("Pizza Palace", "Italian")
restaurant2 = Restaurant("Taco Town", "Mexican")
restaurant3 = Restaurant("Sushi Central", "Japanese")

# Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
print("-" * 20)
restaurant2.describe_restaurant()
print("-" * 20)
restaurant3.describe_restaurant()

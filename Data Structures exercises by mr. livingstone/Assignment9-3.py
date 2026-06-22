class User:
    """A class to model a user profile."""

    def __init__(self, first_name, last_name, age, location, email):
        """Initialize first_name, last_name, and other attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"User Profile for {self.first_name} {self.last_name}:")
        print(f"  - Age: {self.age}")
        print(f"  - Location: {self.location}")
        print(f"  - Email: {self.email}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back.")

# Create several instances representing different users
user1 = User("Tendo", "Divine", 30, "New York", "tendo.divine@email.com")
user2 = User("Jane", "Smith", 25, "London", "jane.smith@email.com")
user3 = User("Peter", "Jones", 42, "Sydney", "peter.jones@email.com")

# Call both methods for each user
user1.greet_user()
user1.describe_user()
print("-" * 20)

user2.greet_user()
user2.describe_user()
print("-" * 20)

user3.greet_user()
user3.describe_user()

import re

class ContactManager:
    """
    A class to manage a collection of contacts.
    """
    def __init__(self):
        """
        Initializes the ContactManager with an empty list of contacts.
        """
        self.contacts = []

    def _validate_phone(self, phone):
        """
        Validates a phone number.
        Allows digits, hyphens, and an optional leading '+'.
        """
        return all(c.isdigit() or c in ['-', '+'] for c in phone)

    def _validate_email(self, email):
        """
        Validates an email address.
        Checks for the presence of '@' and '.' characters.
        """
        if email:
            return '@' in email and '.' in email
        return True  # Email is optional

    def add_contact(self, name, phone, email=None):
        """
        Adds a new contact.
        Validates phone and email before adding.
        """
        if not self._validate_phone(phone):
            print("Error: Invalid phone number. Only digits and hyphens are allowed.")
            return False
        if not self._validate_email(email):
            print("Error: Invalid email address. Must contain '@' and '.'.")
            return False
        
        # Check for duplicate name or phone
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                print(f"Error: A contact with the name '{name}' already exists.")
                return False
            if contact['phone'] == phone:
                print(f"Error: A contact with the phone number '{phone}' already exists.")
                return False

        contact = {'name': name, 'phone': phone, 'email': email}
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully.")
        return True

    def list_all_contacts(self):
        """
        Lists all contacts in a user-friendly format.
        """
        if not self.contacts:
            print("No contacts found.")
            return

        print("\n--- All Contacts ---")
        for contact in self.contacts:
            email_str = contact['email'] if contact['email'] else 'N/A'
            print(f"  Name: {contact['name']}, Phone: {contact['phone']}, Email: {email_str}")
        print("--------------------\n")

    def search_contacts(self, query):
        """
        Searches for contacts by name, phone, or email.
        """
        results = [
            contact for contact in self.contacts
            if query.lower() in contact['name'].lower() or
               query in contact['phone'] or
               (contact['email'] and query.lower() in contact['email'].lower())
        ]

        if not results:
            print(f"No contacts found matching '{query}'.")
            return []

        print(f"\n--- Search Results for '{query}' ---")
        for contact in results:
            email_str = contact['email'] if contact['email'] else 'N/A'
            print(f"  Name: {contact['name']}, Phone: {contact['phone']}, Email: {email_str}")
        print("----------------------------------\n")
        return results
    
    def get_contact(self, name):
        """
        Retrieves a single contact by exact name.
        """
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                return contact
        return None

    def update_contact(self, name, new_phone=None, new_email=None):
        """
        Updates a contact's phone or email.
        """
        contact = self.get_contact(name)
        if not contact:
            print(f"Error: Contact '{name}' not found.")
            return False

        if new_phone:
            if not self._validate_phone(new_phone):
                print("Error: Invalid phone number. Only digits and hyphens are allowed.")
                return False
            contact['phone'] = new_phone
            print(f"Contact '{name}' phone number updated.")

        if new_email is not None: # Allow updating to an empty email
            if new_email and not self._validate_email(new_email):
                print("Error: Invalid email address. Must contain '@' and '.'.")
                return False
            contact['email'] = new_email
            print(f"Contact '{name}' email updated.")
        
        return True

    def delete_contact(self, name):
        """
        Deletes a contact by name.
        """
        contact = self.get_contact(name)
        if not contact:
            print(f"Error: Contact '{name}' not found.")
            return False
        
        self.contacts.remove(contact)
        print(f"Contact '{name}' deleted successfully.")
        return True

def main():
    """
    Main function to run the interactive CLI for the Contact Manager.
    """
    manager = ContactManager()

    while True:
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact Details")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone (+256-7...): ")
            email = input("Enter email (optional): ")
            manager.add_contact(name, phone, email or None)
        
        elif choice == '2':
            name = input("Enter the name of the contact to view: ")
            contact = manager.get_contact(name)
            if contact:
                print("\n--- Contact Details ---")
                email_str = contact['email'] if contact['email'] else 'N/A'
                print(f"  Name: {contact['name']}")
                print(f"  Phone: {contact['phone']}")
                print(f"  Email: {email_str}")
                print("-----------------------\n")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == '3':
            name = input("Enter the name of the contact to update: ")
            if manager.get_contact(name):
                new_phone = input("Enter new phone (leave blank to keep current): ")
                new_email = input("Enter new email (leave blank to keep current): ")
                manager.update_contact(name, new_phone or None, new_email or None)
            else:
                print(f"Contact '{name}' not found.")

        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)

        elif choice == '5':
            query = input("Enter name, phone, or email to search for: ")
            manager.search_contacts(query)

        elif choice == '6':
            manager.list_all_contacts()

        elif choice == '7':
            print("Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 7.")

if __name__ == "__main__":
    main()

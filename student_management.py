import csv
import json
import logging
import pathlib

# Configure logging
logging.basicConfig(
    filename='student_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Custom Exceptions
class StudentManagementError(Exception):
    """Base class for exceptions in this module."""
    pass

class StudentNotFoundError(StudentManagementError):
    """Exception raised when a student is not found."""
    def __init__(self, reg_no):
        self.reg_no = reg_no
        self.message = f"Student with Registration Number '{reg_no}' not found."
        super().__init__(self.message)

class DuplicateStudentError(StudentManagementError):
    """Exception raised when adding a student that already exists."""
    def __init__(self, reg_no):
        self.reg_no = reg_no
        self.message = f"Student with Registration Number '{reg_no}' already exists."
        super().__init__(self.message)

class StudentManagementSystem:
    def __init__(self, csv_file='students.csv', json_file='students.json'):
        self.csv_file = csv_file
        self.json_file = json_file
        self._initialize_files()

    def _initialize_files(self):
        """Creates the files if they do not exist."""
        if not pathlib.Path(self.csv_file).exists():
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['reg_no', 'name', 'dateofbirth', 'address', 'contact', 'program', 'year_of_study'])
            logging.info(f"Initialized new CSV file: {self.csv_file}")

        if not pathlib.Path(self.json_file).exists():
            with open(self.json_file, mode='w') as file:
                json.dump({}, file)
            logging.info(f"Initialized new JSON file: {self.json_file}")

    def _read_csv(self):
        students = []
        try:
            with open(self.csv_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(row)
        except Exception as e:
            logging.error(f"Error reading CSV: {e}")
            print(f"Error reading CSV: {e}")
        return students

    def _write_csv(self, students):
        try:
            with open(self.csv_file, mode='w', newline='') as file:
                fieldnames = ['reg_no', 'name', 'dateofbirth', 'address', 'contact', 'program', 'year_of_study']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(students)
        except Exception as e:
            logging.error(f"Error writing to CSV: {e}")
            print(f"Error writing to CSV: {e}")

    def _read_json(self):
        try:
            with open(self.json_file, mode='r') as file:
                return json.load(file)
        except Exception as e:
            logging.error(f"Error reading JSON: {e}")
            return {}

    def _write_json(self, data):
        try:
            with open(self.json_file, mode='w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            logging.error(f"Error writing to JSON: {e}")

    def add_student(self, reg_no, name, dateofbirth, address, contact, program, year_of_study):
        students = self._read_csv()
        if any(s['reg_no'] == reg_no for s in students):
            logging.warning(f"Failed to add student: Registration number {reg_no} already exists.")
            raise DuplicateStudentError(reg_no)

        # Add to CSV
        students.append({'reg_no': reg_no, 'name': name, 'dateofbirth': dateofbirth,'address': address,'contact': contact, 'program': program, 'year_of_study': year_of_study})
        self._write_csv(students)

        # Add to JSON
        json_data = self._read_json()
        json_data[reg_no] = {
            'address': address,
            'contact': contact,
            'program': program,
            'year_of_study': year_of_study
        }
        self._write_json(json_data)
        
        logging.info(f"Added student: {reg_no} - {name}")
        print(f"Student {name} added successfully!")

    def view_all_students(self):
        students = self._read_csv()
        json_data = self._read_json()
        
        if not students:
            print("No student records found.")
            return

        print("\n--- STUDENT RECORDS ---")
        print(f"{'Reg No':<10} | {'Name':<20} | {'Program':<20} | {'Contact':<15} | {'Year of Study':<15}")
        print("-" * 100)
        for s in students:
            extra = json_data.get(s['reg_no'], {})
            contact = extra.get('contact', 'N/A')
            program = extra.get('program', 'N/A')
            year_of_study = extra.get('year_of_study', 'N/A')
            print(f"{s['reg_no']:<10} | {s['name']:<20} | {program:<20} | {contact:<15} | {year_of_study:<15}")
        logging.info("Viewed all student records.")

    def search_student(self, reg_no):
        students = self._read_csv()
        student = next((s for s in students if s['reg_no'] == reg_no), None)
        
        if not student:
            logging.warning(f"Search failed: Student {reg_no} not found.")
            raise StudentNotFoundError(reg_no)

        json_data = self._read_json()
        extra = json_data.get(reg_no, {})

        print("\n--- Student Details ---")
        print(f"Registration No: {student['reg_no']}")
        print(f"Name:            {student['name']}")
        print(f"Date of Birth:   {student['dateofbirth']}")
        print(f"Address:         {extra.get('address', 'N/A')}")
        print(f"Contact:         {extra.get('contact', 'N/A')}")
        print(f"Program:         {extra.get('program', 'N/A')}")
        print(f"Year of Study:   {extra.get('year_of_study', 'N/A')}")
        logging.info(f"Searched for student: {reg_no}")

    def update_student(self, reg_no):
        students = self._read_csv()
        index = next((i for i, s in enumerate(students) if s['reg_no'] == reg_no), None)

        if index is None:
            logging.warning(f"Update failed: Student {reg_no} not found.")
            raise StudentNotFoundError(reg_no)

        print(f"Updating records for student {reg_no}. Leave blank to keep current value.")
        
        # CSV details
        name = input(f"Enter new name ({students[index]['name']}): ") or students[index]['name']
        dateofbirth = input(f"Enter new date of birth ({students[index]['dateofbirth']}): ") or students[index]['dateofbirth']
        address = input(f"Enter new address ({students[index].get('address', '')}): ") or students[index].get('address', '')
        contact = input(f"Enter new contact ({students[index].get('contact', '')}): ") or students[index].get('contact', '')
        program = input(f"Enter new program ({students[index].get('program', '')}): ") or students[index].get('program', '')
        year_of_study = input(f"Enter new year of study ({students[index].get('year_of_study', '')}): ") or students[index].get('year_of_study', '')
        
        students[index] = {'reg_no': reg_no, 'name': name, 'dateofbirth': dateofbirth,'address': address,'contact': contact, 'program': program, 'year_of_study': year_of_study}
        self._write_csv(students)

        # JSON details
        json_data = self._read_json()
        extra = json_data.get(reg_no, {})

        dateofbirth = input(f"Enter new date of birth ({extra.get('dateofbirth', '')}): ") or extra.get('dateofbirth', '')
        address = input(f"Enter new address ({extra.get('address', '')}): ") or extra.get('address', '')
        contact = input(f"Enter new contact ({extra.get('contact', '')}): ") or extra.get('contact', '')
        program = input(f"Enter new program ({extra.get('program', '')}): ") or extra.get('program', '')
        year_of_study = input(f"Enter new year of study ({extra.get('year_of_study', '')}): ") or extra.get('year_of_study', '')

        json_data[reg_no] = {
            "name": name,
            "dateofbirth": dateofbirth,
            "address": address,
            "contact": contact,
            "program": program,
            "year_of_study": year_of_study
        }
        self._write_json(json_data)
        
        logging.info(f"Updated student: {reg_no}")
        print(f"Student {reg_no} updated successfully!")

    def delete_student(self, reg_no):
        students = self._read_csv()
        new_students = [s for s in students if s['reg_no'] != reg_no]

        if len(students) == len(new_students):
            logging.warning(f"Delete failed: Student {reg_no} not found.")
            raise StudentNotFoundError(reg_no)

        self._write_csv(new_students)

        json_data = self._read_json()
        if reg_no in json_data:
            del json_data[reg_no]
            self._write_json(json_data)

        logging.info(f"Deleted student: {reg_no}")
        print(f"Student {reg_no} deleted successfully!")

def main():
    system = StudentManagementSystem()
    
    while True:
        print("\n=== STUDENTS RECORD MANAGEMENT SYSTEM ===")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by Reg No")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        try:
            if choice == '1':
                reg_no = input("Enter Registration Number: ").strip()
                if not reg_no: raise ValueError("Registration number cannot be empty.")
                name = input("Enter Name: ").strip()
                dateofbirth = input("Enter Date of Birth: ").strip()
                address = input("Enter Address: ").strip()
                contact = input("Enter Contact: ").strip()
                program = input("Enter Program: ").strip()
                year_of_study = input("Enter Year of Study: ").strip()
                system.add_student(reg_no, name, dateofbirth, address, contact, program, year_of_study)

            elif choice == '2':
                system.view_all_students()

            elif choice == '3':
                reg_no = input("Enter Registration Number to search: ").strip()
                system.search_student(reg_no)

            elif choice == '4':
                reg_no = input("Enter Registration Number to update: ").strip()
                system.update_student(reg_no)

            elif choice == '5':
                reg_no = input("Enter Registration Number to delete: ").strip()
                confirm = input(f"Are you sure you want to delete student {reg_no}? (y/n): ").lower()
                if confirm == 'y':
                    system.delete_student(reg_no)
                else:
                    print("Deletion cancelled.")

            elif choice == '6':
                print("Exiting system. Goodbye!")
                logging.info("System closed by user.")
                break

            else:
                print("Invalid choice. Please try again.")

        except StudentManagementError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Input Error: {e}")
            logging.error(f"Input error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            logging.critical(f"Unexpected error: {e}", exc_info=True)
        finally:
            print("\n Returning to main menu...")
            print("-" * 100)
            pass

if __name__ == "__main__":
    main()

import json
from datetime import datetime, timedelta

# Dictionary to hold contacts
contacts = {}

# Function to load contacts from a file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Function to save contacts to a file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# Function to add a contact
def add_contact():
    name = input("Enter contact name: ")
    if name in contacts:
        print("Contact already exists.")
    else:
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        shop_name = input("Enter shop name: ")
        state = input("Enter state: ")
        city = input("Enter city: ")
        landmark = input("Enter landmark: ")
        aadhaar = input("Enter Aadhaar card number: ")
        age = input("Enter age: ")
        dob = input("Enter date of birth (DD/MM/YYYY): ")
        gender = input("Enter gender: ")
        hobbies = input("Enter hobbies (comma-separated): ")

        contacts[name] = {
            'Phone': phone,
            'Email': email,
            'Address': address,
            'Shop Name': shop_name,
            'State': state,
            'City': city,
            'Landmark': landmark,
            'Aadhaar': aadhaar,
            'Age': age,
            'Date of Birth': dob,
            'Gender': gender,
            'Hobbies': hobbies.split(','),  # Convert hobbies into a list
            'Added On': datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Store the date added
        }
        print(f"Contact {name} added successfully.")
        save_contacts()  # Save contacts after adding

# Function to view a contact
def view_contact():
    name = input("Enter contact name to view: ")
    if name in contacts:
        print(f"Name: {name}")
        for key, value in contacts[name].items():
            print(f"{key}: {value}")
    else:
        print("Contact not found.")

# Function to update a contact
def update_contact():
    name = input("Enter contact name to update: ")
    if name in contacts:
        print("1. Update Phone")
        print("2. Update Email")
        print("3. Update Address")
        print("4. Update Shop Name")
        print("5. Update State")
        print("6. Update City")
        print("7. Update Landmark")
        print("8. Update Aadhaar Card Number")
        print("9. Update Age")
        print("10. Update Date of Birth")
        print("11. Update Gender")
        print("12. Update Hobbies")
        choice = input("Enter choice (1-12): ")

        if choice == '1':
            contacts[name]['Phone'] = input("Enter new phone number: ")
        elif choice == '2':
            contacts[name]['Email'] = input("Enter new email address: ")
        elif choice == '3':
            contacts[name]['Address'] = input("Enter new address: ")
        elif choice == '4':
            contacts[name]['Shop Name'] = input("Enter new shop name: ")
        elif choice == '5':
            contacts[name]['State'] = input("Enter new state: ")
        elif choice == '6':
            contacts[name]['City'] = input("Enter new city: ")
        elif choice == '7':
            contacts[name]['Landmark'] = input("Enter new landmark: ")
        elif choice == '8':
            contacts[name]['Aadhaar'] = input("Enter new Aadhaar card number: ")
        elif choice == '9':
            contacts[name]['Age'] = input("Enter new age: ")
        elif choice == '10':
            contacts[name]['Date of Birth'] = input("Enter new date of birth (DD/MM/YYYY): ")
        elif choice == '11':
            contacts[name]['Gender'] = input("Enter new gender: ")
        elif choice == '12':
            hobbies = input("Enter new hobbies (comma-separated): ")
            contacts[name]['Hobbies'] = hobbies.split(',')
        else:
            print("Invalid choice.")
        
        print(f"Contact {name} updated.")
        save_contacts()  # Save contacts after updating
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
        save_contacts()  # Save contacts after deletion
    else:
        print("Contact not found.")

# Function to list all contacts in a more readable format
def list_contacts():
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}")
            for key, value in info.items():
                print(f"{key}: {value}")
            print("---------------------------------------------------")
    else:
        print("No contacts found.")

# Function to count all contacts
def count_contacts():
    print(f"Total number of contacts: {len(contacts)}")

# Function to view contacts added in the last year
def view_recent_contacts():
    one_year_ago = datetime.now() - timedelta(days=365)
    recent_contacts = {name: info for name, info in contacts.items() 
                       if datetime.strptime(info['Added On'], "%Y-%m-%d %H:%M:%S") >= one_year_ago}
    
    if recent_contacts:
        print("Contacts added in the last year:")
        for name, info in recent_contacts.items():
            print(f"Name: {name}, Added On: {info['Added On']}")
    else:
        print("No contacts added in the last year.")

# Menu-driven program
def contact_book():
    global contacts
    contacts = load_contacts()  # Load contacts from the file at the start

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List All Contacts")
        print("6. Count Contacts")
        print("7. View Recent Contacts (Last Year)")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            list_contacts()
        elif choice == '6':
            count_contacts()
        elif choice == '7':
            view_recent_contacts()
        elif choice == '8':
            print("Exiting contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact book program directly
contact_book()
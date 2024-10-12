import pandas as pd
from datetime import datetime, timedelta

# Define the files where we will save the data
csv_file_path = "order_data.csv"
excel_file_path = "order_data.xlsx"

# Function to create a new order
def create_order():
    # Get input from the user
    order_data = {
        "Order Date": [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
        "Company Name": [input("Enter Company Name: ")],
        "Shop Name": [input("Enter Shop Name: ")],
        "Receiver Name": [input("Enter Receiver Name: ")],
        "Email": [input("Enter Email: ")],
        "Phone Number": [input("Enter Phone Number: ")],
        "Product Name": [input("Enter Product Name: ")],
        "Product Quantity": [input("Enter Product Quantity: ")],
        "Billing Address": [input("Enter Billing Address: ")],
        "Landmark": [input("Enter Landmark: ")],
        "City": [input("Enter City: ")],
        "Pincode": [input("Enter Pincode: ")],
        "Country": [input("Enter Country: ")],
        "Comments": [input("Enter Comments (if any): ")],
        "Region": [input("Enter Region: ")],
    }
    
    # Create a DataFrame for the new order
    new_order_df = pd.DataFrame(order_data)

    # Construct a string representation with new lines
    formatted_order = new_order_df.to_string(index=False, header=False, justify='left')
    
    # Save the new order to the CSV file
    with open(csv_file_path, 'a') as f:
        f.write(formatted_order + '\n\n')  # Add an extra newline for separation
    
    # Save to Excel file
    if not pd.io.common.file_exists(excel_file_path):
        new_order_df.to_excel(excel_file_path, index=False, engine='openpyxl')
    else:
        with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            new_order_df.to_excel(writer, index=False, header=False)

    print("Order saved successfully!")

# Function to fetch orders from the past year
def get_orders_from_past_year():
    try:
        # Read the existing data from the CSV file
        data = pd.read_csv(csv_file_path, header=None)
        data.columns = ["Order Data"]  # Set the column name
    except FileNotFoundError:
        print("No orders found. Please add an order first.")
        return

    # Get the current date
    current_date = datetime.now()
    
    # Filter orders from the past year
    past_year_orders = []
    for index, row in data.iterrows():
        order_date_str = row["Order Data"].split('\n')[0]  # Get the first line as the order date
        order_date = pd.to_datetime(order_date_str)
        if order_date >= current_date - timedelta(days=365):
            past_year_orders.append(row["Order Data"])

    if not past_year_orders:
        print("No orders were placed in the past year.")
    else:
        print("Orders from the past year:")
        for order in past_year_orders:
            print(order)
            print()  # Print an extra line for better readability

# Function to update an existing order
def update_order():
    try:
        data = pd.read_csv(csv_file_path, header=None)
        data.columns = ["Order Data"]  # Set the column name
    except FileNotFoundError:
        print("No orders found. Please add an order first.")
        return

    print("\nCurrent orders:")
    for index, row in data.iterrows():
        print(f"{index}:")
        print(row["Order Data"])
        print()  # Print an extra line for better readability

    index = int(input("Enter the index of the order to update (starting from 0): "))
    if index < 0 or index >= len(data):
        print("Invalid index. Please try again.")
        return

    # Split the order data into lines for easier access
    order_lines = data.at[index, 'Order Data'].split('\n')

    # Update the fields with new values
    new_company_name = input(f"Enter new Company Name (current: {order_lines[1]}): ") or order_lines[1]
    new_shop_name = input(f"Enter new Shop Name (current: {order_lines[2]}): ") or order_lines[2]
    new_receiver_name = input(f"Enter new Receiver Name (current: {order_lines[3]}): ") or order_lines[3]
    new_email = input(f"Enter new Email (current: {order_lines[4]}): ") or order_lines[4]
    new_phone_number = input(f"Enter new Phone Number (current: {order_lines[5]}): ") or order_lines[5]
    new_product_name = input(f"Enter new Product Name (current: {order_lines[6]}): ") or order_lines[6]
    new_product_quantity = input(f"Enter new Product Quantity (current: {order_lines[7]}): ") or order_lines[7]
    new_billing_address = input(f"Enter new Billing Address (current: {order_lines[8]}): ") or order_lines[8]
    new_landmark = input(f"Enter new Landmark (current: {order_lines[9]}): ") or order_lines[9]
    new_city = input(f"Enter new City (current: {order_lines[10]}): ") or order_lines[10]
    new_pincode = input(f"Enter new Pincode (current: {order_lines[11]}): ") or order_lines[11]
    new_country = input(f"Enter new Country (current: {order_lines[12]}): ") or order_lines[12]
    new_comments = input(f"Enter new Comments (if any) (current: {order_lines[13]}): ") or order_lines[13]
    new_region = input(f"Enter new Region (current: {order_lines[14]}): ") or order_lines[14]

    # Construct the updated order string
    updated_order = f"{order_lines[0]}\n{new_company_name}\n{new_shop_name}\n{new_receiver_name}\n{new_email}\n{new_phone_number}\n{new_product_name}\n{new_product_quantity}\n{new_billing_address}\n{new_landmark}\n{new_city}\n{new_pincode}\n{new_country}\n{new_comments}\n{new_region}"

    # Update the DataFrame
    data.at[index, 'Order Data'] = updated_order

    # Save the updated DataFrame to the CSV file
    data.to_csv(csv_file_path, index=False, header=False)

    # Save to Excel file
    with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        data.to_excel(writer, index=False, header=False)

    print("Order updated successfully!")

# Function to delete an existing order
def delete_order():
    try:
        data = pd.read_csv(csv_file_path, header=None)
        data.columns = ["Order Data"]  # Set the column name
    except FileNotFoundError:
        print("No orders found. Please add an order first.")
        return

    print("\nCurrent orders:")
    for index, row in data.iterrows():
        print(f"{index}:")
        print(row["Order Data"])
        print()  # Print an extra line for better readability

    index = int(input("Enter the index of the order to delete (starting from 0): "))
    if index < 0 or index >= len(data):
        print("Invalid index. Please try again.")
        return

    # Delete the specified order
    data = data.drop(index).reset_index(drop=True)

    # Save the updated DataFrame to the CSV file
    data.to_csv(csv_file_path, index=False, header=False)

    # Save to Excel file
    data.to_excel(excel_file_path, index=False, header=False, engine='openpyxl')

    print("Order deleted successfully!")

# Main function to run the booking system
def main():
    while True:
        print("\n--- Online Booking System ---")
        print("1. Create a new order")
        print("2. View orders from the past year")
        print("3. Update an existing order")
        print("4. Delete an existing order")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_order()
        elif choice == '2':
            get_orders_from_past_year()
        elif choice == '3':
            update_order()
        elif choice == '4':
            delete_order()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main function directly
main()
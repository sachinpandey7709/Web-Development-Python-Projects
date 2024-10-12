import pandas as pd
from datetime import datetime, timedelta

# File where orders will be saved
ORDER_FILE = 'cafe_orders.csv'
EXCEL_FILE = 'cafe_orders.xlsx'

# Sample cafe menu
cafe_menu = {
    'Coffee': 50,
    'Tea': 30,
    'Sandwich': 80,
    'Cake': 100,
    'Muffin': 60,
    'Pastry': 90,
    'Smoothie': 120
}

# Function to display the menu
def display_menu():
    print("\nAvailable items and prices (per item):")
    for item, price in cafe_menu.items():
        print(f"{item}: {price} Rs")

# Function to create a new order
def create_order():
    order_items = []
    total_price = 0

    display_menu()
    
    while True:
        item = input("\nEnter the item you want to order (or type 'done' to finish): ").title()
        if item == 'Done':
            break
        if item in cafe_menu:
            quantity = int(input(f"Enter quantity for {item}: "))
            item_total = cafe_menu[item] * quantity
            total_price += item_total
            order_items.append({'Item': item, 'Quantity': quantity, 'Price': item_total})
            print(f"{item} added. Item Total: {item_total} Rs")
        else:
            print(f"Sorry, {item} is not on the menu.")

    if not order_items:
        print("No items ordered.")
        return
    
    order_id = datetime.now().strftime('%Y%m%d%H%M%S')
    order_date = datetime.now()

    for order in order_items:
        order['Order ID'] = order_id
        order['Order Date'] = order_date

    print(f"\nOrder successfully created. Total amount to be paid: {total_price} Rs.")

    # Save the order to the CSV file
    save_order_to_csv(order_items)

# Function to save the order to a CSV file
def save_order_to_csv(order_items):
    try:
        # Check if the file already exists
        df = pd.read_csv(ORDER_FILE)
    except FileNotFoundError:
        # If the file doesn't exist, create a new dataframe
        df = pd.DataFrame()

    new_orders_df = pd.DataFrame(order_items)
    df = pd.concat([df, new_orders_df], ignore_index=True)

    df.to_csv(ORDER_FILE, index=False)
    print(f"Order saved to {ORDER_FILE}.")

# Function to view all orders
def view_orders():
    try:
        df = pd.read_csv(ORDER_FILE)
        if df.empty:
            print("No orders found.")
        else:
            print(df)
    except FileNotFoundError:
        print("No orders found. Please create an order first.")

# Function to view orders from the last year
def view_orders_from_last_year():
    try:
        df = pd.read_csv(ORDER_FILE)
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        one_year_ago = datetime.now() - timedelta(days=365)
        last_year_orders = df[df['Order Date'] >= one_year_ago]

        if last_year_orders.empty:
            print("No orders found from the last year.")
        else:
            print("Orders from the last year:")
            print(last_year_orders)
    except FileNotFoundError:
        print("No orders found.")

# Function to export orders to Excel
def export_to_excel():
    try:
        df = pd.read_csv(ORDER_FILE)
        df.to_excel(EXCEL_FILE, index=False)
        print(f"Orders exported to {EXCEL_FILE}.")
    except FileNotFoundError:
        print("No orders found. Please create an order first.")

# Function to count total number of orders
def count_total_orders():
    try:
        df = pd.read_csv(ORDER_FILE)
        total_orders = df['Order ID'].nunique()
        print(f"Total number of orders: {total_orders}")
    except FileNotFoundError:
        print("No orders found.")

# Main menu-driven program
def cafe_management_system():
    while True:
        print("\nCafe Management Menu:")
        print("1. Create New Order")
        print("2. View All Orders")
        print("3. View Orders from Last Year")
        print("4. Export Orders to Excel")
        print("5. Total Number of Orders")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_order()
        elif choice == '2':
            view_orders()
        elif choice == '3':
            view_orders_from_last_year()
        elif choice == '4':
            export_to_excel()
        elif choice == '5':
            count_total_orders()
        elif choice == '6':
            print("Exiting Cafe Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the cafe management system
cafe_management_system()
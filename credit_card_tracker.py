import json
import os

# Path to store credit card data
FILE_PATH = 'credit_cards.json'

# Load existing data if file exists
def load_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

# Save data to file
def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

# Create a new credit card entry
def create_card():
    name = input("Enter the card name: ")
    number = input("Enter the card number: ")
    expiry_date = input("Enter the expiry date (MM/YY): ")
    cvv = input("Enter the CVV: ")

    card = {
        'name': name,
        'number': number,
        'expiry_date': expiry_date,
        'cvv': cvv
    }

    data = load_data()
    data.append(card)
    save_data(data)
    print(f"Credit card '{name}' added successfully.")

# Read (view) all credit cards
def view_cards():
    data = load_data()
    if not data:
        print("No credit cards found.")
        return
    for idx, card in enumerate(data, start=1):
        print(f"\nCard {idx}:")
        print(f"  Name: {card['name']}")
        print(f"  Number: {card['number']}")
        print(f"  Expiry Date: {card['expiry_date']}")
        print(f"  CVV: {card['cvv']}")

# Update an existing credit card
def update_card():
    data = load_data()
    if not data:
        print("No credit cards to update.")
        return
    view_cards()

    try:
        card_index = int(input("\nEnter the card number to update: ")) - 1
        if card_index < 0 or card_index >= len(data):
            print("Invalid card number.")
            return
    except ValueError:
        print("Invalid input.")
        return

    card = data[card_index]
    print(f"Updating card: {card['name']}")

    name = input(f"Enter the new name (current: {card['name']}): ")
    number = input(f"Enter the new card number (current: {card['number']}): ")
    expiry_date = input(f"Enter the new expiry date (current: {card['expiry_date']}): ")
    cvv = input(f"Enter the new CVV (current: {card['cvv']}): ")

    card['name'] = name or card['name']
    card['number'] = number or card['number']
    card['expiry_date'] = expiry_date or card['expiry_date']
    card['cvv'] = cvv or card['cvv']

    save_data(data)
    print(f"Card '{card['name']}' updated successfully.")

# Delete an existing credit card
def delete_card():
    data = load_data()
    if not data:
        print("No credit cards to delete.")
        return
    view_cards()

    try:
        card_index = int(input("\nEnter the card number to delete: ")) - 1
        if card_index < 0 or card_index >= len(data):
            print("Invalid card number.")
            return
    except ValueError:
        print("Invalid input.")
        return

    card = data.pop(card_index)
    save_data(data)
    print(f"Card '{card['name']}' deleted successfully.")

# Main function to show the menu and handle user input
def menu():
    while True:
        print("\n--- Credit Card Tracker ---")
        print("1. Create a new credit card")
        print("2. View all credit cards")
        print("3. Update a credit card")
        print("4. Delete a credit card")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_card()
        elif choice == '2':
            view_cards()
        elif choice == '3':
            update_card()
        elif choice == '4':
            delete_card()
        elif choice == '5':
            print("Exiting the Credit Card Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == '__main__':
    menu()

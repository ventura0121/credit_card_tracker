import json
import os
from utils import load_data, save_data

# File path for storing credit card data
FILE_PATH = 'data/credit_cards.json'

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

    confirmation = input("Are you sure you want to delete this card? This action cannot be undone. (y/n): ")
    if confirmation.lower() == 'y':
        card = data.pop(card_index)
        save_data(data)
        print(f"Card '{card['name']}' deleted successfully.")
    else:
        print("Deletion canceled.")

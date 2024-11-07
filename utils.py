import json
import os

FILE_PATH = 'data/credit_cards.json'

def load_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def explain_features():
    print("1. Create a new credit card - Add a new card to keep track of all your cards in one place.")
    print("2. View all credit cards - See details of all stored cards for easy access.")
    print("3. Update a credit card - Modify card details when they change, keeping your records accurate.")
    print("4. Delete a credit card - Remove old or unused cards to keep your list manageable.")

def show_costs(action):
    if action == "create":
        print("Note: Adding a new card will store sensitive data locally. Please be mindful.")
    elif action == "update":
        print("Note: Updating a card will permanently modify its information. Double-check for accuracy.")
    elif action == "delete":
        print("Warning: Deleting a card is irreversible and will remove it from your records.")
    else:
        print("Invalid action. Please choose 'create', 'update', or 'delete'.")

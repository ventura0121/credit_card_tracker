from card_manager import create_card, view_cards, update_card, delete_card
from utils import explain_features, show_costs

def menu():
    while True:
        print("\n--- Credit Card Tracker ---")
        explain_features()
        print("5. Exit - Quit the application safely")

        choice = input("Enter your choice (or type '?' for more information): ")

        if choice == '?':
            print("This application allows you to manage your credit cards efficiently.")
            continue

        if choice == '1':
            show_costs("create")
            create_card()
        elif choice == '2':
            view_cards()
        elif choice == '3':
            show_costs("update")
            update_card()
        elif choice == '4':
            show_costs("delete")
            delete_card()
        elif choice == '5':
            print("Exiting the Credit Card Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()

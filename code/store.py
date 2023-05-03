import login
import logout
import create_account
import delete_account
import search
import add_to_cart
import remove_from_cart
import view_cart
import checkout
import add_to_order_history
import view_order_history
import edit_shipping
import edit_payment


def main():
    # Start by prompting the user to login or create an account
    print("Welcome to our e-commerce store!")
    print("Please choose an option:")
    print("1. Login")
    print("2. Create Account")
    print("3. Quit")

    choice = input("> ")

    if choice == "1":
        if login.login():
            print("Login successful!")
            # User is logged in, show them the main menu
            show_main_menu()
        else:
            print("Invalid username or password.")

    elif choice == "2":
        # Prompt user to create a new account
        create_account.create_account()
        show_main_menu()

    elif choice == "3":
        # Quit the program
        print("Goodbye!")
        return

    else:
        # Invalid choice
        print("Invalid choice.")
        return


def show_main_menu():
    # Show main menu options to the user
    while True:
        print("\nWhat would you like to do?")
        print("1. View Items in a Category")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. View Order History")
        print("7. Edit Shipping Information")
        print("8. Edit Payment Information")
        print("9. Delete Account")
        print("10. Logout")

        choice = input("> ")

        if choice == "1":
            view_items_in_category.show_categories()

        elif choice == "2":
            add_to_cart.add_to_cart()

        elif choice == "3":
            remove_from_cart.remove_from_cart()

        elif choice == "4":
            view_cart.view_cart()

        elif choice == "5":
            checkout.checkout()

        elif choice == "6":
            view_order_history.view_order_history()

        elif choice == "7":
            edit_shipping_info.edit_shipping_info()

        elif choice == "8":
            edit_payment_info.edit_payment_info()

        elif choice == "9":
            delete_account.delete_account()

        elif choice == "10":
            logout.logout()
            # After logout, return to the login menu
            main()

        else:
            # Invalid choice
            print("Invalid choice.")


if __name__ == "__main__":
    main()

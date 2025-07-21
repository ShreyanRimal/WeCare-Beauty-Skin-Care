# Importing necessary modules
from datetime import date  # This might be used inside Operation module
import Operation  # Custom module where product-related functions are defined

# Displaying header for the application
print("\t\t\t\tWeCare Beauty & Skin Care")
print("\t\tKamaladi, Kathmandu | Phone No. 9800000000")
print("_______________________________________________________________________________")
print("\tWelcome to WeCare! Your skin deserves the best.")
print("_______________________________________________________________________________\n")

# Setting a loop variable to control the menu
loop = True

# Starting the menu loop
while loop:
    # Displaying the menu options
    print("Choose an option:")
    print("1. Display Available Products")  # Option to show current product list
    print("2. Sell Products")               # Option to sell product(s)
    print("3. Restock Products")            # Option to add stock to existing products
    print("4. Exit")                        # Exit the program
    print("_______________________________________________________________________________")
    
    # Taking user input for menu choice
    choice = input("Enter your choice: ")

    # Checking user's choice and calling appropriate function
    if choice == "1":
        Operation.display_products()  # Calls function to display available products
    elif choice == "2":
        Operation.sell_product()  # Calls function to sell products
    elif choice == "3":
        Operation.restock_product()  # Calls function to restock products
    elif choice == "4":
        # Exiting the loop and ending the program
        print("Thank you for visiting WeCare!")
        loop = False
    else:
        # Handling invalid input
        print("Invalid input. Please try again.")

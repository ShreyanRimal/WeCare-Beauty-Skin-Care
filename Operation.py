# Importing necessary modules
import READ   # Module to read product data
import WRITE  # Module to write invoice and product data
from datetime import date  # For recording date if needed

# Function to display available products
def display_products():
    print("_______________________________________________________________________________")
    print("Product | Brand | Stock | Selling Price | Country")
    print("_______________________________________________________________________________")
    READ.fread()  # Calls the function to display product details from file

# Function to handle selling products to customers
def sell_product():
    name = input("Enter customer's name: ")  # Get customer's name
    products = READ.read()  # Load product list from file
    cart = []  # To store the products that customer buys
    total = 0  # To store the total bill

    while True:
        try:
            sn = int(input("Enter product SN to buy (0 to finish): "))  # Get product serial number
            if sn == 0:
                break  # Exit the loop if input is 0
            quantity = int(input("Enter quantity to buy: "))  # Get quantity

            item = products[sn]  # Select the item from product list

            # Check if enough stock is available including free items (buy 3 get 1 free logic)
            if int(item[2]) >= quantity + (quantity // 3):
                free = quantity // 3  # Calculate free items
                total_items = quantity + free  # Total items to be removed from stock

                cost_price = int(item[3])  # Get cost price from list
                selling_price = cost_price * 2  # Selling price is double the cost price
                total += quantity * selling_price  # Update total bill

                item[2] = str(int(item[2]) - total_items)  # Reduce stock in product list

                # Add the item to the cart with details
                cart.append([item[0], item[1], quantity, free, selling_price])
            else:
                print("Insufficient stock.")  # Show error if not enough stock
        except:
            print("Invalid input or SN.")  # Show error if input is wrong

    if cart:
        # If the customer has bought something, write invoice and update product file
        WRITE.write_customer_invoice(cart, name, total)
        WRITE.fwrite(products)

# Function to restock products from supplier
def restock_product():
    name = input("Enter supplier/vendor name: ")  # Get supplier name
    products = READ.read()  # Load current product list
    additions = []  # List to store restocked items

    while True:
        try:
            sn = int(input("Enter product SN to restock (0 to finish): "))  # Get product serial number
            if sn == 0:
                break  # Exit the loop
            new_stock = int(input("Enter quantity to add: "))  # Get quantity to add
            new_price = int(input("Enter cost price per item: "))  # Get new cost price

            item = products[sn]  # Select the item from product list

            item[2] = str(int(item[2]) + new_stock)  # Update stock
            item[3] = str(new_price)  # Update cost price

            # Add the restock details to the list
            additions.append([item[0], item[1], new_stock, new_price])
        except:
            print("Invalid input or SN.")  # Show error if input is invalid

    if additions:
        # If products are restocked, write supplier invoice and update product file
        WRITE.write_supplier_invoice(additions, name)
        WRITE.fwrite(products)

from datetime import date  # Importing date to add current date in invoice files

# Function to write updated product data to the file
def fwrite(dictionary):
    with open("products.txt", "w") as file:  # Open 'products.txt' in write mode
        for val in dictionary.values():  # Loop through all product data
            # Create a comma-separated string of product details
            line = val[0] + "," + val[1] + "," + val[2] + "," + val[3] + "," + val[4]
            file.write(line + "\n")  # Write the line to file

# Function to generate and save invoice for customer after purchase
def write_customer_invoice(cart, customer, total):
    # Create a file name with customer name and today's date
    filename = "Invoice_" + customer + "_" + str(date.today()) + ".txt"
    with open(filename, "w") as file:  # Open the invoice file in write mode
        file.write("Wecare Beauty & Skin Care Invoice\n")
        file.write("Customer: " + customer + "\nDate: " + str(date.today()) + "\n")
        file.write("\nProduct | Brand | Qty | Free | Unit Price | Total\n")

        # Loop through all items the customer bought
        for item in cart:
            # Create line with product details
            line = item[0] + " | " + item[1] + " | " + str(item[2]) + " | " + str(item[3]) + " | " + str(item[4]) + " | " + str(item[2] * item[4]) + "\n"
            file.write(line)  # Write line to invoice

        # Write the grand total at the end
        file.write("\nGrand Total: Rs. " + str(total) + "\n")

# Function to generate and save restock note from supplier
def write_supplier_invoice(restocks, supplier):
    # Create a file name with supplier name and today's date
    filename = "Restock_" + supplier + "_" + str(date.today()) + ".txt"
    with open(filename, "w") as file:  # Open the file in write mode
        file.write("Wecare Beauty & Skin Care Restock Note\n")
        file.write("Supplier: " + supplier + "\nDate: " + str(date.today()) + "\n")
        file.write("\nProduct | Brand | Quantity | Rate | Total\n")

        grand_total = 0  # Initialize grand total

        # Loop through all restocked items
        for item in restocks:
            total = item[2] * item[3]  # Calculate total cost for each item
            grand_total += total  # Add to grand total
            # Create line with product details
            line = item[0] + " | " + item[1] + " | " + str(item[2]) + " | " + str(item[3]) + " | " + str(total) + "\n"
            file.write(line)  # Write line to restock note

        # Write the grand total at the end
        file.write("\nGrand Total: Rs. " + str(grand_total) + "\n")

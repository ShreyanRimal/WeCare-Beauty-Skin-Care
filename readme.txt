WeCare Beauty & Skin Care Management System
Overview
This is a Python-based inventory and sales management system for a beauty and skincare retail business called "WeCare Beauty & Skin Care". The system helps manage product inventory, process customer sales, and handle supplier restocking operations.

Features
Product Management:

View current product inventory

Track product details including name, brand, stock quantity, price, and country of origin

Sales Processing:

Process customer purchases

Automatic "buy 3 get 1 free" promotion calculation

Generate customer invoices

Inventory Management:

Restock products from suppliers

Update product quantities and prices

Generate supplier restock notes

File Operations:

Persistent data storage in text files

Automatic invoice generation with customer/supplier details and date stamps

File Structure
text
wecare-system/
├── products.txt          # Main product database
├── main.py               # Main program entry point
├── Operation.py          # Core business logic operations
├── READ.py               # File reading utilities
├── WRITE.py              # File writing utilities
└── README.md             # This documentation file
Modules
main.py - The main program that displays the menu and controls program flow

Operation.py - Contains core business logic for:

Displaying products

Processing sales

Handling restocks

READ.py - Handles reading product data from file

WRITE.py - Handles:

Updating product data

Generating customer invoices

Creating supplier restock notes

Usage
Run main.py to start the application

Use the menu to:

Display available products

Process customer sales

Restock inventory

The system will automatically:

Update product quantities

Generate invoices/restock notes

Save all changes to files

Business Rules
Selling price is automatically calculated as 2x the cost price

"Buy 3 get 1 free" promotion is automatically applied during sales

All transactions are date-stamped and saved as text files

Product database is maintained in products.txt with comma-separated values

Sample Data Format
The products.txt file contains product information in CSV format:

text
ProductName,Brand,Quantity,CostPrice,Country
Requirements
Python 3.x

No external dependencies required

Author
[SHREYAN RIMAL ]

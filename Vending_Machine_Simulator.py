# 🥤 Prompt: Smart Vending Machine Simulator
# 📝 Problem Statement:
# Create a command-line Python program that simulates a smart vending machine. The user can interact with the machine to view available products,
# insert money, buy products, check their balance, and exit the system.The entire system should work in memory and reset only upon restarting the program.
#
# 🎯 Objectives:
# Create a vending machine product catalog using a dictionary.
# Let users add money and purchase products based on their balance.
# Show updated stock after each purchase.
# Display a purchase summary and return any remaining balance on exit.
# Use a loop to continuously show options until the user exits.
#
# 🧩 Features to Implement:
# 1. Product Catalog:
# Use a dict to store product info with:
# Product ID as key
# Values as another dict with:
# "name": name of the product
# "price": cost of the product
# "stock": quantity available
#
# Example:
# products = {
#     1: {"name": "Chips", "price": 25, "stock": 10},
#     2: {"name": "Soda", "price": 40, "stock": 8},
#     3: {"name": "Chocolate", "price": 30, "stock": 5},
#     4: {"name": "Water Bottle", "price": 20, "stock": 15}
# }
#
# 2. User Wallet and Purchase History:
# Let the user add money to their wallet.
# Maintain a purchase history using a list to track bought items.
# 3. Interactive Menu System:
# Present a menu using a loop and display the following options:
#
# 1. Show Available Products
# 2. Add Money
# 3. Buy Product
# 4. Check Balance
# 5. Exit
# 4. Menu Actions:
# ✅ Show Available Products:
#
# Display all items with ID, name, price, and stock.
# ✅ Add Money:
# Let user input a number to increase their balance. Validate positive input.
# ✅ Buy Product:
# Ask for product ID.
# Check if ID exists.
# Check stock and balance before purchase.
# Deduct price from balance and reduce stock.
# Add item to purchase history.
# ✅ Check Balance:
# Show current available money.
# ✅ Exit:
# Show purchase summary.
# Return remaining balance.
# Exit loop using break.

def user_list():
    total_money = 3000
    summary_dict = []

    products = {
        1: {"name": "Chips", "price": 25, "stock": 10},
        2: {"name": "Soda", "price": 40, "stock": 8},
        3: {"name": "Chocolate", "price": 30, "stock": 5},
        4: {"name": "Water Bottle", "price": 20, "stock": 15}
    }

    while True:
        print(f"\n1. Show Available Products \n2. Add Money \n3. Buy Product\n4. Check Balance\n5. Exit")
        select = input("Select Task :")

        if select == "1":
            for key, value in products.items():
                print(f"{key}: {value}")

        elif select == "2":
            try:
                add_money = int(input("Enter Money you want to Add :"))
                total_money += add_money
                print(f"Added money: {add_money}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif select == "3":
            try:
                buy = int(input("Enter ID You want to buy product : "))

                if buy not in products:
                    print("Enter valid product ID.")
                    continue

                stock = products[buy]["stock"]
                print(f"Product : {products[buy]['name']} available quantity  : {stock}")

                try:
                    qty = int(input("Enter Quantity : "))
                except ValueError:
                    print("Invalid input")
                    continue

                if qty > stock:
                    print(f"Not enough stock. Only available: {stock}")
                else:
                    current_stock = stock - qty
                    total_cost = products[buy]["price"] * qty

                    if total_money < total_cost:
                        print(f"Insufficient funds.")
                    else:
                        total_money -= total_cost
                        products[buy]["stock"] = current_stock
                        print(f"Purchase successful: {qty} x {products[buy]['name']} for {total_cost}.")
                        temp_var = f"Total Quantity {qty} and Stock Name: {products[buy]['name']} for Total Cost: {total_cost}"
                        summary_dict.append(temp_var)

            except ValueError:
                print("Invalid input enter valid product ID.")

        elif select == "4":
            print(f"Current Amount: {total_money}")

        elif select == "5":
            print("Exit")
            for i in summary_dict:
                print(i)
            print(f"Total Amount: {total_money}")
            break

        else:
            print("Invalid selection.")


user_list()
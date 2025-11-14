# Add the following items to the inventory as dictionary entries: For your information price is per quantity.
#
# Item: 'Apple', Quantity: 50, Price: 100
# Item: 'Banana', Quantity: 30, Price: 50
#
# Item: 'Orange', Quantity: 40, Price: 70
#

inventory = {}
# add item in dictionary
def fruit():

    try:
        total_fruit = int(input("Enter number of fruits to add: "))

        for j in range(1, total_fruit + 1):
            print(f"\nFruit {j} details:")
            try:
                fruit_name = input("Enter fruit name: ").capitalize()

                if fruit_name not in inventory:
                    quantity = float(input("Enter Quantity: "))
                    price = float(input("Enter Price : "))

                    inventory.update({
                        fruit_name: {'Quantity': quantity, 'Price': price}
                    })

                    print(f"{fruit_name} successfully added in inventory.\n")
                else:print(f"fruit :{fruit_name} is alredy in inventory  ")

            except ValueError:
                print("Invalid input.")
                break

    except ValueError:
        print("Invalid input")

#display item
def display_inventory():

    print("\n--- INVENTORY LIST ---")
    print("{:<12} {:<12} {:<12}".format('Fruit', 'Quantity', 'Price'))

    for item, detail in inventory.items():
        print("{:<12} {:<12} {:<12}".format(item, detail['Quantity'], detail['Price']))

#update item in dictionary
def update_inventory(item_name, quantity):
    item_name = item_name.capitalize()
    if item_name in inventory:
        inventory[item_name].update({
            'Quantity': inventory[item_name]['Quantity'] + quantity
        })
        print(f"{item_name} quantity updated.")
    else:
        try:
            price = float(input(f"Enter price for new item '{item_name}': "))
            inventory.update({
                item_name: {'Quantity': quantity, 'Price': price}
            })
            print(f"{item_name} added successfully to inventory.")
        except ValueError:
            print("Invalid price entered.")



#sell item in dictionary
sale_revenue = 0
def sell_item(item_name ,  qty ):
    global sale_revenue
    item_name = item_name.capitalize()

    if item_name not in inventory:
        print(f"Not found : {item_name} in inventory ")
        return
        
    if inventory[item_name]['Quantity'] < qty:
        print(f"{item_name}And that Quantity is {qty} : not enough ")
        return

    sale_revenue = qty * inventory[item_name]['Price']

    inventory[item_name]['Quantity'] -= qty
    print(f"SELL {item_name} of quantity {qty} ")



#create total revenue
def calculate_total_revenue():
    total = 0
    for i in inventory.values():
        total += i['Quantity'] * i['Price']
    print(f"Total Revenue : {total}")
    print(f"Total Sales Revenue:{sale_revenue}")


#,main code that call all the function as pre input
def main_program():

    while True:
        print("\nINVENTORY MANAGEMENT SYSTEM  \n1. Add Item \n2. Display Items \n3. Update Inventory \n4. Sell Item \n5. Total Revenue \n6. Exit")

        select = input("\nSELECT TASK: ")

        if select == "1":
            fruit()

        elif select == "2":
            display_inventory()

        elif select == "3":
            item_name = input("Enter Item Name to update: ")
            try:
                qty_change = float(input("Enter quantity change :"))
                update_inventory(item_name, qty_change)
            except ValueError:
                print("Invalid quantity input. ")

        elif select == "4":
            print("4.Sell Item ")
            item_name = input("Enter Item Name to SELL : ")

            try:
                qty_sell = float(input("Enter quantity To SELl : "))
                sell_item(item_name ,qty_sell )
            except ValueError:
                print("Invalid quantity input")


        elif select == "5":
            print("5. Total Revenue.")
            calculate_total_revenue()

        elif select == "6":
            print("Exit....")
            break

        else:
            print("Invalid input.")

main_program()

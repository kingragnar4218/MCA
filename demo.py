def user_list():
    total_money = 0
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
            add_money = int(input("Enter Money you want to Add :"))
            total_money += add_money
            print(f"Added money: {add_money}")

        elif select == "3":
            buy = int(input("Enter ID You want to buy product : "))


            if buy not in products:
                print("Invalid ID  Enter valid product ID.")
                continue


            stock = products[buy]["stock"]
            print(f"Product : {products[buy]['name']} available quantity  : {stock}")
            qty = int(input("Enter Quantity : "))


            if qty > stock:
                print(f"Not enough stock Only available : {stock}")
            else:
                current_stock = stock - qty
                total_cost = products[buy]["price"] * qty


                if total_money < total_cost:
                    print(f"Insufficient funds.")
                else:
                    total_money -= total_cost

                    products[buy]["stock"] = current_stock
                    print(
                        f"Purchase successful: {qty} x {products[buy]['name']} for {total_cost}.")

        elif select == "4":
            print(f"Current Amount: {total_money}")

        elif select == "5":
            print("Exit")
            break

        else:
            print("Invalid selection.")


user_list()


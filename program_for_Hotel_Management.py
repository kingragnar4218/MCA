from datetime import datetime
import random
from itertools import repeat

#
# WELCOME TO HOTEL
#
# 1. Enter Customer Data
#
# 2. Calculate Room Rent
#
# 3. Calculate the Restaurant Bill.
#
# 4. Show Total Cost
#
# 5. Exit
#
#
#
# Enter your Choice: 1
#
# Enter your name: Ram
#
# Enter your City: Rajkot
#
# Enter your checkin date: 24-11-2023
#
# Enter your checkout date: 25-11-2023
#
# Your room no is 101
#
#
#
# Enter your Choice: 2
#
# We have the following rooms for you:
#
# 1. Type A --> 6000 Rs
#
# 2. Type B --> 5000 Rs
#
# 3. Type C --> 4000 Rs
#
# Enter your Choice: 2
#
# For how many nights did you stay: 4
#
# You have opted for room type B
#
# Your room rent is 20000
#
#
#
# Enter your Choice: 3
#
# Restaurant Menu
#
# 1. Water ---> 20 Rs
#
# 2. Tea ---> 10 Rs
#
# 3. Breakfast ---> 90 Rs
#
# 4. Lunch ---> 110 Rs
#
# 5. Dinner ---> 150 Rs
#
# 6. Exit
#
# Enter your Choice: 4
#
# Enter the quantity: 3
#
# Enter your Choice: 2
#
# Enter the quantity: 3
#
# Total Restaurant Bill = 360 Rs
#
#
#
# Enter your Choice: 4
#
# Enter your room number: 101
#
# Your room rent is: 20000 Rs
#
# Your restaurant bill is: 360 Rs
#
# Your grand total is: 20360 Rs

customer = {}

customer_id = 0


#2002-11-11


#customer_unq_id = random.randint(100, 103)
# def get_unq_num():
#     global customer_id
#     customer_unq_id = random.randint(100, 103)
#     while True:
#
#         if customer_unq_id in customer:
#
#             print("Room is Allocate Change the Room ")
#             # print(customer.keys())
#             break
#         else:
#             customer_id = customer_unq_id
#             customer.update({
#                 # customer_id: customer_unq_id
#                 'customer_id': customer_id
#             })

import random


customer_id = 0


def get_unq_num():
    global customer, customer_id
    while True:
        customer_unq_id = random.randint(100, 103)
        if customer_unq_id in customer:
            print(f"Room {customer_unq_id} is allocated. Trying another ")
        else:
            customer_id = customer_unq_id
            # customer.update({
            #     # customer_id: customer_unq_id
            #     'customer_id': customer_unq_id
            # })
            #print(f"Allocated new customer ID: {customer['customer_id']}")
            #print(customer)
            break

            # print(customer.keys())


# get_unq_num()

def add_customer():
    try:
        for j in range(1):

            global customer_id
            #customer_id = random.randint(100, 102)
            get_unq_num()
            print("---- 1. Enter Customer Data ----")
            try:
                if customer_id not in customer:

                    name = input("Enter Your Name :")
                    city = input("Enter your City :")

                    check_in = input("Enter your checkin date format = YYYY-MM-DD:")
                    format = "%Y-%m-%d"
                    try:
                        validate_date(check_in, format)
                    except ValueError:
                        print("invalid Date Enterrrrrr ")
                        continue

                    check_out = input("Enter your checkout date format = YYYY-MM-DD: :")
                    try:
                        validate_date(check_out, format)
                    except  ValueError:
                        print("invalid Date Enterrrrrr ")
                        continue  # 2002-11-11
                    #get_unq_num()

                    customer.update({
                        customer_id: {'name': name, 'city': city, 'check_in': check_in, 'check_out': check_out}
                    })
                else:
                    print(f" {customer_id} is alredy in Allocate  ")

                #print(f"Your room no is :{customer[customer_id]}")
                print(f"Your room no is: {customer_id}")
                display_inventory()
                print("---- Customer Data Add successfully ----")
                # print(customer)


                # for key in customer:
                #     print(f"Key: '{key}', Data Type: {type(key)}")

            except ValueError:
                print("Invalid input ")
                break
    # here    create    random.randint(100, 102)    but if one    number is repeat    so    it    not enter    dictionary and where    use
    # while loop if loop is false than that number store in customer_id give me simpe and easy code and create that function

    except ValueError:
        print("Invalid input")


# display item
def display_inventory():
    print("\n--- INVENTORY LIST ---")
    print("{:<12} {:<12} {:<12} {:<12} {:<12}".format('ID', 'name', 'city', 'check_in', 'check_out'))

    for item, detail in customer.items():
        print("{:<12} {:<12} {:<12} {:<12} {:<12}".format(item, detail['name'], detail['city'], detail['check_in'],
                                                          detail['check_out']))


def validate_date(date_string, date_format):
    return datetime.strptime(date_string, date_format)

room_rent =0
def choice_2(get_room_id):
    global room_rent
    print("---- We have the following rooms for you: ----")
    print(f"type a = 6000\ntype b = 5000\ntype c = 4000")
    type_a = 6000
    type_b = 5000
    type_c = 4000
    try:
        night = int(input("For how many nights did you stay:"))
        room_type = input("You have opted for room type")
    except ValueError:
        print("Invalid input ")

    if room_type == "a":
        room_rent = night * type_a
        print(f"Your room rent is :{room_rent}")
    elif room_type == "b":
        room_rent = night * type_b
        print(f"Your room rent is :{room_rent}")
    elif room_type == "c":
        room_rent = night * type_c
        print(f"Your room rent is :{room_rent}")
    else:
        print("You Enter Invalid Input Type  ")

    customer[customer_id].update({
        'room_rent': room_rent
    })

    #print(customer)


# 1. Water ---> 20 Rs
# 2. Tea ---> 10 Rs
# 3. Breakfast ---> 90 Rs
# 4. Lunch ---> 110 Rs
# 5. Dinner ---> 150 Rs
# 6. Exit
# Enter your Choice: 4
# Enter the quantity: 3
# Enter your Choice: 2
# Enter the quantity: 3
# Total Restaurant Bill = 360 Rs
total_bill = 0
def choice_3(get_room_id):
    global total_bill
    quantity = 0
    while True:
        print("----Restaurant Menu----")
        print(f"\n1. Water ---> 20 Rs \n2. Tea ---> 10 Rs \n3. Breakfast ---> 90 Rs\n4. Lunch ---> 110 Rs\n5. Dinner ---> 150 Rs\n6. Exit")

        try:
            menu_number = input("Enter Your Choice :")
        except ValueError:
            print("Invalid input ")

        # if menu_number == Restaurant[menu_number]:
        #     print(Restaurant[menu_number])

        if menu_number == "1":
            water = 20
            try:
                quantity = int(input("Enter quantity Water :"))
            except ValueError:
                print("Invalid input ")

            total_water_bill = water * quantity
            total_bill += total_water_bill
        elif menu_number == "2":
            tea = 10
            try:
                quantity = int(input("Enter quantity Tea :"))
            except ValueError:
                print("Invalid input ")

            total_tea_bill = tea * quantity
            total_bill += total_tea_bill
        elif menu_number == "3":
            break_fast = 90
            try:
                quantity = int(input("Enter quantity BreakFast :"))
            except ValueError:
                print("Invalid input ")

            total_break_bill = break_fast * quantity
            total_bill += total_break_bill
        elif menu_number == "4":
            lunch = 110
            try:
                quantity = int(input("Enter quantity Lunch :"))
            except ValueError:
                print("Invalid input ")

            total_lunch_bill = lunch * quantity
            total_bill += total_lunch_bill
        elif menu_number == "5":
            dinner = 150
            try:
                quantity = int(input("Enter quantity Dinner :"))
            except ValueError:
                print("Invalid input ")
            total_dinner_bill = dinner * quantity
            total_bill += total_dinner_bill
        elif menu_number == "6":
            print("Exit..... Restaurant Menu ")
            break
        else:
            print("Invalid Input ")

    print(f"Total Restaurant Bill {total_bill}")
    customer[customer_id].update({
        'total_bill': total_bill
    })
    print(customer)



def choice_3_update(get_room_id):

    global total_bill
    total_bill = 0

    Restaurant = {
        "1": ("Water", 20),
        "2": ("Tea", 10),
        "3": ("Breakfast", 90),
        "4": ("Lunch", 110),
        "5": ("Dinner", 150)
    }

    while True:
        print("\n---- Restaurant Menu ----")
        for key, (item, price) in Restaurant.items():
            print(f"{key}. {item} ---> {price} Rs")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "6":
            print("--- Restaurant Menu ---")
            break

        if choice not in Restaurant:
            print("Invalid choice")
            continue

        item_name, price = Restaurant[choice]
        try:
            quantity = int(input(f"Enter quantity for {item_name}: "))
        except ValueError:
            print("Invalid quantity")


        item_total = price * quantity
        total_bill += item_total

        print(f"Current Total: Rs {total_bill}")

    customer[customer_id].update({
        'total_bill': total_bill
    })
    print("---- Restaurant Bill Added Successfully ----")




# Enter your Choice: 4
# Enter your room number: 101
# Your room rent is: 20000 Rs
# Your restaurant bill is: 360 Rs
# Your grand total is: 20360 Rs

def choice_4(get_room_id):
    print("---- Show Total Cost ----")
    #get_room = input(f"Enter your room number:{customer[customer_id]}")

    grand_total = customer[get_room_id]['room_rent'] + customer[get_room_id]['total_bill']

    print(f"Your Room Number: {get_room_id}")
    print(f"Your room rent is : {customer[get_room_id]['room_rent']}")
    print(f"Your restaurant bill is :{customer[get_room_id]['total_bill']}")
    print(f"Your grand total is :{grand_total}")


def select_choice():
    while True:
        print("WELCOME TO HOTEL")
        print(
            f"1. Enter Customer Data \n2. Calculate Room Rent \n3. Calculate the Restaurant Bill. \n4. Show Total Cost \n5. Exit")
        select = input("Enter Your Choice :")

        if select == "1":
            add_customer()

        elif select == "2":

            try:
                get_room_id = int(input("Enter Enter Room Number :"))

                if get_room_id in customer:
                    #update_choice_2(get_room_id)
                    choice_2(get_room_id)
                else:
                    print(f"Not found {get_room_id}")

            except ValueError:
                print("Invalid quantity input. ")#2000-2-2

        elif select == "3":

            try:
                get_room_id = int(input("Enter Enter Room Number :"))

                if get_room_id in customer:

                    choice_3_update(get_room_id)
                else:
                    print(f"Not found {get_room_id}")

            except ValueError:
                print("Invalid quantity input. ")#2000-2-2
        elif select == "4":
            #choice_4()
            try:
                get_room_id = int(input("Enter Enter Room Number :"))

                if get_room_id in customer:

                    choice_4(get_room_id)
                else:
                    print(f"Not found {get_room_id}")

            except ValueError:
                print("Invalid quantity input. ")#2000-2-2
        elif select == "5":
            print("Exit..... Program....")
            break
        else:
            print("Invalid Input...")


select_choice()

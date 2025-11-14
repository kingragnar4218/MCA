# NOTE : sarting time 9:05 endding 12:20
# 3 hours and 15 minutes
# this task first i create 2 empty list and get value from user and that append in list after i complet 10% fixed discount where i first get total amount and after add
# 18% GST and total amount i display and after that amount i give 10% on total amount and after that diduct and i display that total payble amount and complet that
# and i create function dynamic_discount where it work user enter discount on that specific item and it amount and display final  amount
# after this i create this Total_Price_Calculation_and_GST_and_discount_itemwise() function so where i use list item_discount and list final_amounts_after_discount
# using variable  this item_discount_value discount_price where calculete amount and store and append in list after display list in format item and that amount

#this function is get item append in list
item_name = [] # "qqq","www","aaa"
def get_item():
    print("------enter item list -----")
    for i in range(1 , 4):
        item_name.append(input(f"enter item name {i} :"))
    print(item_name)


#this function is get item price  append in list
item_amount = [] # 100 , 200 , 300
def get_amount_item():
    print("----- item amount ------")
    for i in range(1 ,4):
        item_amount.append(float(input(f"enter price of item {i} :")))
    # print(item_amount)

#this function is Calculation total amount and TAX
def Total_Price_Calculation_and_GST_and_discount ():
    print("----- 10% discount bill -----")
    total_amount = sum(item_amount)
    print(f"Total Amount before TAX :  {total_amount}")

    #calculate GST
    tax = total_amount * 18 / 100
    # hete i print tax [GST]
    print(f"Total GST : {tax}")
    # sum of tax [GST] and total amount
    final_amount = tax + total_amount
    print(f"Total Amount After TAX [GST ] : {final_amount}")

    #here i calculate discount after final amount
    discount = final_amount * 10 / 100
    print(f"Total Discount is : {discount}")
    #diduct amount discount
    total_final_amount = final_amount - discount
    print(f"Total Payble final Amount is : {total_final_amount}")


get_item()
get_amount_item()
Total_Price_Calculation_and_GST_and_discount()

def dynamic_discount():
    print("------ dynamic discount -------")
    selected_item = int(input("enter item number you want :"))
    if selected_item <= 3:
        selected_item -= 1
        # print(selected_item)
    else:
        print("invalid  item selected  ")
    qty = item_amount[selected_item]
    print(f"selected Item amount : {qty}")

    total_amount = qty
    print(f"Total Amount before TAX :  {total_amount}")

    # calculate GST
    tax = total_amount * 18 / 100
    # hete i print tax [GST]
    print(f"Total GST : {tax}")
    # sum of tax [GST] and total amount
    final_amount = tax + total_amount
    print(f"Total Amount After TAX [GST ] : {final_amount}")

    # here i calculate discount after final amount
    user_discount = int(input("enter discount you want to give :"))
    discount = final_amount * user_discount / 100
    print(f"Total Discount is : {discount}")
    # diduct amount discount
    total_final_amount = final_amount - discount
    print(f"Total Payble final Amount is : {total_final_amount}")

dynamic_discount()

def Total_Price_Calculation_and_GST_and_discount_itemwise():
    print("----- Discount Itemwise -----")
    # Calculate total amount before tax
    total_amount = sum(item_amount)
    print(f"Total Amount before TAX: {total_amount}")

    # Calculate GST (18% tax)
    tax = total_amount * 18 / 100
    print(f"Total GST: {tax}")

    # Calculate the final amount after adding GST
    final_amount = tax + total_amount
    print(f"Total Amount After TAX [GST]: {final_amount}")


    item_discount = []
    for i in range(3):
        item_discount.append(float(input(f"Enter discount for item {i + 1} {item_name[i]}: ")))

    # Calculate discount and the final amount for each item
    final_amounts_after_discount = []
    for i in range(3):
        # Calculate the discount for each item based on the input percentage
        item_discount_value = item_amount[i] * item_discount[i] / 100
        discount_price = item_amount[i] - item_discount_value
        final_amounts_after_discount.append(discount_price)

    # Calculate the total payable amount after discount
    total_after_discount = sum(final_amounts_after_discount)
    print(f"Total Payable Amount After Discount for all items: {total_after_discount}")

    # Print individual item amounts after discount
    for i in range(3):
        print(
            f"Item: {item_name[i]}, Original Price: {item_amount[i]}, Discount: {item_discount[i]}%, Final Price: {final_amounts_after_discount[i]}")



Total_Price_Calculation_and_GST_and_discount_itemwise()

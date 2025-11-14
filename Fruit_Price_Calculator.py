# Enter number of fruits: 2
#
# Fruit 1 details:
# Enter fruit name: Apple
# Enter price per kg: 120
# Enter quantity in kg: 2
#
# Fruit 2 details:
# Enter fruit name: Banana
# Enter price per kg: 60
# Enter quantity in kg: 3
#
# Results:
#        0           1           2       3
#    0  Fruit      Price/kg   Qty(kg)   Total
#    1  Apple      120.0      2.0       240.0
#    2  Banana     60.0       3.0       180.0
#
# Grand Total = 420.



def fruit():
    fruit = []

    try:
        total_fruit = int(input("Enter number of fruits: "))

        for j in range(1, total_fruit + 1):
            print(f"Fruit {j} details:")

            try:
                fruit_name = input("Enter fruit name: ")
                price_kg = float(input("Enter price per kg: "))
                qty_kg = float(input("Enter quantity in kg: "))
                total_price = price_kg * qty_kg


                fruit.append([fruit_name, price_kg, qty_kg, total_price])

            except ValueError:
                print("Invalid input ")
                break


        print("\n{:<12} {:<10} {:<10} {:<10}".format('Fruit', 'Price/kg', 'Qty(kg)', 'Total'))

        grand_total = 0
        for i in fruit:
            print("{:<12} {:<10} {:<10} {:<10}".format(i[0], i[1], i[2], i[3]))
            grand_total += i[3]
        print(f"Grand Total : {grand_total}")

    except ValueError:
        print("Invalid input")

fruit()



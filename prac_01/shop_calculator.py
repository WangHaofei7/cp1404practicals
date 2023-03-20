"""
SET total to 0
INPUT number of items
WHILE number of items is less than 0
    PRINT "Invalid number of items!"
    INPUT number of items
END WHILE
FOR each item
    INPUT price of item
    ADD price of item to total
END FOR
IF total is greater than 100
    MULTIPLY total by 0.9
END IF
PRINT "Total price for", number of items, "items is $", total
"""

def shop_calculator():
    total = 0
    num_items = int(input("Number of items: "))
    while num_items < 0:
        print("Invalid number of items!")
        num_items = int(input("Number of items: "))
    for i in range(num_items):
        price = float(input("Price of item: "))
        total += price
    if total > 100:
        total *= 0.9
    print(f"Total price for {num_items} items is ${total:.2f}")


shop_calculator()
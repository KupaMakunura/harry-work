# SECTION B


# B1
'''
1. Set initial value i = 1
2. Set initial value divisor = 1
3. Set initial value result = 0
4. Repeat until divisor is less than or equal to 0.00001:
    a. Calculate result = 1 / (i * 2)
    b. Print result
    c. Increment i by 2
    d. Update divisor to the absolute value of result

'''
def convergence_sequence():
    i = 1
    divisor = 1
    result = 0

    while divisor >= 0.00001:
        result = 1 / (i * 2)
        print(result)
        i += 2
        divisor = abs(result)

convergence_sequence()

# B2
def sales_adder():
    sales = []
    while True:
        try:
            sale = float(input("Enter daily sales (enter 0 to finish): "))
            if sale == 0:
                break
            sales.append(sale)
        except ValueError:
            print("Please enter a valid number.")

    total_sales = sum(sales)
    average_sales = total_sales / len(sales) if len(sales) > 0 else 0

    print(f"Total Sales: {total_sales}")
    print(f"Average Sales: {average_sales}")

sales_adder()

# B3

def update_prices(items):
    for item, price in items.items():
        while True:
            try:
                change = input(f"Do you want to change the price of {item}? (yes/no): ")
                if change.lower() == 'yes':
                    percentage = float(input("Enter the percentage increase/decrease (e.g. 100 for 100% increase): "))
                    price_change = price * (percentage / 100)
                    price += price_change
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        items[item] = price

    return items

def main():
    items = {}
    while True:
        item = input("Enter the name of the item (enter 'done' to finish): ")
        if item.lower() == 'done':
            break
        price = float(input(f"Enter the price of {item}: "))
        items[item] = price

    updated_items = update_prices(items)

    print("\nUpdated Prices:")
    for item, price in updated_items.items():
        print(f"{item}: ${price:.2f}")

if __name__ == "__main__":
    main()

# B4
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You're at a crossroads. Where do you want to go? Type 'left' or 'right': ")

if direction.lower() == "left":
    action = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ")
    
    if action.lower() == "wait":
        door_color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ")
        
        if door_color.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif door_color.lower() == "yellow":
            print("You found the treasure! You Win!")
        elif door_color.lower() == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

# END
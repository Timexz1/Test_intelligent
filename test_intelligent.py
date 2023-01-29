# Juice Vending Machine

# Available coins: 1, 2, 5, 10 baht
coin_values = {'a':1,'b':2,'c':5,'d':10}
coin_count = {'a': 10, 'b': 10, 'c': 10, 'd': 10}

# Available products and prices
products = {"orange juice": 13, "apple juice": 15, "kiwi juice": 22}

# Function to calculate change
def calculate_change(paid, price):
    change = paid - price
    change_coins = {}
    for coin in sorted(coin_values.keys(), key=lambda x:coin_values[x], reverse=True):
        if change == 0:
            break
        if change >= coin_values[coin] and coin_count[coin] > 0:
            num_of_coin = change // coin_values[coin]
            if num_of_coin > coin_count[coin]:
                num_of_coin = coin_count[coin]
            change -= num_of_coin * coin_values[coin]
            change_coins[coin] = num_of_coin
            coin_count[coin] -= num_of_coin
    if change != 0:
        return "Sorry, the machine cannot give back the change at the moment. Please try again later."
    return change_coins

# Main function
def vending_machine():
    print("Welcome to the Juice Vending Machine!")
    print("Available products:")
    for product, price in products.items():
        print(f"- {product} ({price} baht)")
    selected_product = input("Please select a product: ")
    if selected_product not in products:
        return "Invalid product. Please select a valid product."
    price = products[selected_product]
    coin_input = input("Please enter the type of coins, separated by commas, for example 'c,d,d': ")
    coins = coin_input.split(",")
    paid = 0
    for coin in coins:
        if coin not in coin_values:
            return "Invalid coin type. Please enter a valid coin type."
        if coin_count[coin] <= 0:
            return "Insufficient coin in machine. Please enter other coin type."
        coin_count[coin] -= 1
        paid += coin_values[coin]
    if paid < price:
        return "Insufficient amount. Please insert more coins."
    change = calculate_change(paid, price)
    return f"Enjoy your {selected_product}! Your change is {change} baht."

# Example usage
print(vending_machine())
# Input: "c,d,d"
# Output: "Enjoy your orange juice! Your change is {'c': 1, 'b': 1} baht."

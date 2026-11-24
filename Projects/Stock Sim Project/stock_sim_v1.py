# STOCK PRICE SIMULATOR v1

# Import random 
import random

# Starting values
stock_price_today = 100
highest_price = 100
lowest_price = 100

print("Starting price: $100")

# Loop for 30 days

for daily_price_mvmnt in range(1, 31):
    daily_move = random.randint(-5, 5)
    daily_percent = (daily_move / 100) + 1

    stock_price_today = stock_price_today * daily_percent

    print("Day " + str(daily_price_mvmnt) + ": " + str(round(stock_price_today, 2)))

    if stock_price_today > highest_price:
        highest_price = stock_price_today

    if stock_price_today < lowest_price:
        lowest_price = stock_price_today

    final_price = stock_price_today
        

print("Stock price: $" + str(round(final_price, 2)))
print("Highest price: $" + str(round(highest_price, 2)))
print("Lowest price: $" + str(round(lowest_price, 2)))

          
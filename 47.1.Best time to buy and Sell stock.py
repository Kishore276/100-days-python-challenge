def max_profit(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)  # Update the minimum price
        profit = price - min_price  # Calculate profit if sold at current price
        max_profit = max(max_profit, profit)  # Update maximum profit

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
result = max_profit(prices)
print("Maximum profit:", result)

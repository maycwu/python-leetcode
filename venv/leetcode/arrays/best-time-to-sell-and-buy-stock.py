prices = [7, 1, 5, 3, 6, 4]  # max profit is 5 (buy 1 and sell 6)


def max_profit(prices):
    buy = prices[0]
    profit = 0

    for i in range(len(prices)):
        current_price = prices[i]
        # if current price is less than previous buy value, assign buy to current price
        if current_price < buy:
            buy = current_price
        else:
            current_profit = current_price - buy
            profit = max(current_profit, profit)
    return profit


print(max_profit(prices))

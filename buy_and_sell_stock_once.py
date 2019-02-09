# Write a program that takes an array denoting the daily stock price and returns that could be made by buying and then
# selling one share of that stock

test_prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
test_result = 30
# buy at 260, sell at 290


def buy_and_sell_stock_once(prices):
    lowest_price_so_far = prices[0]
    max_profit = 0

    for price in prices[1:]:
        # check max profit for a day
        max_profit_sell_today = price - lowest_price_so_far

        # update max profit value
        max_profit = max(max_profit, max_profit_sell_today)

        # update lowest price value
        lowest_price_so_far = min(lowest_price_so_far, price)

    return max_profit


if test_result == buy_and_sell_stock_once(test_prices):
    print('Test passed!')

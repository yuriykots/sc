# Write a program that computes the maximum profit that can be made by buying and selling a share at most twice.


test_prices = [12, 11, 13, 9, 12, 8, 14, 13, 15]
test_result = 10


def buy_and_sell_stock_twice(prices):
    max_profit_for_two_sales = 0

    # What is max amount of money you can make selling at particular day
    # 12, 11, 13, 9, 12, 8, 14, 13, 15
    # 0, 0, 2, 2, 3, 3, 6, 6, 7
    # We want to store that information in the array

    max_profit_at_the_day = [0, ]

    min_price_so_far = prices[0]
    max_profit_so_far = 0

    for i in range(1, len(prices)):
        max_profit_at_the_day.append(max(max_profit_so_far, prices[i] - min_price_so_far))

        max_profit_so_far = max(max_profit_so_far, prices[i] - min_price_so_far)
        min_price_so_far = min(min_price_so_far, prices[i])

    # What is max amount of money you can make selling at particular day going backwards
    # 12, 11, 13, 9, 12, 8, 14, 13, 15
    #  7   7   7  7   7  7   2   2   0
    max_price_so_far_backward = 0

    for i in reversed(range(len(prices))):
        # what is the profit on the last day reverse
        max_profit_for_two_sales = max(max_profit_for_two_sales, max_price_so_far_backward - prices[i] + max_profit_at_the_day[i])
        max_price_so_far_backward = max(max_price_so_far_backward, prices[i])

    print(max_profit_for_two_sales)


buy_and_sell_stock_twice(test_prices)

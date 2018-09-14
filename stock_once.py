#!/usr/bin/env python3

def max_profit(prices):
    min_price_so_far = float("inf")
    max_profit_so_far = 0

    for price in prices:
        profit_now = price - min_price_so_far
        max_profit_so_far = max(max_profit_so_far, profit_now)
        min_price_so_far = min(min_price_so_far, price)

    return max_profit_so_far

def max_profit_rev(prices):
    max_price_so_far = float("-inf")
    max_profit_so_far = 0

    for price in reversed(prices):
        profit_now = max_price_so_far - price
        max_profit_so_far = max(max_profit_so_far, profit_now)
        max_price_so_far = max(max_price_so_far, price)

    return max_profit_so_far

def length_of_longest_subarray(x):
    max_length = 1
    last_number_seen = None
    count = 1

    for i in x:
        if i == last_number_seen:
            count += 1
            max_length = max(max_length, count)
        else:
            count = 1
        last_number_seen = i

    return max_length

def max_profit_2x(prices):
    # First, calculate for each day N in [0, len(prices) - 1],
    # the max profit that can be made from day 0 to day N (inclusive).
    # Store the results in an array max_profit_arr.
    #
    # i.e.
    # description of max_profit_arr
    # value at index i -> max profit that can be made starting from day 0
    #                     up to and including day i
    max_profit_arr = []

    min_price_so_far = float("inf")
    max_profit_so_far = 0

    for price in prices:
        profit_now = price - min_price_so_far
        max_profit_so_far = max(max_profit_so_far, profit_now)
        max_profit_arr.append(max_profit_so_far)
        min_price_so_far = min(min_price_so_far, price)

    max_profit_one_sale = max_profit_so_far

    # Let X = len(prices) - 1.
    # Next, iterating from right to left over the same prices array,
    # for each day I in [1, X] (starting from day X, then to day X-1, ..., day 1):
    # calculate the max profit that can be made from day I to day X (inclusive).
    max_price_so_far = float("-inf")
    max_profit_so_far = 0
    # set the initial max profit of two sales to be the max profit of one sale
    max_profit_two_sales = max_profit_one_sale

    plen = len(prices)
    # e.g. range(10 - 1, 0, -1) => [9, 8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(plen - 1, 0, -1):
        price = prices[i]

        # Calculate max profit for right slice
        profit_now = max_price_so_far - price
        max_profit_so_far = max(max_profit_so_far, profit_now)
        max_price_so_far = max(max_price_so_far, price)

        # Calculate max profit that can be made by buying & selling the stock up to two times
        max_profit_two_sales = max(max_profit_two_sales, max_profit_arr[i - 1] + max_profit_so_far)

    return max_profit_two_sales


if __name__ == "__main__":
    prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    #abc = [310, 253, 253, 245, 267, 1, 1, 1, 1, 0, 0, 253, 253, 253, 253]
    prices2 = [12, 11, 13, 9, 12, 8, 14, 13, 15]
    print(max_profit(prices2))
    print(max_profit_2x(prices2))
    #print(length_of_longest_subarray(abc))

"""
Create a function that takes a list of integers that represent the amount in dollars that a single stock is worth,
and return the maximum profit that could have been made by buying stock on day x and selling stock on day y where y>x.

If given the following list:

[44, 30, 24, 32, 35, 30, 40, 38, 15]
... your program should return 16 because at index 2 the stock was worth $24 and at the index 6 the stock
was then worth $40, so if you bought the stock at 24 and sold it on 40, you would have made a profit of $16, which is the maximum profit that could have been made with this list of stock prices.

If there is no profit that could have been made with the stock prices, then your program should return -1
(e.g. [[10, 9, 8, 2]] should return -1).

Examples
stock_picker([10, 12, 4, 5, 9]) ➞ 5

stock_picker([14, 20, 4, 12, 5, 11]) ➞ 8

stock_picker([80, 60, 10, 8]) ➞ -1

From: https://edabit.com/challenge/DqLngKnnJcZyPMctn
"""

# Note: First example is exponential time complexity

def stock_picker(arr):
    if len(arr) < 2:
        return "Error"
    low_value = arr[0]
    high_value = arr[1]
    # for i in range(2, len(arr)):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (arr[j] - arr[i]) > (high_value - low_value):
                if arr[j] > high_value:
                    high_value = arr[j]
                else:
                    low_value = arr[i]
    # print(high_value)
    # print(low_value)
    return (high_value - low_value)

print(stock_picker([10, 12, 4, 5, 9]))
print(stock_picker([14, 20, 4, 12, 5, 11]))

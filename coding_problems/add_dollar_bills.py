"""
Create a function that takes a string containing money in dollars and pounds sterling (seperated by comma) and returns the sum of dollar bills only, as an integer.

For the input string:

Each amount is prefixed by the currency symbol: $ for dollars and £ for pounds.
Thousands are represented by the suffix k.
i.e. $4k = $4,000 and £40k = £40,000

Examples
add_bill("d20,p40,p60,d50") ➞ 20 + 50 = 70

add_bill("p30,d20,p60,d150,p360") ➞ 20  + 150 = 170

add_bill("p30,d2k,p60,d200,p360") ➞ 2 * 1000 + 200 = 2200
"""

def add_bill(string):
    ret = 0
    parsed_array = string.split(",")
    for item in parsed_array:
        if item[0] == "d":
            if item[-1] == "k":
                ret += int(item[1:-1]) * 1000
            else:
                ret += int(item[1:])
    return ret

print(add_bill("d20,p40,p60,d50"))
print(add_bill("p30,d20,p60,d150,p360"))
print(add_bill("p30,d2k,p60,d200,p360"))

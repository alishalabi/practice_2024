"""
Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

Examples
format_date("11/12/2019") ➞ "20191211"

format_date("12/31/2019") ➞ "20193112"

format_date("01/15/2019") ➞ "20191501"

From: https://edabit.com/challenge/co4nwXSvnCjGEu8vp
"""

def format_date(date):
    split_string = date.split("/")
    ret = str(split_string[2]+split_string[1]+ split_string[0])
    return ret

print(format_date("11/12/2019"))
print(format_date("12/31/2019"))
print(format_date("01/15/2019"))

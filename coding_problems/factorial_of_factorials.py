"""
Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:

Examples
fact_of_fact(4) ➞ 288
# 4! * 3! * 2! * 1! = 288

fact_of_fact(5) ➞ 34560

fact_of_fact(6) ➞ 24883200
"""

def factorial(number):
    ret = 1
    current = number
    while current > 1:
        ret = ret * current
        current -= 1
    return ret

def fact_of_fact(number):
    ret = 1
    current = number
    while current > 1:
        ret = ret * factorial(current)
        current -= 1
    return ret


print(fact_of_fact(4))
print(fact_of_fact(5))
print(fact_of_fact(6))

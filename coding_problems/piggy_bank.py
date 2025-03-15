"""
John wants to save money for his first car. He puts money in his piggy bank every day.
Every day, he puts in $1 more than the previous day. Every Monday he starts with a new value ⁠— $1 more than the previous Monday.

Week 1 (starting at $1)
Day	Amount	Sum
Monday	$1	$1
Tuesday	$2	$3
Wednesday	$3	$6
Thursday	$4	$10
Friday	$5	$15
Saturday	$6	$21
Sunday	$7	$28

Week 2
Day	Amount	Sum
Monday	$2	$30
Tuesday	$3	$33
Wednesday	$4	$37
etc ...

Write a function that returns the number of days he needs to buy his first car cost. John had some savings (include it before counting). On the first Monday, he puts the start amount into his piggy bank.

Examples
num_of_days(2050, 1200, 10) ➞ 53
# 2050: cost of car, 1200: savings, 10: start amount
# After 53 days he can buy a car.

num_of_days(10000, 2500, 50) ➞ 123
# After 123 days he can buy a car.

num_of_days(500, 300, 50) ➞ 4
# After 4 days he can buy a car.
"""

def num_of_days(cost, savings, initial_amt):
    days = 0
    daily_saving = initial_amt
    total_saved = 0
    while total_saved + savings < cost:
        days += 1
        if days % 7 == 0:
            daily_saving = daily_saving - 5
            total_saved += daily_saving
        else:
            daily_saving += 1
            total_saved += daily_saving
    return days

print(num_of_days(2050, 1200, 10))
print(num_of_days(10000, 2500, 50))
print(num_of_days(500, 300, 50))

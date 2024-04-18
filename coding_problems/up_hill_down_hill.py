"""
If a person traveled up a hill for 18mins at 20mph and then traveled back down the same path at 60mph then their average speed traveled was 30mph.

Write a function that returns the average speed traveled given an uphill time, uphill rate and a downhill rate. Uphill time is given in minutes. Return the rate as an integer (mph). No rounding is necessary.

Examples
ave_spd(18, 20, 60) ➞ 30

ave_spd(30, 10, 30) ➞ 15

ave_spd(30, 8, 24) ➞ 12

From: https://edabit.com/challenge/NYEaXXCnSj9jteNWA
"""

def ave_spd(uphill_time, uphill_speed, downhill_speed):
    # Find one way distance
    distance = (uphill_time / 60) * uphill_speed
    # Calculate time it takes to travel distance downhill
    downhill_time = distance / downhill_speed
    # Add uphill and downhill time, divide double distance by that number
    average_speed = distance * 2 / (downhill_time + (uphill_time / 60))
    return average_speed

print(ave_spd(18, 20, 60))
print(ave_spd(30, 10, 30))
print(ave_spd(30, 8, 24))

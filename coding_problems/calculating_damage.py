"""
Create a function that takes damage and speed (attacks per second)
and returns the amount of damage after a given time.

Examples
damage(40, 5, "second") ➞ 200

damage(100, 1, "minute") ➞ 6000

damage(2, 100, "hour") ➞ 720000

Problem from: https://edabit.com/challenge/HSHHkdRYXfgfZSqri

"""

def calculate(damage, time, unit):
    allowed_times = ("second", "minute", "hour")
    if unit not in allowed_times:
        return "Invalid time unit"
    if unit == "second":
        multiplier = 1
    elif unit == "minute":
        multiplier = 60
    elif unit == "hour":
        multiplier = 360
    else:
        return "Invalid time unit"
    total_damage = damage * time * multiplier
    return total_damage


print(calculate(40, 5, "second"))
print(calculate(100, 1, "minute"))
print(calculate(2, 100, "hour"))

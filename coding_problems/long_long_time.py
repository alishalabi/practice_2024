"""
Create a function that takes three values:

h hours
m minutes
s seconds
Return the value that's the longest duration.

Examples
longest_time(1, 59, 3598) ➞ 1

longest_time(2, 300, 15000) ➞ 300

longest_time(15, 955, 59400) ➞ 59400
"""

def longest_time(hours, minutes, seconds):
    hours_converted = hours * 60 * 60
    minutes_converted = minutes * 60
    sorted_values = [hours_converted, minutes_converted, seconds]
    sorted_values.sort()
    if sorted_values[2] == hours_converted:
        return hours
    if sorted_values[2] == minutes_converted:
        return minutes
    else:
        return seconds


print(longest_time(1, 59, 3598))
print(longest_time(2, 300, 15000))
print(longest_time(15, 955, 59400))

"""
A pie chart is a circular graphical representation of a dataset, where each category frequency is represented by a slice (or circular sector) with an amplitude in degrees given by the single frequency percentage over the total of frequencies. You can obtain the degrees of sectors following these steps:

Calculate frequencies total.
Calculate percentage of every category frequency dividing it by the frequencies total.
Transform every percentage in degrees multiplying it for 360.
You are given a dictionary data with keys being the data categories (represented by letters) and values being the data frequencies. Implement a function that returns a map to design a pie chart, like to say the same dictionary with values transformed in degrees instead of frequencies. Round final values to the nearest tenth.

Examples
pie_chart({ "a": 1, "b": 2 }) ➞ { "a": 120, "b": 240 }

pie_chart({ "a": 30, "b": 15, "c": 55 }) ➞ { "a": 108, "b": 54, "c": 198 }

pie_chart({ "a": 8, "b": 21, "c": 12, "d": 5, "e": 4 }) ➞ { "a": 57.6, "b": 151.2, "c": 86.4, "d": 36, "e": 28.8 }
"""

def pie_chart(my_map):
    total = 0
    ret = {}
    for key in my_map:
        total += my_map[key]
    for key in my_map:
        portion = round(my_map[key] / total * 360, 1)
        ret[key] = portion
    return ret

print(pie_chart({ "a": 1, "b": 2 }) )
print(pie_chart({ "a": 30, "b": 15, "c": 55 }))
print(pie_chart({ "a": 8, "b": 21, "c": 12, "d": 5, "e": 4 }))

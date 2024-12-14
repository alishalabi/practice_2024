"""
Create a function that emulates the .title() function.
"""

def my_title(word):
    lower_case = word.lower()
    ret = str(lower_case[0].upper() + lower_case[1:])
    return ret

print(my_title("HAPPY"))
print(my_title("gilmore"))

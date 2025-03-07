"""
Create a function that takes a string txt and censors any word from a given list lst.
The text removed must be replaced by the given character char.

Examples
censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")

censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"
"""

def censor_string(string, censor_array, censor_char):
    parsed_array = string.split()
    ret_array = []
    for word in parsed_array:
        if word in censor_array:
            new_word = censor_char * len(word)
            ret_array.append(new_word)
        else:
            ret_array.append(word)
    ret = " ".join(ret_array)
    return ret


print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))

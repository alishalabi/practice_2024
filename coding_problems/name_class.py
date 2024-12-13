"""
Write a class called Name and create the following attributes given a first name and last name (as fname and lname):

An attribute called fullname which returns the first and last names.
An attribute called initials which returns the first letters of the first and last name. Put a . between the two letters.
Remember to allow the attributes fname and lname to be accessed individually as well.

Examples
a1 = Name("john", "SMITH")
a1.fname ➞ "John"

a1.lname ➞ "Smith"

a1.fullname ➞ "John Smith"

a1.initials ➞ "J.S"
"""

class Name:
    def __init__(self, firstname, lastname):
        self.fname = firstname.title()
        self.lname = lastname.title()
        self.fullname= f"{self.fname} {self.lname}"
        self. initials = f"{self.fname[0]}.{self.lname[0]}."

a1 = Name("john", "SMITH")
print(a1.fname)
print(a1.lname)
print(a1.fullname)
print(a1.initials)

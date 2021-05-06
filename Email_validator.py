#Import the re(regex) module
import re

#Declare a variable for pattern check
check_pattern = '^(\w|\.|\-)+[@]+(\w|\.|\-)+[.]\w{2,4}$'

#Create a function to check for valid email addresses
def validate(email):
    if(re.search(check_pattern, email)):
        print('Valid Email')
    else:
        print('Invalid Email')
    return validate







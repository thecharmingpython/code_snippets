# Creating passwords is a boring activity 
# This simple script makes a password of 16 random characters

import random
import string
#create a string of all letters, numbers and punctuation from which to create a password
total = string.ascii_letters + string.digits + string.punctuation
length = 16
password = "".join(random.sample(total, length))
print(password)
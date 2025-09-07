
import random
import string 

Uplet = string.ascii_uppercase
Lolet = string.ascii_lowercase
number = string.digits
special = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

allchar = Uplet + Lolet + number + special

randomnum = ''.join(random.choices(allchar, k=12))


print(randomnum)




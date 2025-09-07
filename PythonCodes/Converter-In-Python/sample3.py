import secrets 
import string 
allchar = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?/"
random_secure = ''.join(secrets.choice(allchar) for _ in range(10)) 
print (random_secure)

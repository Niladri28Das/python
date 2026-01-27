# password generator 

import string 
import random

# for generating a random pasword of 12 characters 

def generate_password(lenght=12):
    # our character pool
    chars = string.ascii_letters + string.digits + string.punctuation

    #pick random characters "lenght" times
    password =''.join(random.choice(chars) for _ in range(lenght))
    return password

print(generate_password())
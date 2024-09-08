#Possward Generator
import string
import random
len = int(input("Select length of the password: "))
a = string.ascii_uppercase
b = string.ascii_lowercase
c = string.digits
d = string.punctuation
combine = a+b+c+d
x = random.sample(combine,len)
print("Your password is:", "".join(x))

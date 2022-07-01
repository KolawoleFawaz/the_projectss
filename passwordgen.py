import random
import string

total = string.ascii_letters + string.digits + string.punctuation

length = int(input("Type password Length: "))

password = "".join(random.sample(total, length))

print("Your generated password is " + password)
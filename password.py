import random 
import string 

print("Password Generator")

length = int(input("Password length: "))

characters = string.ascii_letters + string.digits + "!@#$%^&*"

password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:")
print(password)

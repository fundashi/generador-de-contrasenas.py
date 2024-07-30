import random


characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = int(input("Introduce la longitud de la contraseña: "))

generated_password = ""

for _ in range(password_length):
    generated_password += random.choice(characters)

print("Tu contraseña generada es:", generated_password)
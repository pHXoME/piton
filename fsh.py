import random
lenght = 6
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.!'^^+%&/()=?"
apass =random.choices(characters,k=lenght)
print("".join(apass))
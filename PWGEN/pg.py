import random
import string
alphabets = string.ascii_letters
digits = string.digits
symbols = string.punctuation
print("********************* Password Generator *********************\n")
alpha = int(input("Enter the number of alphabets to be include in the password : \n"))
digi = int(input("Enter the number of digits to be include in the password : \n"))
symb = int(input("Enter the number of symbols to be include in the password : \n"))
PW = []
for i in range(1, alpha + 1):
    char = random.choice(alphabets)
    PW += char
for i in range(1, digi + 1):
    char = random.choice(digits)
    PW += char
for i in range(1, symb + 1):
    char = random.choice(symbols)
    PW += char
random.shuffle(PW)
Password = ""
for char in PW:
    Password += char 
print(f"\nYour password is : {Password}")
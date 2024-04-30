#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

x=""
for item in range(1,nr_letters+1):
    x+=letters[random.randint(0,len(letters)-1)]

for item in range(1,nr_symbols+1):
    x+=symbols[random.randint(0,len(symbols)-1)]

for item in range(1,nr_numbers+1):
    x+=numbers[random.randint(0,len(numbers)-1)]


# random.shuffle(x)
# print(x)
s_shuffled = ''.join(random.sample(x, len(x)))
print(f"Your password may be : {s_shuffled}")

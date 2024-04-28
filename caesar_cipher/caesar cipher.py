import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

c=True
def caesar(text,shift,direction):
    if shift>=26:
      shift=shift%26
    y=""
    for letter in text:
      if letter==' ':
        y+=' '
      elif letter.isnumeric():
        y+=letter
      else:
        x=alphabet.index(letter)
        if direction=="encode":
          y+=alphabet[x+shift]
        elif direction=="decode":
          y+=alphabet[x-shift]
        else:
          print("Invalid input")
    print(y)
while c==True:  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text,shift,direction)
  res=input("Would you like to restart the program? type 'yes' or 'no'")
  if res=="no":
    c=False
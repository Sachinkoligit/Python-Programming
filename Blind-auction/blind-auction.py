import art
#from replit import clear
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
bidders={}
print("Welcome to the secret auction program.")
name=input("What is your name?:")
bid=int(input("What's your bid?: $"))
bidders[name]=bid
c=True
while c==True:
  x=input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if x=='yes':
    #clear()
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    bidders[name]=bid
  else:
    c=False
max=0
maxp=""
for h in bidders:
  if max<bidders[h]:
    max=bidders[h]
    maxp=h
print(f"The Winner is {maxp} with a bid of ${max}")
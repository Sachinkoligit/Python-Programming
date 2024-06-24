import random
import  nineart
def deal_card():
   cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
   x=(cards[random.randint(0,12)])
   return x

def cal_score(x):
   sum=0
   for item in x:
      item=int(item)
      sum+=item
   if sum==21:
      for item in x:
         if item==11:
            x.remove(11)
            x.append(1)
      return sum
   else:
        return sum

user_cards=[]
computer_cards=[]

print(nineart.x)
for _ in range(2):
   user_cards.append(deal_card())
computer_cards.append(deal_card())
print(f"The user cards are: {user_cards} and the sum is: {cal_score(user_cards)}")
print(f"The comp. cards are: {computer_cards} and the sum is: {cal_score(computer_cards)}")
ch='T'
res='F'
while ch=='T':
   x=input("Type Stand or Pass? s or p:")
   if x=='s' and cal_score(user_cards)<21:
      user_cards.append(deal_card())
      if cal_score(user_cards)>21:
         print("Dealer's Win..")
         res='T'
         break
      print(f"The user cards are: {user_cards} and the sum is: {cal_score(user_cards)}")
   elif x=='p':
      while cal_score(computer_cards)<=18:
         computer_cards.append(deal_card())
         print(f"The comp. cards are: {computer_cards} and the sum is: {cal_score(computer_cards)}")
         if cal_score(computer_cards)>21:
            print("You Win..")
            res='T'
            break
      ch='F'
   else:
      print("Invalid choice.")

if res!='T':
   if cal_score(user_cards)>=cal_score(computer_cards) and cal_score(user_cards)<=21:
      print("You Win..")   
   else:
      print("Dealer's Win..")

print(f"The user cards are: {user_cards} and the sum is: {cal_score(user_cards)}")
print(f"The comp. cards are: {computer_cards} and the sum is: {cal_score(computer_cards)}")
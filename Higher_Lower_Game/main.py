import art
import game_data
import random
print(art.logo)

score=0
status='T'
while  status!='F':
  A=random.choice(game_data.data)
  B=random.choice(game_data.data)

  while A==B:
    B=random.choice(game_data.data)

  print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")      
  

  print(f"{art.vs}")

  print(f"\nCompare B: {B['name']}, {B['description']}, from {B['country']}")  
  

  x=input("Who has more Followers? Type 'A' or 'B': ")

  if x=='A' and  A['follower_count']>B['follower_count']:
    score+=1
    print(f"You're right! Current score: {score}")
    status='T'
    
  elif x=='A' and  A['follower_count']<B['follower_count']:
    print(f"You're Wrong! Current score: {score}")
    status='F'
    break

  elif x=='B' and  A['follower_count']<B['follower_count']:
    score+=1
    print(f"You're right! Current score: {score}")
    status='T'
    
  else:
    print(f"You're Wrong! Current score: {score}")
    status='F'

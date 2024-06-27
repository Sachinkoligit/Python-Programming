from coffee import MENU
from coffee import resources
from coffeeart import art

def report():
    for key in resources:
        if key=='coffee':
            print(f"{key}: {resources[key]}g")
        elif key=='money':
            print(f"{key}: ${resources[key]}")
        else:
            print(f"{key}: {resources[key]}ml")

def change(x,y,z,p,rate):
    total=x*0.25+y*0.10+z*0.05+p*0.01
    if rate>total:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change=total-rate
        print(f"Here is ${change} in change")
        return True

def res(x):
        resources['water']=resources['water']-MENU[x]['water']
        resources['milk']=resources['milk']-MENU[x]['milk']
        resources['coffee']=resources['coffee']-MENU[x]['coffee']
        resources['money']=resources['money']+MENU[x]['cost']

def check(resources,x):
    z=['water','milk','coffee']
    for l in z:
        if resources[l]<MENU[x][l]:
            break
    if  resources['water']>=MENU[x]['water'] and resources['milk']>=MENU[x]['milk']and resources['coffee']>=MENU[x]['coffee']:
        return True
    else:
        print(f"Sorry there is not enough {l}")
        return False   

print(f"{art}\n")
x1=1
while x1!=0:
    x=input("What would you like? (espresso/latte/cappuccino): ")
    if x=='report':
        report() 
    else:
        q=check(resources,x)
        if q==True:
            print("Please insert coins.")
            quarters=int(input("How many quarters?: "))
            dimes=int(input("How many dimes?: "))
            nickles=int(input("How many nickles?: "))
            pennies=int(input("How many pennies?: "))

            p=change(quarters,dimes,nickles,pennies,MENU[x]['cost'])
            if p==True:
                res(x)
            else:
                x1=0
        else:
            x1=0
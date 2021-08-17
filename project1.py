import random

def gamewin(comp,you):
    if comp==you:
        None
    if comp=='s' :
        if you=='w':
            return False
        else:
            if you=='g':
                return True
    elif comp=='w':
        if you=='g':
            return False
        else:
            if you=='s':
                return True
    else:
        if comp=='g':
            if you=='w':
                return False
            else:
                if you=='s':
                    return True


print("Computer's turn: Snake(s) Water(w) or Gun(g) ?")
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
else:
    comp='g'        

you=input("Player 1 turn: Snake(s) Water(w) or Gun(g) ?")
r=gamewin(comp,you)

print(f"Computer choose {comp}")
print(f"You choose {you}")
if r==None:
    print("Draw")
elif r:
    print("You lose")
else:
    print("You win")        

import random

def game(comp,You):
    if comp == You:
        return None
    if comp== 'S':
        if You == 'P':
            return False
        elif You == 'SS':
            return True

    elif comp== 'P':
        if You == 'SS':
            return False
        elif You == 'S':
            return True

    elif comp== 'SS':
        if You == 'S':
            return False
        elif You == 'P':
            return True


ran= random.randint(1,3)
if ran == 1:
    comp ='S'
elif ran == 2:
    comp ='P'
elif ran == 3:
    comp ='SS'


You= input("Your turn:Stone(S), Paper(P) or Scissors(SS)")

a= game(comp,You)

print(f"You chose {You} and computer chose {comp}")
if a==None:
    print("IT IS A TIE!")
elif a==False:
    print("You Win!")
if a==True:
    print("You loses!")

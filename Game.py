
import random

def play():
    user=input("What's your choice? \n'r' for rock, 'p' for paper and 's' for scissors\n")
    computer =random.choice(['r','p','s'])
    print("computer's choice is : ",computer)
    
    if user==computer:  #same chioce tie
        return 'tie'
 # r>s, s>p,  p>r    
    if is_win(user, computer):
        return "You won!!"
                      #if is_win(computer,user):   if true ---prints u lost
    return "You lost!"

def is_win(player,opponent):
    
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True

print(play())    #func call
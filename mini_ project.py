import random
def game(li):
    n=int(input("give total number of games"))
    print(n)
    l=""
    user_won=0
    system_won=0
    for i in range(n):
        if i<n:
            print("entering into game:", i+1)
            l=(input())
            print("user input is:",l)
            a=random.choice(li)
            print("system input is:",a)
            if a==l or l==a:
                print("tie, no points for user and system")
            elif l=="paper" and a=="rock":
                user_won=user_won+1
                print("user points are:",user_won)
                print("system points are:",system_won)
            elif  l=="scissor" and a=="rock":
                system_won=system_won+1
                print("system points are:",system_won)
                print("user points are:",user_won)
            elif l=="scissor" and a=="paper":
                user_won=user_won+1
                print("user points are:",user_won)
                print("system points are:",system_won)
            elif  l=="rock" and a=="paper":
                system_won=system_won+1
                print("system points are:",system_won)
                print("user points are:",user_won)
            elif  l=="rock" and a=="scissor":
                user_won=user_won+1
                print("user points are:",user_won)
                print("system points are",system_won)
            elif l=="paper" and a=="scissor":
                system_won=system_won+1
                print("system pints are:",system_won)
                print("user points are:",user_won)
            else:
                print("invalid input")
    else:
         print("number of games finished")
    if user_won > system_won:
        print("congratulations......user won the game")
    elif user_won==system_won:
        print("its a tie game")
    else:
        print("congratulations....system won the game")
li=["rock","paper","scissor"]
game(li)

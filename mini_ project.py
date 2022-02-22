import random
l1=["rock","paper","scissor"]

def game(li):
    n=int(input("give total number of games"))
    print(n)
    li=""
    for i in range(n):
        if i<n:
            print("entering into game:", i+1)
            li=(input())
            a=random.choice(l1)
            print(a)
            if a==li or li==a:
                print("tie game")
            elif li=="paper" and a=="rock":
                print("user  won")
            elif  li=="scissor" and a=="rock":
                print("system  won")
            elif li=="scissor" and a=="paper":
                print("user won")
            elif  li=="rock" and a=="paper":
                print("system won")
            elif  li=="rock" and a=="scissor":
                print("user won")
            elif li=="paper" and a=="scissor":
                print("system won")
            else:
                print("invalid input")
    else:
            print("number of games finished")
li=["rock","paper","scissor"]
game(li)

output:

give total number of games4
4
entering into game: 1
rock
scissor
user won
entering into game: 2
paper
rock
user  won
entering into game: 3
scissor
rock
system  won
entering into game: 4
rock
scissor
user won
number of games finished

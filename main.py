import os
from random import randint
from time import sleep

def clear():
  os.system('cls')

#######    Your code here    #######
score = 1500
cost = 100
payout = 0
print("Welcome to the slot machine!")
start = input("Do you want to play? (y or n) ")
if start == "y":
  while score >= cost:
    sleep(0.4)
    score = score - cost
    slot = [[1,2,3],[4,5,6,],[7,8,9]]
    for i in range(len(slot)):
        for j in range(len(slot[i])):
            slot[i][j] = randint(1,6)
    for row in slot:
        for num in row:
          print(f"|{num}|",end="")
        print()
    if slot[0][0] == slot[0][1] and slot[0][0] == slot[0][2]:
       print("JACKPOT!!!")
       print("You earned 1000 more score!!!")
       score = score + 1000
    if slot[1][0] == slot[1][1] and slot[1][0] == slot[1][2]:
       print("JACKPOT!!!")
       print("You earned 1000 more score!!!")
       score = score + 1000
    if slot[2][0] == slot[2][1] and slot[2][0] == slot[2][2]:
       print("JACKPOT!!!")
       print("You earned 1000 more score!!!")
       score = score + 1000
    if slot[0][0] == slot[1][1] and slot[0][0] == slot[2][2]:
       print("JACKPOT!!!")
       print("You earned 1000 more score!!!")
       score = score + 1000
    if slot[2][0] == slot[1][1] and slot[2][0] == slot[0][2]:
       print("JACKPOT!!!")
       print("You earned 1000 more score!!!")
       score = score + 1000
    play = input("Do you want to play again? (y or n): ")
    if play.lower() == "y":
      continue
    if play.lower() == "n":
      break
  print("Thanks for playing")
if start == "n":
   print("Then get out of here.")
if score < cost:
   print("Sorry, you can't play any more since you ran out of score.")
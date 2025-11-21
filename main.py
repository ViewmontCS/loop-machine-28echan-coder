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
while score >= cost:
  sleep(0.8)
  score = score - cost
  slot = [[1,2,3],[4,5,6,],[7,8,9]]
  for row in slot:
      for num in row:
          num = randint(1,9)
          print(f"|{num}|",end="")
      print()

slot = [[num, num, num][num, num, num][num, num, num]]
if slot[0][0] == slot[0][1] == slot[0][2]:
  print("hooray")

  play = input("Do you want to play again? (y or n): ")
  if play.lower() == "y":
     continue
  if play.lower() == "n":
    break
  print("Thanks for playing")
if score < cost:
   print("Sorry, you can't play any more since you ran out of score.")
'''

overveiw
one player gusses the word and the other player gusses aleter
and the gussed leter if present in the word  will be repleced on its postion in the word
untill the hangman produced
if the hangman is producded before all space are filled the game over and the player lose
if  the space are all fill ed before all leters in the word replace
thethe game over and the player lose
'''

import random
list_word=["apple","banana","mango",'cats',"monkey","tree","hangman"]
gussed_word=random.choice(list_word)
space=[]
for i in gussed_word:
    space.append('_')
lives=6

#print(gussed_word)
game_over=False
print("Welcome to Hangman game! Good lack")
while not game_over:
    print(space)
    gussed_letter=input("Guss the letter!").lower()
    if gussed_letter in gussed_word:
      if gussed_letter in space:
          print("Please gusee another leter")
      else:
         for i in range(len(gussed_word)):
            if gussed_letter==gussed_word[i]:
                space[i]=gussed_letter

         if "_" not in space:
            game_over=True
            print(space)
            print("You win!!")
    else:
        lives-=1
        if lives==0:
            game_over=True
            print("You lose!!")







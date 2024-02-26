import random  #for random selection of words
import hangman_stages #importing hangman stages that contains stages of hangman
import hangmanwords #to import the module that contains the list of words 
lives = 6  #no of lives a player has 
chosen_word = random.choice(hangmanwords.words) #pick any randon word from list and store in  a variable chosen word
print(chosen_word)
display = ['_'] * len(chosen_word) #creating a list called display 
game_over = False
#starting the loop
while not game_over: # while  game_over is true guess a letter   
    guessed_letter = input("guess a letter: ").lower() #input from the user stored under the variable guessed_letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] =guessed_letter #
    if guessed_letter not in chosen_word:
        lives -= 1   #a life is lost for every wrong guess
        if lives == 0:
            game_over = True
            print("you lose!!")
    if'_' not in display:
        game_over = True 
        print("you win")       
print(hangman_stages.stages[lives])
       

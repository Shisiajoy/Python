

import random
print("Welcome to Snake and Ladder Game.")
print("Version: 1.0.0  *Feel Free to use anything*")

player1 = input("player 1 enter your name:")
player2 = input("player 2 enter your name:")

#initialize positions for both player
position1 = 0   #player 1s position
position2 = 0   #player 2s position
i=1             #counter to track turns

#loop continues until either players reaches or exceeds 25
while(position1<=25 or position2<=25):

    if(i%2==0):  # determine whose turn it is based on value of i i.e.  player 1's turn if i is even

        r1 = random.randint(1,3)   #randint() is a method within the random module that generates a random integer within a range
        turn = input("player 1 your turn")
        print ("your rolled = ",r1)
        position1 = position1 + r1
        print ("your position = ",position1)
        i = i+1  #incremented by 1 after each iteration of game loop

                #ladder
        if (position1 == 7):
            position1 = 17
            print ("you get a ladder to position 17")
        if(position1 == 14):
            position1 = 19
            print ("you get a ladder to position 19")

            #snakes
        if (position1 == 24):
            position1 = 2
            print ("you got snaked to position 2")
        if (position1 == 16):
            position1 = 4
            print ("you got snaked to position 4")
        if (position1 == 20):
            position1 = 6
            print ("you got snaked to position 6")

        if (position1 >= 25):
            print (player1, "congratulations you won!")

            break #break out of the loop if pos1 >=25


        #player 2s turn
    else:
        r2 = random.randint(1,3)   #randint() is a method wuthin the random module that generates a random integer within a range(1.3(ranges from 1 to 2 not including 3))
        turn = input("player 2 your turn :")
        print("your rolled = ",r2)
        position2 = position2 + r2
        print ("your position = ",position2)
        i = i+1

            #ladder
        if (position2 == 7):
            position2 = 17
            print ("you get a ladder to position 17")
        if(position2 == 14):
            posotion2 = 19

            #snakes
            print ("you get a ladder to position 19")
        if (position2 == 24):
            position2 = 2
            print ("you got snaked to position 2")
        if (position2 == 16):
            position2 = 4
            print ("you got snaked to position 4")
        if (position2 == 20):
            position2 = 6
            print ("you got snaked to position 6")

        if (position2 >= 25):
            print (player2, "congratulations you won!")

            break
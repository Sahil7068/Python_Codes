### SL WORLD ###

print('''       
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )⠁   \n\n\n''')




print("Welcome to SL World !")
print("Kin, save your queen")

choice_1 = input('You are about to enter the game! Make your choice "forest" or "city" ').lower()
if choice_1 == "forest":
    choice_2 = input('Welcome to the forest, choose your way "mountain" or "river" ').lower()
    if choice_2 == "river":
        choice_3 = input('Welcome to the amazon, choose your ride "boat" or "turtle" ').lower()
        if choice_3 == "turtle":
            choice_4 = input('You have made to the castle! choose the door "red" "green" "pink" ').lower()
            if choice_4 == "red":
                print("GAME OVER! you are finished by the fire")
            elif choice_4 == "green":
                print("Congratulation! You saved the queen. YOU WIN! ")
            elif choice_4 == "pink":
                print("You are eaten by a pig. GAME OVER!")
        else:
           print("Your boat drowns, GAME OVER!")
    else:
        print("You fell down from the mountain, GAME OVER!")
else:
    print("You have chosen the wrong way. GAME OVER!")
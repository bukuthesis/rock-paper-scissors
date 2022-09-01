#rock,paper,scissors

import random
print("Rules:\n"
      +"rock vs paper -> paper wins \n"
      +"rock vs scissor -> rock win \n"
      +"scissor vs paper -> scissors win \n")

while True:
    print("Enter choice \n 1. for rock, \n 2. for paper, \n 3. for scissor")
    choice = int(input("User Turn: "))

    #Loop until user inputs invalid value

    while choice > 3 or choice < 1:
        choice = int(input("Invalid input, Enter valid input: "))

    if choice == 1:
        choice_name =  'rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'

    #print the users choice
    print("User choice: " + choice_name)
    print("\ncomputers turn..... \n")

    mac_choice = random.randint(1, 3)
    while mac_choice == choice:
        mac_choice = random.randint(1, 3)

    if mac_choice == 1:
        mac_choice_name = 'rock'
    elif mac_choice == 2:
        mac_choice_name = 'paper'
    else:
        mac_choice_name = 'scissor'
    print("computer is going to play...\n=>" + mac_choice_name + "\n")
    print("{} v/s {}\n".format(choice_name,mac_choice_name))

    if choice == mac_choice:
        result = "Draw"
        print("Draw=>", end = "")

    elif ((choice == 1 and mac_choice == 2) or
        choice == 2 and mac_choice == 1):
            print("paper wins\n", end="")
            result = "paper\n"

    elif ((choice == 1 and mac_choice == 3) or
          (choice == 3 and mac_choice == 1)):
        print("rock wins\n ", end="")
        result = "rock\n"

    else:
        print("scissor wins\n", end="")
        result = "scissor\n"


    print("=>Do you want to play again? (y/n)")
    ans = input()
    if ans == 'n':
        break


print("\nThanks for playing")


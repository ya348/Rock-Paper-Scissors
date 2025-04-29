# Rock-Paper-Scissors

player1 = input('Enter your name Player1 : ')
print("\n Player 1: ", player1 , '\n ----------------------')

# input("Player 1: Rock, Paper, or Scissors?")
player2 = input('Enter your name player2 : ')
print("\n Player 2: ", player2 , '\n ----------------------')

# input("Player 2: Rock, Paper, or Scissors?")

print("Rock = 1 ")
print("Paper = 2 ")
print("Scissors = 3 \n")
print("Shoot!!!!!!! \n" + '------------------')

num__of__play = int(input("How many times do you want to play? "))
print('------------------')

result = 0
player1__ = 0
player2__ = 0


for i in range(0,num__of__play):
    while True:
            try:
                player1__ = int(input(f'{player1} Enter your choice: '))
                if player1__ in [1, 2, 3]:
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    while True:
            try:
                player2__ = int(input(f'{player2} Enter your choice: '))
                if player2__ in [1, 2, 3]:
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
                    
    print('------------------')


    if player1__ == 1 and player2__ == 2:
        print(f'{player2} wins' + '\n------------------')
        player2__ += 1
    elif player1__ == 1 and player2__ == 3:
        print(f'{player1} wins' + '\n------------------')
        player1__ += 1
    elif player1__ == 2 and player2__ == 1:
        print(f'{player1} wins' + '\n------------------')
        player1__ += 1
    elif player1__ == 2 and player2__ == 3:
        print(f'{player2} wins' + '\n------------------')
        player2__ += 1
    elif player1__ == 3 and player2__ == 1:
        print(f'{player2} wins' + '\n------------------')
        player2__ += 1
    elif player1__ == 3 and player2__ == 2:
        print(f'{player1} wins' + '\n------------------')
        player1__ += 1
    else:
        print("It's a tie!"     + '\n------------------') 
        i += 1    
#---------------------------------------------------------

print(f'{player1} wins: ', player1__)
print(f'{player2} wins: ', player2__)


if player1__ > player2__:
    print(f'{player1} wins the game!')
elif player2__ > player1__:
    print(f'{player2} wins the game!')
else:
    print("It's a tie")


print("Thanks for playing!\n " , "Created by ya348")
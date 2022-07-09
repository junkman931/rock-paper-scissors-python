import random

options_list = ['rock', 'paper', 'scissors']
userScore = computerScore = 0
rounds = int(input("Enter number of rounds: "))


for i in range(rounds):

#print(random.choice(options_list))
    computerInput = random.choice(options_list)
    userInput = input("Your choice: ")

    if userInput == computerInput:
        print("It's a tie")
    elif userInput == 'rock' and computerInput == 'scissors':
        userScore += 1
        print("User wins, computer chose " + computerInput)
    elif userInput == 'rock' and computerInput == 'paper':
        computerScore += 1
        print("Computer wins choosing " + computerInput)
    elif userInput == 'paper' and computerInput == 'scissors':
        computerScore += 1
        print("Computer wins choosing " + computerInput)
    elif userInput == 'paper' and computerInput == 'rock':
        userScore += 1
        print("User wins, computer chose " + computerInput)
    elif userInput == 'scissors' and computerInput == 'paper':
        userScore += 1
        print("User wins, computer chose " + computerInput)
    elif userInput == 'scissors' and computerInput == 'rock':
        computerScore += 1
        print("Computer wins choosing " + computerInput)

if userScore > computerScore:
    print("User wins with " + str(userScore) + " and computer lost with " + str(computerScore))
elif userScore < computerScore:
    print("Computer wins with " + str(computerScore) + " and user lost with " + str(userScore))
else:
    print("It is a tie")
import random



rounds = int(input("Enter number of rounds: "))

def play():
    userScore = computerScore = 0
    for i in range(rounds):
        computerInput = random.choice(['rock', 'paper', 'scissors'])
        userInput = input("Your choice: ")

        if userInput == computerInput:
            print("It's a tie")

        if is_win(userInput, computerInput):
            userScore += 1
            print("You win! Computer chose " + computerInput)

        if is_win(computerInput, userInput):
            computerScore += 1
            print("You lost! Computer chose " + computerInput) 

    if computerScore < userScore:
        print("Game ended. You won with " + str(userScore))
    elif computerScore > userScore:
        print("Game ended. Computer won with " + str(computerScore))
    else:
        print("Game ended in tie")
    
def is_win(player, opponent):
    # r > s, s > p, p > r
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True

print(play())

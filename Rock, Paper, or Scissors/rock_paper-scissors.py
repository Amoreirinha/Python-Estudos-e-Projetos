import random

def play():
    print("\n-----------------------------\n")
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])
    print("Computer choice:", computer,"\n")

    if user == computer:
        return 'It\'s a tie\n'
    
    if is_win(user, computer):
        return 'You won!\n'
    
    return 'You lost\n'

def is_win(player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True

while True:
    print(play())
    replay = input("You wana replay?\nType 'y' for yes or 'n' for no\n")
    if replay != 'y':
        break

print("Thanks for playing!")
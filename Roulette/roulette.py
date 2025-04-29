import random

def play():
    print("\n-----------------------------\n")

    valor_coin = 5.00

    valor_aposta = input("Welcome to the roulette!\nHow much do you want to bet? 1 coin = $ " + str(valor_coin) + "\n")

    if not valor_aposta.isdigit():
        return "Please enter a valid number.\n"
    
    valor_aposta = int(valor_aposta)
    
    if valor_aposta % int(valor_coin) != 0:
        return "The value must be a multiple of " + str(valor_coin) + ".\n"
    
    coins = valor_aposta // valor_coin
    print(f"You have {int(coins)} coin(s).\n")

    mode = input ("Select the difficult mode of the game:\nType 'e' for easy mode\nType 'n' for normal mode\nType 'h' to hard mode\n").lower()

    if mode not in ("e", "n", "h"):
        return None, "Por favor, insira uma resposta válida."
    
    if mode == "e":
        possibility = ['1', '2']
        jackpot = 10

    elif mode == "n":
        possibility = ['1', '2', '3']
        jackpot = 100

    elif mode == "h":
        possibility = ['1', '2', '3', '4', '5', '6', '7']
        jackpot = 1000

    user = input("Do you want to spend 1 coin to play?\nType 'y' for yes or 'n' for no\n")
    if user == 'y':
        print("\n-----------------------------\n")
        def game():
            nonlocal coins
            if coins <= 0:
                return "You don't have enough coins to play.\n"
            
            coins -= 1
            print(f"Remaining coins: {int(coins)}\n")
            computer1 = random.choice(possibility)
            computer2 = random.choice(possibility)
            computer3 = random.choice(possibility)
            print("Roulette:", computer1 + computer2 + computer3)

            if computer1 == computer2 == computer3:
                coins += jackpot
                print("\n+"+str(jackpot)+"\n")
                print("Now you have "+str(int(coins))+" coins\n")
                return 'You win!\n'
            
            return 'You lost!\n'

        while coins > 0:
            print(game())
            if coins <= 0:
                print("\n-----------------------------\n")
                return "You have no more coins left.\n"
            replay = input("Do you want to play again?\nType 'y' for yes or 'n' for no\n").lower()
            if replay != 'y':
                break
        
        return "Thanks for playing!"
    return "Bye"

while True:
    print(play())
    replay = input("\n-----------------------------\nDo you want to start a new game?\nType 'y' for yes or 'n' for no\n").lower()
    if replay != 'y':
        break

print("Thanks for playing!")
import random

def rps():
    Bots_score = 0
    Your_score = 0
    
    while True:
        print("\n******************************* Welcome to the -- Rock Paper Scissors -- game *******************************\n")
        choice = "1. Rock\n2. Paper\n3. Scissors\n"
        print(choice)
        
        you = int(input("Please choose the number of your choice: \n"))
        
        if you == 1:
            print("Your choice = Rock\n")
        elif you == 2:
            print("Your choice = Paper\n")
        elif you == 3:
            print("Your choice = Scissors\n")
        else:
            print("Invalid choice, please select again.\n")
            continue
        
        bot = random.randint(1, 3)
        if bot == 1:
            print("Bot's choice = Rock\n")
        elif bot == 2:
            print("Bot's choice = Paper\n")
        elif bot == 3:
            print("Bot's choice = Scissors\n")
        
        if you == bot:
            print("It's a Draw!")
        elif (you == 1 and bot == 3) or (you == 2 and bot == 1) or (you == 3 and bot == 2):
            print("You Win!")
            Your_score += 1
        else:
            print("Bot Wins!")
            Bots_score += 1
        
        print(f"\nYour Score: {Your_score} | Bot's Score: {Bots_score}\n")
        
        play_again = input("Do you want to play again? (Y/N): \n").upper()
        if play_again != "Y":
            print("Goodbye! Thanks for playing.\n")
            break

rps()


    

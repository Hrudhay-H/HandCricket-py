import random
tossChoices = {1:'bat', 0:'bowl'}
def getUserChoice():
    while True:
            choice = int(input("Enter your choice (1-6): "))
            if choice in range(1, 7):
                return choice
            else:
                print("Invalid choice, please enter a number between 1 and 6.")
                getUserChoice()
def computerChoice():
    return random.randint(1, 6)
def plbatting():
    score = 0
    while True:
        plyr = getUserChoice()
        pc = computerChoice()
        print(f"Player chose {plyr}, Computer chose {pc}")
        if plyr == pc:
            print("Player is OUT!")
            break
        else:
            score += plyr
            print(f"Current Score: {score}")
    return score
def pcbatting():
    score = 0
    while True:
        plyr = getUserChoice()
        pc = computerChoice()
        print(f"Player chose {plyr}, Computer chose {pc}")
        if plyr == pc:
            print("Computer is OUT!")
            break
        else:
            score += plyr
            print(f"Current Score: {score}")
    return score
def toss():
    t = random.choice(['h','t'])
    tChoice = input("Heads(H) or Tails(T) : ")
    if(tChoice.lower() == t):
        print("Congratulations! You won the toss")
        plyrChoice = int(input("What would you do first, Bat(1) or Bowl(0) : "))
        print(f"You chose to {tossChoices[plyrChoice]} first")
        if(plyrChoice == 1):
            print("\nPlayer's turn to bat!")
            playerScore = plbatting()
            print(f"Player's final score: {playerScore}")
            print("\nComputer's turn to bat!")
            computerScore = pcbatting()
            print(f"Computer's final score: {computerScore}")
            if playerScore > computerScore:
                print("\nPlayer wins!")
            elif playerScore < computerScore:
                print("\nComputer wins!")
            else:
                print("\nIt's a tie!")
        else:
            print("\nComputer's turn to bat!")
            computerScore = pcbatting()
            print(f"Computer's final score: {computerScore}")
            print("\Player's turn to bat!")
            playerScore = plbatting()
            print(f"Player's final score: {playerScore}")
            if playerScore > computerScore:
                print("\nPlayer wins!")
            elif playerScore < computerScore:
                print("\nComputer wins!")
            else:
                print("\nIt's a tie!")
    else:
        print("Oops! You lost the toss")
        pcChoice = random.choice([0,1])
        print(f"PC chose to {tossChoices[pcChoice]} first")
        if(pcChoice == 1):
            print("\nComputer's turn to bat!")
            computerScore = pcbatting()
            print(f"Computer's final score: {computerScore}")
            print("\Player's turn to bat!")
            playerScore = plbatting()
            print(f"Player's final score: {playerScore}")
            if playerScore > computerScore:
                print("\nPlayer wins!")
            elif playerScore < computerScore:
                print("\nComputer wins!")
            else:
                print("\nIt's a tie!")
        else:
            print("\nPlayer's turn to bat!")
            playerScore = plbatting()
            print(f"Player's final score: {playerScore}")
            print("\nComputer's turn to bat!")
            computerScore = pcbatting()
            print(f"Computer's final score: {computerScore}")
            if playerScore > computerScore:
                print("\nPlayer wins!")
            elif playerScore < computerScore:
                print("\nComputer wins!")
            else:
                print("\nIt's a tie!")
            print("Welcome To PC Version of Hand-Cricket")
def rules():
    print('''RULES:-
    *) Batting and Bowling:
    The bowler "delivers" the ball by choosing a number (usually between 1 and 6)
    The batsman responds simultaneously by choosing a number (also between 1 and 6)
        
    *) Scoring:
    If the number shown by the bowler and the batsman is different, the batsman's score increases by the number of fingers they showed.
    If the number shown by both players is the same, the batsman is considered "out."

    *) Wickets:
    The game continues with the same batsman until they are "out."
    Once out, players swap roles, or the next batsman comes in if there are multiple players.

    *) Winning:
    If playing with a set number of overs, the batsman's objective is to score as many runs as possible in those overs.
    The bowler's goal is to get the batsman out before they can score heavily.
    After the agreed number of overs, players swap roles.
    The player with the highest score wins the game\n''')
x = input("Click '1' if you want to see the rules of the game or any other key to start : ")
if(x == '1'):
    rules()
toss()

import random


def game():
    user = input(
        "What's your choice ? 'r' for Rock , 's' for Scissor or 'p' for Paper \n "
    )
    computer = random.choice(['c', 'r', 's'])
    # r > s , s > p , p > r
    if user == computer:
        print("It's a tie !! ")

    if isWin(user, computer):
        print("You won !! ")
    else:
        print("You loose !! ")


def isWin(choice1, choice2):

    # r > s , s > p , p > r
    if (choice1 == 'r' and choice2 == 's') or (choice1 == 's' and choice2
                                               == 'p') or (choice1 == 'p'
                                                           and choice2 == 'r'):
        return True


if __name__ == "__main__":
    game()
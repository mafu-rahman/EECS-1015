# Lab 4
# Author: Mahfuz Rahman
# Email: mafu@my.yorku.ca
# Student ID: 217847518

import random

def drawcards():
    card1 = random.randint(2, 14)
    card2 = random.randint(2, 14)

    if card1 >= card2:            # Returning the card values in order
        return card1, card2
    elif card1 < card2:
        return card2, card1


def card2str(s):
    if s >= 2 and s <= 10:       # Returning the card as a string number
        return str(s)
    else:
        if s == 11:              # Returning string equivalent
            return "J"
        elif s == 12:
            return "Q"
        elif s == 13:
            return "K"
        elif s == 14:
            return "A"


def printhand(card1, card2, player):
    card1 = card2str(card1)
    card2 = card2str(card2)
    if player == "user":            # Distinguishing the player
        print(f"[{card1}] [{card2}] Your Cards")
    elif player == "comp":
        print(f"[{card1}] [{card2}] Computer's Cards")


def printoutcome(user_card1, user_card2, comp_card1, comp_card2):
    user_card1, user_card2 = drawcards()
    comp_card1, comp_card2 = drawcards()

    printhand(user_card1, user_card2, player="user")
    printhand(comp_card1, comp_card2, player="comp")

    winner = ""  # To store the winner

    if user_card1 == user_card2 and comp_card1 == comp_card2:  # If both players have a pair
        if user_card1 > comp_card1:
            winner = "user"
        elif user_card1 < comp_card1:
            winner = "comp"
        elif user_card1 == comp_card1 and user_card2 == comp_card2:  # If its a tie
            winner = "tie"

    elif user_card1 == comp_card1 and user_card2 == comp_card2:  # When all the cards are equal (Tie)
        winner = "tie"

    elif user_card1 == user_card2 and comp_card1 != comp_card2:  # If user has a pair
        winner = "user"

    elif comp_card1 == comp_card2 and user_card1 != user_card2:  # If computer has a pair
        winner = "comp"

    elif user_card1 != user_card2 and comp_card1 != comp_card2 and user_card1 != comp_card1:  # If neither has a pair
        if user_card1 > comp_card1:
            winner = "user"
        else:
            winner = "comp"

    elif user_card1 == comp_card1 and user_card2 != comp_card2:  # If both players highest card is the same
        if user_card2 > comp_card2:
            winner = "user"
        else:
            winner = "comp"

    if winner == "user":
        print("""You Win !
           """)
    elif winner == "comp":
        print("""Computer Wins
           """)
    elif winner == "tie":
        print("""Tie
           """)


def main():
    input("""-----> Two Card Poker Game <-----
    Press ENTER to Start
    """)
    play = "Y"
    while play.upper() != "N":
        printoutcome(1, 2, 3, 4)    # Passing initial parameter values
        play = input("Want to play again ? Y/N ")
        print("-------------------------")
    input("""*** Thank You for playing ! ***
    Press Enter to exit""")

if __name__ == '__main__':
    main()


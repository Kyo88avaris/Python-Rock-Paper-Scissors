"""
Simple Rock Paper Scissors Game

Rock > Scissors
Paper > Rock
Scissors > Paper

Generate Counters for wins / losses / ties
"""
import random

class Player():

    def __init__(self, name):
        self.name = name
        self.win = 0
        self.loss = 0
        self.ties = 0
        self.rock = 0
        self.paper = 0
        self.scissors = 0

    def update_stats(self,outcome,hand):
        if outcome.lower() == 'win':
            self.win += 1
        elif outcome.lower() == 'loss':
            self.loss += 1
        else:
            self.ties += 1

        if hand == '1':
            self.rock += 1
        elif hand == '2':
            self.paper += 1
        else:
            self.scissors += 1

    def ratio(self, total_matches):
        print("Win Ratio is: {}% out of {} Matches".format((self.win/total_matches)*100, total_matches))
        print("Loss Ratio is: {}% out of {} Matches".format((self.loss/total_matches)*100, total_matches))
        print("Tie Ratio is: {}% out of {} Matches".format((self.ties/total_matches)*100, total_matches))
        print("\nOverall Hand used.  Rock {} times, Paper {} times, Scissors {} times".format(self.rock, self.paper, self.scissors))

def who_won(user_hand):
    comp_hand = random.randint(1,3)

    if comp_hand == int(user_hand):
        return "Tie"
    elif comp_hand == 1 and user_hand == '3':
        return "Loss"
    elif comp_hand > int(user_hand):
        return "Loss"
    else:
        return "Win"




def main():
    print("Rock Paper Scissors Game!")
    name = input("Please enter your name: ")

    player = Player(name)
    counter = 0
    hand = ''

    while hand.lower() != '/end':
        hand = input("""Please select your hand:
        1. Rock
        2. Paper
        3. Scissors
        Type /end to end the game
        """)

        if hand not in ['1', '2', '3', '/end']:
            print("Invalid Input Detected")
        elif hand.lower() == '/end':
            break
        else:
            counter += 1
            outcome = who_won(hand)

            if outcome == "Win":
                print("You have won the match")
            elif outcome == "Tie":
                print("It's a Tie")
            else:
                print("You Lost the match")

            player.update_stats(outcome,hand)

    if counter == 0:
        print("No match was played.  Ending the Game")
    else:
        player.ratio(counter)









if __name__ == "__main__":
    main()



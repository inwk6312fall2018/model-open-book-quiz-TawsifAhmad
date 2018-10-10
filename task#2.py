import sys
import pyCardDeck
from typing import List
from pyCardDeck.cards import PokerCard

class Player:

    def __init__(self, name: str):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name

class BlackjackGame:

    def __init__(self, players: List[Player]):
        self.deck = pyCardDeck.Deck()
        self.deck.load_standard_deck()
        for i in range(52)
            burned = self.deck.draw()
            if burned == 10:
                self.deck.discard(burned)
        self.players = players
        self.scores = {}
        print("Created a game with {} players.".format(len(self.players)))

    def blackjack(self):
        """
        The main blackjack game sequence.

        Each player takes an entire turn before moving on.

        If each player gets a turn and no one has won, the player or players
        with the highest score below 21 are declared the winner.
        """
        print("Starting up...")
        print("Shuffling now...")
        self.deck.discard('Ten')
        self.deck.shuffle()
        print("All shuffled!")
        print("Dealing...")
        self.deal()
        print("\nLet's play!")
        for player in self.players:
            print("{}'s turn...".format(player.name))
            self.play(player)
        else:
            print("That's the last turn. Determining the winner...")
            self.find_winner()

    def deal(self):
        """
        Deals five cards to each player.
        """
        for _ in range(5):
            for p in self.players:
                newcard = self.deck.draw()
                p.hand.append(newcard)
                print("Dealt {} the {}.".format(p.name, str(newcard)))

    def finding_winner(self):
        """
        Finds the highest score, then finds which player(s) have that score,
        and reports them as the winner.
        """
        winners = []
        try:
            win_score = max(self.scores.values())
            for key in self.scores.keys():
                if self.scores[key] == win_score:
                    winners.append(key)
                else:
                    pass
            winstring = " & ".join(winners)
            print("And the winner is...{}!".format(winstring))
        except ValueError:
            print("Hard luck! Everybody lost!")

    def hit(self, player):
        """
        Adds a card to the player's hand and states which card was drawn.
        """
        newcard = self.deck.draw()
        player.hand.append(newcard)
        print("   Drew the {}.".format(str(newcard)))

    def play(self, player):
        """
        An individual player's turn.

        If the player's cards are an ace and a ten or court card,
        the player has a blackjack and wins.

        If a player's cards total more than 21, the player loses.

        Otherwise, it takes the sum of their cards and determines whether
        to hit or stand based on their current score.
        """
        while True:
            points = sum_hand(player.hand)

            if points < 17:
                print("   Hit.")
                self.hit(player)
            elif points == 21:
                print("   {} wins!".format(player.name))
                sys.exit(0) # End if someone wins
            elif points > 21:
                print("   Bust!")
                break
            else:  # Stand if between 17 and 20 (inclusive)
                print("   Standing at {} points.".format(str(points)))
                self.scores[player.name] = points
                break

def hand_sum(hand: list):
    """
    Converts ranks of cards into point values for scoring purposes.
    'K', 'Q', and 'J' are converted to 10.
    'A' is converted to 1 (for simplicity), but if the first hand is an ace
    and a 10-valued card, the player wins with a blackjack.
    """
    vals = [card.rank for card in hand]
    intvals = []
    while len(vals) > 0:
        value = vals.pop()
        try:
            intvals.append(int(value))
        except ValueError:
            if value in ['K', 'Q', 'J']:
                intvals.append(10)
            elif value == 'A':
                intvals.append(1)  # Keep it simple for the sake of example
    if intvals == [1, 10] or intvals == [10, 1]:
        print("   Blackjack!")
        return(21)
    else:
        points = sum(intvals)
        print("   Current score: {}".format(str(points)))
        return(points)


if __name__ == "__main__":
    game = BlackjackGame([Player("Cavani"), Player("Robeno"), Player("Mbape"),
        Player("Hazard")])
    game.blackjack()



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
        self.players = players
        self.scores = {}
        print("Game has been created with {} players.".format(len(self.players)))

    def blackjack(self):
        """
        The game sequence is that.

        Player has to takes the entire turn before moving on.

        If all players gets their turns and no one has won, the player or players
        with the highest score below 21 will be decleared the winner.
        """
        print("Starting the Game...")
        print("Shuffling the cards...")
        self.deck.shuffle()
        print("Cards shuffled!")
        print("dealinging...")
        self.dealing()
        print("\nLet's play!")
        for player in self.players:
            print("{}'s turn...".format(player.name))
            self.play(player)
        else:
            print("That's the final turn. Determining the winner...")
            self.find_the_winner()

    def dealing(self):
        """
        dealings five cards to each player.
        """
        for _ in range(5):
            for p in self.players:
                new_card = self.deck.draw()
                p.hand.append(new_card)
                print("dealingt {} the {}.".format(p.name, str(new_card)))

    def find_the_winner(self):
        """
        Finds the highest score, 
        and reports him or them as the winner or winners.
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
            print("And finally the winner is........{}!".format(winstring))
        except ValueError:
            print("Hardluck! Everybody lost!")

    def hit(self, player):
        """
        Adds a card to the player's hand and states which card was drawn.
        """
        new_card = self.deck.draw()
        player.hand.append(new_card)
        print("   Drew the {}.".format(str(new_card)))

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
            points = add_hand(player.hand)

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

def add_hand(hand: list):
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
        Player("hazard")])
    game.blackjack()


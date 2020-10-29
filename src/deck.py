from card import Suit, Rank, Card
import random


class Deck:

    def __init__(self, num_players: int):
        self.deck = list()

        for player in range(num_players):
            for suit in Suit:
                for rank in Rank:
                    self.deck.append(Card(rank=rank, suit=suit))
                self.deck.append(Card(is_joker=True))

    def shuffle(self):
        random.shuffle(self.deck)

    def take_top_card(self):
        return self.deck.pop()

    def take_random_card(self):
        return self.deck.pop(random.randint(1, len(self.deck)))
from enum import Enum


class Suit(Enum):
    SPADES = "spades"
    DIAMONDS = "diamonds"
    HEARTS = "hearts"
    CLUBS = "clubs"


class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card:

    def __init__(self, suit: Suit = Suit.SPADES, rank: Rank = Rank.ACE, is_joker: bool = False):
        self.rank = rank
        self.suit = suit
        self.is_joker = is_joker

    def __str__(self):
        if self.is_joker:
            return "Joker"
        return str(self.rank) + " of " + str(self.suit)

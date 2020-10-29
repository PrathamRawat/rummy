from enum import Enum


class Suit(Enum):
    SPADES = "spades"
    DIAMONDS = "diamonds"
    HEARTS = "hearts"
    CLUBS = "clubs"
    JOKER = "joker"


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

    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if self.suit == Suit.JOKER:
            return "Joker"
        return str(self.rank) + " of " + str(self.suit)

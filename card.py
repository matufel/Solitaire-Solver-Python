from enum import Enum


class Suit(Enum):
    """Enum representing card suits
    """
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4 

class Value(Enum):
    """Enum representing card values
    """
    Ace = 1
    ONE = 1
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
    """
    Models a Card.
    Constructor takes in Suit and Value.
    """
    def __init__(self, suit : Suit, value : Value):
        """Constructor

        Args:
            suit (Suit): Suit of the card
            value (Value): value of a card
        """
        self.suit =  suit
        self.value = value
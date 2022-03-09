import random


class Card:
    def __init__(self, value: int = None, suit: int = None, deck: classmethod = None) -> None:
        self.deck = deck
        if value is not None and suit is not None:
            self.__validate_params(value, suit)
            self.value = value
            self.suit = suit
        else:
            self.value, self.suit = self.__generate_card()
        self.suit_name = self.__convert_suit()
        self.rank = self.__convert_rank()
        self.name = f"{self.rank} of {self.suit_name}"
        self.img = self.__generate_img()

    def __str__(self) -> str:
        return self.name

    def __validate_params(self, value, suit):
        if type(value) == int and type(suit) == int:
            return 1 <= value <= 13 and 1 <= suit <= 3
        raise InvalidCardParameters

    def __generate_card(self):
        value = random.randint(1, 13)
        suit = random.randint(0, 3)
        return value, suit

    def __convert_rank(self) -> str:
        conversion_dict = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        return conversion_dict.get(self.value, self.value)

    def __convert_suit(self) -> str:
        suit_conversion = {0: "Spades", 1: "Clubs", 2: "Hearts", 3: "Diamonds"}
        return suit_conversion[self.suit]

    def __generate_img(self) -> str:
        """
        Creates an ASCII image of the playing card object.
        """
        suit_emojis = ["♠", "♣", "♥", "♦"]
        suit = suit_emojis[self.suit]
        rank = str(self.rank)[0]
        return f"*- - -*\n|{suit}    |\n|  {rank}  |\n|   {suit} |\n*- - -*"

    def __gt__(self, other: object) -> bool:
        return self.value > other.value

    def __lt__(self, other: object) -> bool:
        return self.value < other.value

    def __ge__(self, other: object) -> bool:
        return self.value >= other.value

    def __le__(self, other: object) -> bool:
        return self.value <= other.value

    def __eq__(self, other: object) -> bool:
        return self.value == other.value

    def __ne__(self, other: object) -> bool:
        return self.value != other.value

    def __repr__(self):
        return self.name


class InvalidCardParameters(Exception):
    pass

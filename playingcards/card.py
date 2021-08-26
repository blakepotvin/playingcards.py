import random

class Card:
    def __init__(self, value:int=None, suit:int=None, deck:classmethod=None, seed=None) -> None:
        if seed is not None:
            random.seed(seed)
            
        self.deck = deck
        if self.deck is None:
            if value is None and suit is None:
                value, suit = self.__generate_card()
            elif not self.__validate_params(value, suit):
                raise InvalidCardParameters

        self.suit = suit
        self.suit_name = self.__convert_suit()
        self.value = value
        self.rank = self.__convert_rank()
        self.name = f"{self.rank} of {self.suit_name}"
        self.img = self.__generate_img()
        
    
    def __str__(self) -> str:
        return self.name
    
    def __validate_params(self, value, suit) -> bool:
        return 1 <= value <= 13 and 1<= suit <= 3

    def __generate_card(self):
        value = random.randint(1,13)
        suit = random.randint(0,3)
        return value, suit
    
    def __convert_rank(self) -> str:
        conversion_dict = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        if self.value in conversion_dict:
            return conversion_dict[self.value]
        else:
            return self.value

    def __convert_suit(self) -> str:
        suit_conversion = {0: "Spades", 1: "Clubs", 2: "Hearts", 3: "Diamonds"}
        return suit_conversion[self.suit]

    def __generate_img(self) -> str:
        """
        Creates an ASCII image of the playing card object.
        """
        suit_emojis = {0: "♠", 1: "♣", 2: "♥", 3: "♦"}
        suit = suit_emojis[self.suit]
        rank = str(self.rank)[0]
        return f"*- - -*\n|{suit}    |\n|  {rank}  |\n|   {suit} |\n*- - -*"

    def __gt__(self, other:object) -> bool:
        return self.value > other.value
    
    def __lt__(self, other:object) -> bool:
        return self.value < other.value
    
    def __ge__(self, other:object) -> bool:
        return self.value >= other.value
    
    def __le__(self, other:object) -> bool:
        return self.value <= other.value
    
    def __eq__(self, other: object) -> bool:
        return self.value == other.value
    
    def __ne__(self, other: object) -> bool:
        return self.value != other.value
    
class InvalidCardParameters(Exception):
    pass
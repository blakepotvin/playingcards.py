import random

class Card:
    def __init__(self, value:int=None, suit:str=None, deck:classmethod=None) -> None:
        self.__valid_suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.deck = deck

        if self.deck is None:
            if value is None and suit is None:
                value, suit = self.__generate_card()
            elif not self.__validate_params(value, suit):
                raise InvalidCardParameters

        self.suit = suit
        self.value = value
        self.rank = self.__convert_rank()
        self.name = f"{self.rank} of {self.suit}"
        self.img = self.__generate_img()
    
    def __str__(self) -> str:
        return self.name
    
    def __validate_params(self, value, suit) -> bool:
        return 1 <= value <= 13 and suit in self.__valid_suits

    def __generate_card(self):
        value = random.randint(1,13)
        suit = random.choice(self.__valid_suits)
        return value, suit
    
    def __convert_rank(self) -> str:
        conversion_dict = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        if self.value in conversion_dict:
            return conversion_dict[self.value]
        else:
            return self.value

    def __generate_img(self) -> str:
        """
        Creates an ASCII image of the playing card object.
        """
        suit_emojis = {'Hearts': "♥", 'Diamonds': "♦", 'Clubs': "♣", 'Spades': "♠"}
        suit = suit_emojis[self.suit]
        rank = str(self.rank)[0]
        return f"*- - -*\n|{suit}    |\n|  {rank}  |\n|   {suit} |\n*- - -*"

class InvalidCardParameters(Exception):
    pass
import random
from . import card
class Deck():
    
    def __init__(self, seed=None) -> None:
        self.drawn_cards = {0: [], 1: [], 2: [], 3: []}
        self.cards = []
        self.drawn = 0
        self.remaining = 52
        if seed is not None:
            random.seed(seed)

    def draw_card(self, value:int=None, suit:int=None) -> card.Card:
        if self.remaining == 0:
            raise MaxCardsDrawn
        if value is None and suit is None:
            value, suit = self.__generate_card_values()
        elif not 1 <= value <= 13 and not 1 <= suit <= 3:
            raise card.InvalidCardParameters
        elif value in self.drawn_cards[suit]:
            raise card.InvalidCardParameters
        self.drawn += 1
        self.remaining -= 1
        # draw card and append
        drawn_card = card.Card(value=value, suit=suit, deck=self)
        self.cards.append(drawn_card)
        self.drawn_cards[drawn_card.suit].append(drawn_card.value)
        return drawn_card

    def shuffle(self) -> None:
        self.cards = []
        self.drawn_cards = {0: [], 1: [], 2: [], 3: []}

    def __generate_card_values(self):
        valid = False
        while not valid:
            suit = random.randint(0,3)
            value = random.randint(1,13)
            if value not in self.drawn_cards[suit]:
                valid = True
        return value, suit

class MaxCardsDrawn(Exception):
    pass
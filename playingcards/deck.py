import random
from . import card


class Deck():

    def __init__(self, deck: list = None) -> None:
        if deck is not None and self.__validate_initial_deck(deck):
            self.cards = deck
        else:
            self.cards = self.__generate_deck()
        self.drawn = 0
        self.remaining = 52

    def __generate_deck(self) -> list:
        deck = []
        for suit in range(4):
            deck.extend(card.Card(value=value, suit=suit, deck=self)
                        for value in range(1, 14))
        return deck

    def __validate_initial_deck(self, deck) -> bool:
        return all(isinstance(card, card.Card) for card in deck)

    def draw_card(self) -> card.Card:
        if len(self.cards):
            drawn_card = self.cards.pop()
        else:
            raise MaxCardsDrawn
        self.drawn += 1
        self.remaining -= 1
        return drawn_card

    def shuffle(self) -> None:
        random.shuffle(self.cards)


class MaxCardsDrawn(Exception):
    pass

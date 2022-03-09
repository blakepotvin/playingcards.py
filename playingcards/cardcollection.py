from random import randint, shuffle
from . import card


class MaxCardsReached(Exception):
    pass


class CardCollection:
    def __init__(self, cards=None, maximum: int = None, ordered: bool = False) -> None:
        self.cards = cards
        self.maximum = maximum
        self.ordered = ordered

    def add_cards(self, cards, position, random: bool = False):
        if self.maximum is not None and len(self.cards) + len(cards) > self.__maximum:
            raise MaxCardsReached
        if not random:
            self.cards.insert(position, *cards)
        else:
            random_position = randint(0, len(self.cards))
            self.cards.insert(random_position, *cards)
        self.ordered = False

    def remove_card(self, position):
        self.cards.pop(position)

    def order_cards(self):
        if not self.ordered:
            self.cards.sort()
            self.ordered = True

    def shuffle(self) -> None:
        shuffle(self.cards)
        self.ordered = False

    def __str__(self) -> str:
        return ", ".join(str(card) for card in self.cards)

    def __iter__(self) -> iter:
        return iter(self.cards)

    def __add__(self, other):
        if isinstance(other, CardCollection):
            return self.cards + other.cards
        elif isinstance(other, card.Card):
            return self.cards.append(other)
        else:
            raise TypeError(
                f"Cannot add {type(self)} to {type(other)}. Can only add CardCollection or Card to CardCollection")

    def __len__(self):
        return len(self.cards)

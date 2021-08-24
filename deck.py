import random
import card

class Deck():
    
    def __init__(self) -> None:
        self.drawn_cards = {'Hearts': [], 'Diamonds': [], 'Clubs': [], 'Spades': []}
        self.cards = []
        self.drawn = 0
        self.remaining = 52

    def draw_card(self) -> card.Card:
        # TODO add a way to keep track of drawn cards
        # update card counts
        if self.remaining == 0:
            raise MaxCardsDrawn

        self.drawn += 1
        self.remaining -= 1
        # draw card and append
        value, suit = self.__generate_card_values()
        drawn_card = card.Card(value=value, suit=suit, deck=self)
        self.cards.append(drawn_card)
        self.drawn_cards[drawn_card.suit].append(drawn_card.value)
        return drawn_card

    def __generate_card_values(self):
        valid = False
        while not valid:
            valid_suits = list(self.drawn_cards.keys())
            suit = random.choice(valid_suits)
            value = random.randint(1,13)
            if value not in self.drawn_cards[suit]:
                valid = True
        return value, suit

class MaxCardsDrawn(Exception):
    pass
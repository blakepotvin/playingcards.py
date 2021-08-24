import random
import card

class Deck():
    
    def __init__(self) -> None:
        self.drawn_cards = {'Hearts': [], 'Diamonds': [], 'Clubs': [], 'Spades': []}
        self.drawn = 0
        self.remaining = 52

    def draw_card(self) -> card.Card:
        # TODO add a way to keep track of drawn cards
        # update card counts
        self.drawn_count += 1
        self.remaining -= 1
        # draw card and append
        drawn_card = card.Card()
        self.drawn_cards[drawn_card.suit].append(drawn_card.value)
        return drawn_card
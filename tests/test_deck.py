from playingcards import Deck
from random import seed

seed("xyz")

deck = Deck()
card_1 = deck.draw_card()
card_2 = deck.draw_card(value=11, suit=3)

"""
Test Deck Attributes
"""


def test_drawn_cards():
    assert deck.drawn_cards[2] == [6]
    assert deck.drawn_cards[3] == [11]


def test_cards():
    assert card_1 is deck.cards[0]
    assert card_2 is deck.cards[1]


def test_drawn():
    assert deck.drawn == 2


def test_remaining():
    assert deck.remaining == 50


def test_shuffle():
    deck.shuffle()
    assert deck.cards == [] and deck.drawn_cards[2] == [] and deck.drawn_cards[3] == []


"""
Test Card Drawn from Deck
"""


def test_value():
    assert card_1.value == 6
    assert card_2.value == 11


def test_rank():
    assert card_1.rank == 6
    assert card_2.rank == 'Jack'


def test_suit():
    assert card_1.suit == 2
    assert card_2.suit == 3


def test_suit_name():
    assert card_1.suit_name == 'Hearts'
    assert card_2.suit_name == 'Diamonds'


def test_name():
    assert card_1.name == '6 of Hearts'
    assert card_2.name == 'Jack of Diamonds'


def test_img():
    assert card_1.img == '*- - -*\n|♥    |\n|  6  |\n|   ♥ |\n*- - -*'
    assert card_2.img == '*- - -*\n|♦    |\n|  J  |\n|   ♦ |\n*- - -*'


def test_deck():
    assert card_1.deck is deck
    assert card_2.deck is deck

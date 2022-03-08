from playingcards import Deck
from random import seed

seed("xyz")

deck = Deck()
card_1 = deck.draw_card()

"""
Test Deck Attributes
"""


def test_drawn():
    assert deck.drawn == 1


def test_remaining():
    assert deck.remaining == 51


def test_shuffle():
    test_card = deck.cards[1]
    deck.shuffle()
    assert test_card != deck.cards[1]


"""
Test Card Drawn from Deck
"""


def test_value():
    assert card_1.value == 13


def test_rank():
    assert card_1.rank == 'King'


def test_suit():
    assert card_1.suit == 3


def test_suit_name():
    assert card_1.suit_name == 'Diamonds'


def test_name():
    assert card_1.name == 'King of Diamonds'


def test_img():
    assert card_1.img == '*- - -*\n|♦    |\n|  K  |\n|   ♦ |\n*- - -*'


def test_deck():
    assert card_1.deck is deck


def test_order_cards():
    deck.order_cards()
    assert deck.cards[0].value == 1
    assert deck.cards[-1].value == 13

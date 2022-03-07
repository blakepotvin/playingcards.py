from playingcards import Card
from random import seed

seed("xyz")

card = Card()

def test_value():
    assert card.value == 5

def test_rank():
    assert card.rank == 5

def test_suit():
    assert card.suit == 2

def test_suit_name():
    assert card.suit_name == 'Hearts'

def test_name():
    assert card.name == '5 of Hearts'

def test_img():
    assert card.img == '*- - -*\n|♥    |\n|  5  |\n|   ♥ |\n*- - -*'

def test_deck():
    assert card.deck is None
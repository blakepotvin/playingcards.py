from playingcards import Deck

deck = Deck(seed="xyz")
card = deck.draw_card()

"""
Test Deck Attributes
"""
def test_drawn_cards():
    assert deck.drawn_cards[2] == [6]

def test_cards():
    assert card is deck.cards[0]

def test_drawn():
    assert deck.drawn == 1

def test_remaining():
    assert deck.remaining == 51

def test_shuffle():
    deck.shuffle()
    assert deck.cards == [] and deck.drawn_cards[2] == []




"""
Test Card Drawn from Deck
"""
def test_value():
    assert card.value == 6

def test_rank():
    assert card.rank == 6

def test_suit():
    assert card.suit == 2

def test_suit_name():
    assert card.suit_name == 'Hearts'

def test_name():
    assert card.name == '6 of Hearts'

def test_img():
    assert card.img == '*- - -*\n|♥    |\n|  6  |\n|   ♥ |\n*- - -*'

def test_deck():
    assert card.deck is deck
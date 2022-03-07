from playingcards import Deck

deck = Deck(seed="xyz")
card_1 = deck.draw_card()
card_2 = deck.draw_card(value=6, suit=2)

"""
Test Deck Attributes
"""


def test_drawn_cards():
    assert deck.drawn_cards[2] == [6, 6]


def test_cards():
    assert card_1 is deck.cards[0]
    assert card_2 is deck.cards[1]


def test_drawn():
    assert deck.drawn == 2


def test_remaining():
    assert deck.remaining == 50


def test_shuffle():
    deck.shuffle()
    assert deck.cards == [] and deck.drawn_cards[2] == []


"""
Test Card Drawn from Deck
"""


def test_value():
    assert card_1.value == 6
    assert card_2.value == 6


def test_rank():
    assert card_1.rank == 6
    assert card_2.rank == 6


def test_suit():
    assert card_1.suit == 2
    assert card_2.suit == 2


def test_suit_name():
    assert card_1.suit_name == 'Hearts'
    assert card_2.suit_name == 'Hearts'


def test_name():
    assert card_1.name == '6 of Hearts'
    assert card_2.name == '6 of Hearts'


def test_img():
    assert card_1.img == '*- - -*\n|♥    |\n|  6  |\n|   ♥ |\n*- - -*'
    assert card_2.img == '*- - -*\n|♥    |\n|  6  |\n|   ♥ |\n*- - -*'


def test_deck():
    assert card_1.deck is deck
    assert card_2.deck is deck

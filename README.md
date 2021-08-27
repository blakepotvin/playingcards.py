# playingcards&#46;py

[![MIT License](https://img.shields.io/github/license/Prodxgy/playingcards.py?label=license)](https://github.com/Prodxgy/playingcards.py/blob/master/LICENSE)
[![PyPi Python Versions](https://img.shields.io/pypi/pyversions/Django)]()


An Advanced Python Playing Card Module that makes creating playing card games simple and easy!

## Features
* Easy to Understand Class Objects
* ASCII Card Images
* Card Comparisons
* Duplicate Prevention within Decks
* *`Optional`* Seed Input for Custom Generation Sequences

## Installation
>*Requires Python 3.6 and above*

You can install the module from [PyPI]() or by using pip.

```sh
# Linux/MacOS
pip3 install playingcards.py

# Windows
pip install playingcards.py

```

## How To Use
This module introduces two class objects: `Deck` and `Card`.

The difference between the two classes is that the `Deck` class keeps track of all of the drawn cards to prevent duplicates from being generated.

### Drawing Cards
The `Deck` class can be called with the `draw_card()` function to draw a card object. 

Generating a card by only using the `Card` class happpens when you instantiate it.

> *Both Classes Have A Seed Argument To Modify The Random Number Generator*
```py
from playingcards import Deck, Card

# Card Generated Using Deck
player_deck = Deck()
player_card = player_deck.draw_card()

# Card Generated From Instantiation
player_card_2 = Card()

# Card Generated With A Seed
player_deck_2 = Deck(seed="abc")
player_card_3 = Card(seed="xyz")
```

### Class Attributes

* **Deck** Attributes
  * drawn_cards `dict` - Returns a dict of the values that were drawn from each corresponding suit.
  * cards `list` - Returns a list containing the class objects of each drawn card.
  * drawn `int` - Returns an integer of the amount of cards that have been drawn.
  * remaining `int` - Returns an integer amount of the remaining cards that can be drawn.

* **Card** Attributes
  * deck `Deck` - Returns a Deck object if the card was drawn from a deck. *Default: None*.
  * suit `int` - Returns an integer that corresponds with the card's suit.
  * suit_name `str` - Returns a string containing the converted suit name.
  * value `int` - Returns an integer of the card's face value.
  * rank `str|int` - Returns a string if the value can be converted into a word value (Ex. 11 -> Jack). Defaults to returning an integer if its not applicable (Ex. 2 -> 2).
  * name `str` - Returns a string containing the full name of the card. This prints out the rank and the suit of the card. (Ex. Ace of Spades, 3 of Hearts)
  * img `str` - Returns a string that contains an ASCII image of the card with the corresponding suit symbol.


### Class Arguments
A card object can be instantiated with preconceived values instead of using a random generator.

* Suits are ordered numerically from 0-3.

    * 0: **Spades**

    * 1: **Clubs**
  
    * 2: **Hearts**
  
    * 3: **Diamonds**

* Values are ordered numerically from 1-13.

  * 1: **Ace**

  * 2-10: **Face Value**

  * 11: **Jack**

  * 12: **Queen**
  
  * 13: **King**


```py
player_card = Card(value=11, suit=1)


print(player_card)
>> Jack of Clubs

print(player_card.value)
>> 11

print(player_card.suit_name)
>> Clubs

print(player_card.rank)
>> Jack

print(player_card.img)
>> *- - -*
   | ♣   |
   |  J  |
   |   ♣ |
   *- - -*
```
> These arguments can also be used in the `draw_card()` function apart of the `Deck` class.

### Card Comparisons
The card objects feature comparison features which allows their **values** to be compared. 

> When checking for equivalency, it only checks the value of the card, *not the suits*.

```py
card_1 = Card(value=8, suit=0)
card_2 = Card(value=12, suit=2)
card_3 = Card(value=8, suit=3)

print(card_1 < card_2)
>> True

print(card_3 == card_1) # Returns True even if the suit is different
>> True

```
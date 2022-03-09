# playingcards&#46;py

[![MIT License](https://img.shields.io/pypi/l/playingcards.py?style=for-the-badge)](https://github.com/Prodxgy/playingcards.py/blob/master/LICENSE)
[![PyPi Python Versions](https://img.shields.io/pypi/pyversions/playingcards.py?style=for-the-badge)]()


An Advanced Python Playing Card Module that makes creating playing card games simple and easy!

## Features
* Easy to Understand Class Objects
* ASCII Card Images
* Card Comparisons
* Duplicate Prevention within Decks

## Installation
>*Requires Python 3.6 and above*

You can install the module from [PyPI](https://pypi.org/project/playingcards.py/) or by using pip.

```sh
# Linux/MacOS
pip3 install playingcards.py

# Windows
pip install playingcards.py

```

## How To Use
This module introduces three class objects: `CardCollection`, `Deck` and `Card`.

## Differences Between Classes
<!-- The difference between the two classes is that the `Deck` class keeps track of all of the drawn cards to prevent duplicates from being generated. -->

`Card` is a class that contains properties that are found on your everyday playing card, i.e. rank and suit.

`CardCollection` is a class used to construct various types of card collections. For example, you could use it to construct a class for a "Hand" of cards. 

`Deck` is class constructed from the CardCollection class. It contains 52 upon its initialization and has member functions related to drawing cards and attributes referring to the numeric amounts in the deck.

### Drawing Cards
The `Deck` class can be called with the `draw_card()` function to draw a card object. Additionally, `draw_n()` can be used to draw multiple cards at once and be returned as a CardCollection object. 

Generating a card by only using the `Card` class happpens when you instantiate it.

```py
from playingcards import Deck, Card

# Card Generated Using Deck
player_deck = Deck()
player_card = player_deck.draw_card()
player_hand = player_deck.draw_n(5)

# Card Generated From Instantiation
player_card_2 = Card()

```

## Class Methods & Attributes

* **Card** 
  * **Attributes**
    * deck `Deck` - Returns a Deck object if the card was drawn from a deck. *Default: None*.
    * suit `int` - Returns an integer that corresponds with the card's suit.
    * suit_name `str` - Returns a string containing the converted suit name.
    * value `int` - Returns an integer of the card's face value.
    * rank `Union[str,int]` - Returns a string if the value can be converted into a word value (Ex. 11 -> Jack). Defaults to returning an integer if its not applicable (Ex. 2 -> 2).
    * name `str` - Returns a string containing the full name of the card. This prints out the rank and the suit of the card. (Ex. Ace of Spades, 3 of Hearts)
    * img `str` - Returns a string that contains an ASCII image of the card with the corresponding suit symbol.
* **CardCollection**
  * **Attributes**
      * cards `List[Card]` - Returns a list of Card objects.
      * maximum `int` - Returns the maximum number of cards that can be held in the collection.
      * ordered `bool` - Returns a boolean value that indicates whether the collection is ordered or not.
  * **Methods**
      * add_cards(`cards`, `position`, `random` ) - Adds cards to the collection.
        * **Parameters**
          * **cards** (`List[Card]`) - A list of Card objects to be added to the collection.
          * **position** (`int`) - The position in the collection to add the cards.
          * **random** (`bool`) - A boolean value that indicates whether the cards should be added in a random position.
        * **Returns**
          * `None`
      * remove_card(`cards`, `position`) - Removes a card from the collection.
        * **Parameters**
          * **cards** (`List[Card]`) - A list of Card objects to be removed from the collection.
          * **position** (`int`) - The position in the collection to remove the card.
        * **Returns**
          * `None`
      * order_cards() - Orders the cards in the collection.
        * **Parameters**
          * **None**
        * **Returns**
          * `None`
      * shuffle() - Shuffles the cards in the collection.
        * **Parameters**
          * **None**
        * **Returns**
          * `None`
* **Deck** (inherits `CardCollection` methods & attributes)
  * **Attributes**
    * cards `list` - Returns a list containing the class objects of each drawn card.
    * drawn `int` - Returns an integer of the amount of cards that have been drawn.
    * remaining `int` - Returns an integer amount of the remaining cards that can be drawn.
* **Methods**
  * draw_card() - Draws a card from the top of the deck.
    * **Parameters**
      * **None**
    * **Returns**
      * `Card`
  * draw_n(n) - Draws a number of cards from the top of the deck.
    * **Parameters**
      * **n** (`int`) - The number of cards to draw.
    * **Returns**
      * `CardCollection`
  



## Object Initialization Arguments
A card object can be instantiated with preconceived values instead of using a random number generator.

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

## Card Comparisons
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

## Contributing
See [CONTRIBUTING.md](https://github.com/Prodxgy/playingcards.py/blob/master/CONTRIBUTING.md)

## Acknoledgements
The `CardCollection` object was inspired by [@mitchr1598](https://github.com/mitchr1598) whose playingcards project utilized.

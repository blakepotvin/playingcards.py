import random
import deck

class Card():

    global suits    
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

    def __init__(self, value:int=-1, suit:str=None) -> None:
        card_conversion = {
        1: "Ace",
        11: "Jack",
        12: "Queen",
        13: "King"
        }


        self.value = self.generate_value() if not 1 <= value <= 13 else value
        if suit not in suits or suit is None:
            self.suit = self.generate_suit()
        else:
            self.suit = suit
        self.converted_value = (
            card_conversion[self.value]
            if self.value in card_conversion
            else self.value
        )

        self.name = f"{self.converted_value} of {self.suit}"

    def __str__(self) -> str:
        return self.name    
    def generate_value(self) -> int:
        return random.randint(1,12)

    def generate_suit(self) -> str:
        return random.choice(suits)


if __name__ == "__main__":
    newDeck = deck.Deck()
    newCard = newDeck.draw_card()
    newCard2 = newDeck.draw_card()
    newCard3 = newDeck.draw_card()
    print(newCard, newCard2, newCard3)
    print(newDeck.drawn_cards)

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suites = ("Hearts", "Spades", "Clubs", "Diamonds")
        cards = []
        for suite in suites:
            for num in range(2, 15):
                cards.append(Card(suite, num))
        self.cards = cards

class Card:
    def __init__(self, suite, number):
        self.suite = suite
        self.number = number

    def __str__(self):
        return f"The {self.number} of {self.suite}"

mydeck = Deck()
for card in mydeck.cards: print(card)

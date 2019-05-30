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
        self.determine_value()

    def __str__(self):
        if self.isNumber():
            return f"The {self.number} of {self.suite}"
        elif self.number == 11:
            return f"The Jack of {self.suite}"
        elif self.number == 12:
            return f"The Queen of {self.suite}"
        elif self.number == 13:
            return f"The King of {self.suite}"
        elif self.isAce():
            return f"The Ace of {self.suite}"

    def determine_value(self):
        if(self.isNumber()):
            self.value = self.number
        elif(self.isFace()):
            self.value = 10
        elif(self.isAce()):
            self.value = 1

    def isNumber(self):
        return self.number <= 10

    def isFace(self):
        return self.number > 10 and self.number < 14

    def isAce(self):
        return self.number == 14

    def draw(self):
        return self.cards.pop()

class Hand:
    def __init__(self, card):
        cards = []
        cards.append(card)
        self.cards = []

class Player:
    def __init__(self, hand):
        self.hand = hand

mydeck = Deck()
for card in mydeck.cards: print(card.value)

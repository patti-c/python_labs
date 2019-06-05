import random

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

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

class Card:
    def __init__(self, suite, number):
        self.suite = suite
        self.number = number
        self.determine_value()

    def __str__(self):
        if self.isNumber():
            return f"the {self.number} of {self.suite}"
        elif self.number == 11:
            return f"the Jack of {self.suite}"
        elif self.number == 12:
            return f"the Queen of {self.suite}"
        elif self.number == 13:
            return f"the King of {self.suite}"
        elif self.isAce():
            return f"the Ace of {self.suite}"

    def determine_value(self):
        if(self.isNumber()):
            self.min_value = self.number
            self.max_value = self.number
        elif(self.isFace()):
            self.min_value = 10
            self.max_value = 10
        elif(self.isAce()):
            self.min_value = 1
            self.max_value = 10

    def isNumber(self):
        return self.number <= 10

    def isFace(self):
        return self.number > 10 and self.number < 14

    def isAce(self):
        return self.number == 14

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def min_value(self):
        return sum(card.min_value for card in self.cards)

    def is_busted(self):
        return self.min_value() > 21

    def max_value(self):
        return sum(card.max_value for card in self.cards)

class Player:
    def __init__(self):
        self.name = "You"
        self.hand = Hand()

    def hand_is_busted(self):
        return self.hand.is_busted()

    def min_hand_value(self):
        return self.hand.min_value()

    def max_hand_value(self):
        return self.hand.max_value()

    def best_hand_value(self):
        if(self.max_hand_value() <= 21):
            return self.max_hand_value()
        else:
            return self.min_hand_value()

class Dealer:
    def __init__(self):
        self.name = "The Dealer"
        self.hand = Hand()
        self.deck = Deck()
        self.shuffle()
        self.deal()

    def deal(self, user=None, count=1):
        if user == None: user = self
        for num in range(0, count):
            drawn_card = self.deck.draw()
            user.hand.add_card(drawn_card)
            print(f"{user.name} drew {str(drawn_card)}")

    def shuffle(self):
        self.deck.shuffle()

    def min_hand_value(self):
        return self.hand.min_value()

    def clear_hand(self, user=None):
        if user == None: user = self
        user.hand = Hand()

    def take_turn(self):
        while(self.min_hand_value() < 17):
            self.deal(None, 1)

    def is_busted(self):
        return self.hand.is_busted()

    def max_hand_value(self):
        return self.hand.max_value()

    def best_hand_value(self):
        if(self.max_hand_value() <= 21):
            return self.max_hand_value()
        else:
            return self.min_hand_value()

def init():
    print("Welcome to Blackjack!\n")
    dealer = Dealer()
    player = Player()
    dealer.deal(player, 2)
    player_choice = None
    while player_choice != 'surrender':
        print(f"Your hand's min value is {player.min_hand_value()} and max value is {player.max_hand_value()}")
        player_choice = input("Would you like to hit, stand or surrender?\n").lower()
        operate_on(player_choice, player, dealer)

    print("Thank you for playing!")

def operate_on(player_choice, player, dealer):
    if player_choice == 'hit':
        dealer.deal(player, 1)
        if player.hand_is_busted():
            print(f"Busted! Your hand's value was {player.min_hand_value()}. Too bad!\n")
            print("A new hand is starting.\n")
            new_hand(player, dealer)
    elif player_choice == 'stand':
        dealer.take_turn()
        if dealer.is_busted():
            print("The dealer busted! You win!")
        elif(dealer.best_hand_value() > player.best_hand_value()):
            print(f"House wins. Your hand of {player.best_hand_value()} lost to the dealer's hand of {dealer.best_hand_value()}\n")
        elif(dealer.best_hand_value() < player.best_hand_value()):
            print(f"You win! Your hand of {player.best_hand_value()} beat the dealer's hand of {dealer.best_hand_value()}\n")
        elif(dealer.best_hand_value() == player.best_hand_value()):
            print("It was a tie.\n")
        print("A new hand is starting.\n")
        new_hand(player, dealer)

def new_hand(player, dealer):
    dealer.clear_hand(dealer)
    dealer.clear_hand(player)
    dealer.deal(player, 2)
    dealer.deal(dealer, 1)

def check_if_choice_is_valid(player_choice):
    valid_options = ('hit', 'stand', 'surrender')
    if player_choice not in valid_options:
        print("That is not a valid choice.")

init()

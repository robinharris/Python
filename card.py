# Playing Cards

class Card(object):
    """A playing card"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    CARDVALUE = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10 }
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        rep = self.rank + self.suit
        return rep
        
class Hand(object):
    """A hand of playing cards"""
    
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        if self.cards:
            rep =""
            for card in self.cards:
                rep += str(card) + "   "
            
        else:
            rep ="<empty>"
        return rep
            
    def clear(self):
        self.cards = []
        
    def add(self,card):
        self.cards.append(card)
        
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
        
    def points(self):
        points=0
        if self.cards:
            for card in self.cards:
                print(self.card)
                points += Card.CARDVALUE["self.card.RANK"]
            
        
class Deck(Hand):
    """A deck of cards"""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
                
    def shuffle(self):
        import random
        random.shuffle(self.cards)
        
    def deal(self, hands,  per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card =self.cards[0]
                    self.give(top_card,  hand)
                else:
                    print("Can't continue deal.  Out of cards!")
        
    
#main
deck1 = Deck()
my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
cardsPerHand = int(input("\nEnter number of cards to deal: "))
deck1.populate()
deck1.shuffle()
print("Shuffled the deck: \n",  deck1)
deck1.deal(hands, per_hand=cardsPerHand)
print("My hand: \n", my_hand, "\nYour hand: \n",your_hand,"\nDeck: \n",deck1)
# another comment to make a change to the file
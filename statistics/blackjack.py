from random import random
class Card():
    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.length = 0
        if rank >= 10:
            self.points = 10
        elif rank == 1:
            self.points = 11
        else:
            self.points = rank

    def __repr__(self):
        d = {11: 'Jack', 12:'Queen', 13:'King', 1:'Ace'}

        if self.rank > 10 or self.rank == 1:
            return f'{d[self.rank]} of {self.suit}'
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.stack = []
        self.shuffled = False

        for rank in range(1, 14):
            for suit in ("spades", "clubs", "hearts", "diamonds"):
                self.stack.append(Card(suit, rank))

        if not self.shuffled:
            self.shuffle()

    def __eq__(self, other):
        if not self.shuffled == other.shuffled:
            return False

        for this_card, that_card in zip(self.stack, other.stack):
            if not this_card == that_card:
                return False

        return True

    def shuffle(self):
        random.seed(1)
        random.shuffle(self.stack)
        self.shuffled = True

deck1 = Deck.shuffle
print(deck1())
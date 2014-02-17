"""
Deck of cards
"""
import random


class Card():
    rank = None
    color = None
    point = None

    def __init__(self, rank, color, point):
        self.rank = rank
        self.color = color
        self.point = point


class Deck():
    cards = []

    def gen_cards(self):
        for p, i in enumerate(['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']):
            for j in ['diamond', 'heart', 'flower', 'black heart']:
                if p + 1 > 10:
                    p = 9
                card = Card(i, j, p + 1)
                self.cards.append(card)

    def draw(self):
        if not self.cards:
            return None
        else:
            return self.cards.pop(random.randrange(len(self.cards)))

    def judge(self, p1, p2):
        p1_p = p1.points()
        p2_p = p2.points()
        if p1_p > p2_p:
            return p1
        else:
            return p2


class Player():

    def __init__(self, name, deck):
        self.name = name
        self.cards = []
        self.deck = deck

    def join_deck(self, deck):
        self.deck = deck

    def points(self):
        p = 0
        for c in self.cards:
            p += c.point
        if p > 21:
            return -1
        return p

    def draw(self):
        self.cards.append(self.deck.draw())


if __name__ == '__main__':
    d = Deck()
    d.gen_cards()

    p1 = Player("John", d)
    p2 = Player("James", d)

    p1.draw()
    p2.draw()

    print d.judge(p1, p2).name

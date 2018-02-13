import random

card_data = {
    'Blue': {'n': 10,
             'bm': {3: 1,
                    5: 2,
                    7: 3,
                    8: 4}
             },
    'Red':  {'n': 8,
             'bm': {3: 1,
                    5: 2,
                    7: 3,
                    8: 4}
             }
             }


class Deck(list):
    def pop(self, n):
        values = self[:n]
        del self[:n]

        return values


class Game:

    def create_deck(self):
        for kind, data in card_data.items():
            c = Card(kind, data['n'], data['bm'])
            self.deck += data['n'] * [c]

        random.shuffle(self.deck)

    def __init__(self):
        self.turned_up = []
        self.deck = Deck()
        self.hands = [ [], [] ]
        self.fields = [ [], [] ]

        self.create_deck()

        # Initialise hands
        dealt_cards = self.deck.pop(10)
        self.hands[0] = dealt_cards[0:10:2]
        self.hands[1] = dealt_cards[1:10:2]

        # Initialise fields
        self.fields[0] = [Field(), Field(), Field()]
        self.fields[1] = [Field(), Field(), Field()]

    def play_cards(self, player_id, cards, field_id):
        self.fields[player_id][field_id].add_cards(cards)

    def play_first_card(self, player_id, field_id):
        self.play_cards(player_id, g.hands[player_id].pop(), field_id)

    def turn_up(self):
        self.turned_up = self.deck.pop(3)

    def play_turned_up(self, index, player_id, field_id):
        self.play_cards(player_id, self.turned_up.pop(index), field_id)

    def status(self):
        print('Turned up: %s' % self.turned_up)
        print('')
        print('P0:')
        print('Hand: %s' % str(self.hands[0]))
        for i in range(3):
            print('Field %d: %s' % (i, str(self.fields[0][i])))

        print('')
        print('P1')
        print('Hand: %s' % str(self.hands[1]))
        for i in range(3):
            print('Field %d: %s' % (i, str(self.fields[1][i])))
        print('-------------')

class Card:

    def __init__(self, kind, n, bm):
        self.kind = kind
        self.n = n
        self.beanometer = bm

    def __str__(self):
        return "%s bean" % (self.kind)

    def __repr__(self):
        return str(self)


class Field:

    def __init__(self):
        self.kind = None
        self.cards = []

    def add_cards(self, new_cards):
        try:
            _ = len(new_cards)
        except:
            new_cards = [new_cards]

        if self.kind is None:
            self.kind = new_cards[0].kind

        kinds_equal = [card.kind == self.kind for card in new_cards]

        if all(kinds_equal):
            self.cards += new_cards
        else:
            raise ValueError('Card kinds in a single field must match')

    def harvest_value(self):
        return 0

    def __str__(self):
        return "%d x %s" % (len(self.cards), self.kind)

    def __repr__(self):
        return str(self)

g = Game()
g.status()
g.play_first_card(0, 0)
g.play_first_card(1, 0)
g.status()
g.turn_up()
g.status()
g.play_turned_up(0, 0, 0)
g.status()

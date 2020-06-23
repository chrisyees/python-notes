import random


class Deck:

    deck = []

    def __init__(self):
        pass

    def create_deck(self):
        for i in range(1, 14):
            self.deck.extend([i] * 4)

    def take_card(self):
        random_num = random.randint(1, 13)
        self.deck.remove(random_num)
        return random_num


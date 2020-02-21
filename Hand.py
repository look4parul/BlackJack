from Card import Card


class Hand:
    def __init__(self):
        self.Card_in_hand = []
        self.value = 0
        self.aces = 0

    def add_card(self, cart, value):
        self.Card_in_hand.append(cart)
        if value == 11:
            self.aces = self.aces + 1
        self.value = self.value + value

        if self.value > 21 and self.aces >= 1:
            self.value = (
                self.value - 10
            )  # if i have 21+ and i have 1 ace , ace now == 1 and not 11
            self.aces = self.aces - 1  # -1 ace its no more ace now i have 1 and not 11

    def hand_win(self):
        if (self.value) == 21:
            return "Win"
        elif (self.value) > 21:
            return "Loose"
        else:
            return "Go on"

    def __str__(self):
        return "{" + str(self.Card_in_hand) + "," + str(self.value) + "}"
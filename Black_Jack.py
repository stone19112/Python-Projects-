"""
This is a text based card game called Black Jack that supports both single player or multiplayers. It is also an object-oriented program that mainly uses classes and functions to create the game. Each play has $1000 in the beginning. Beat the dealer and most importantly, have fun!!
class: card, deck, hands, chips.
function set 1: place_bet, take_bet, hit, hit or stand, show_some, show_all
function set 2: player_busts, player_wins, dealer_busts, dealer wins():
"""
import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, ranks, suits):
        self.suits = suits
        self.ranks = ranks
        self.values = values[ranks]
    def __str__(self):
        return self.ranks + " of " + self.suits

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal_one(self):
        return self.deck.pop(0)

class Hands:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,drawn_card):
        self.cards.append(drawn_card)
        self.value = self.value + drawn_card.values

    def adjust_ace(self):
        if self.value > 21:
            for card in self.cards:
                if card.values == 11:
                    card.values = 1
                    self.value = 0
                    for card in self.cards:
                        self.value = self.value + card.values
                        if self.value > 21 and card == 11:
                            break
                        else:
                            pass

class Chips:
    def __init__(self):
        self.total = 1000
        self.bet = 0
    def win_bet(self,total_bets):
        self.total = self.total + total_bets
    def lose_bet(self,my_bet):
        self.total = self.total - my_bet
    def bet(self,my_bet):
        self.total = self.total - my_bet
        return my_bet
def multiplayer_mode():
    players = int(input("Please enter the total number of players: "))
    return players

def take_bet(player):
    bet = 'waiting for input'
    while type(bet) is not int:
        try:
            bet = int(input(f"{player}: Choose the amount of chips you want to place on the table:"))
        except:
            print("You must enter a number!")
            continue
        else:
            return bet
def hit_or_stand (deck, players):
    decision = 'wrong'
    show_some_player(players)
    while decision not in ["s"]:
        decision = input('\nHit or stand? (Enter "h" for hit and "s" for stand) : ')
        if decision == 'h':
            print("Drawing a card...")
            time.sleep(3)
            players.add_card(deck.deal_one())
            players.adjust_ace()
            if players.value >= 21:
                break
            for card in range(len(players.cards)):
                print(players.cards[card])
            print(players.value)
            continue
        elif decision == 's':
            return True
        else:
            pass



def show_some_player(players):
    for card in range(len(players.cards)):
        print(players.cards[card])
def show_some_dealer(dealer):
    print("\n")
    print("Dealer's hand: ")
    print(dealer.cards[0])
    print("FACE DOWN CARD")

def show_chip(i):
    print(f"{names[i]}'s remaining chips: {chip[i].total}")

# Game code starts here!!!


# initialize all variables
players = 'wrong'
while players not in [1,2,3,4,5,6,7]:
    try:
        players = int(input("How many players are playing?: "))
        if players not in [1,2,3,4,5,6,7]:
            print("please limit the players less 8")
    except:
        print("You must enter a NUMBER")

player = []
chip = []
names = []
bet = []
bets = 0
chip_dealer = Chips()
for i in range(players):
    chip.append(i)
    chip[i] = Chips()

for i in range(players):
    order = i+1
    name = input(f"please enter player{order}'s name: ")
    names.append(name)
game_on = True
while game_on is not False:

    new_deck = Deck()
    new_deck.shuffle()
    # Collect all players' bet in the following for-loop
    for i in range(players):
        bet.append(i)
        bet[i] = take_bet(names[i])
        bets = bets + bet[i]
    for i in range(players):
        print("\n")
        print(f"player{i+1}")
        player.append(i)
        player[i] = Hands()
        player[i].add_card(new_deck.deal_one())
        player[i].add_card(new_deck.deal_one())
        print(f"{names[i]}'s hand: ")
        show_some_player(player[i])
    dealer = Hands()
    dealer.add_card(new_deck.deal_one())
    dealer.add_card(new_deck.deal_one())
    show_some_dealer(dealer)
    playing = True
    print("\nGame will start in 10 seconds. Get ready")
    time.sleep(5)
    while playing:
        for i in range(players):
            print("\n waiting for next player...")
            time.sleep(5)
            print(f"\n{names[i]}, it is your turn now. Please decide: ")
            stay = hit_or_stand(new_deck,player[i])
            if player[i].value >21:
                show_some_player(player[i])
                print(player[i].value)
                print(f"{names[i]} is busted")

                chip[i].lose_bet(bet[i])
                player[i].value = 0
                continue
            elif player[i].value == 21:
                show_some_player(player[i])
                print(f"{names[i]} has a Blackjack! waiting for dealer!")
            elif stay:
                continue

        while dealer.value <17:
            time.sleep(3)
            print("\n\nDealer's turn. Hidden card flipped")
            show_some_player(dealer)
            time.sleep(3)
            print("\nDealer is drawing cards...")
            time.sleep(3)
            dealer.add_card(new_deck.deal_one())
            dealer.adjust_ace()
            for card in range(len(dealer.cards)):
                print(dealer.cards[card])
            print(dealer.value)


        if dealer.value >21:
            print("\nDealer busted, all remaining players win")
            for i in range(players):
                if player[i].value != 0:
                    print(f'{names[i]} is still on the table, collecting {bet[i]} chips for this player')
                    chip[i].win_bet(bet[i])
                else:
                    pass

        elif dealer.value ==21:
            print("\nDealer has a Blackjack!!")
            for i in range(players):
                if player[i].value < 21:
                    print(f"competing dealer's hand with {names[i]}... ")
                    print(f'{names[i]} has {player[i].value}. Lost')
                    chip[i].lose_bet(bet[i])
                elif player[i].value ==21:
                    print(f"competing dealer's hand with {names[i]}... ")
                    print(f'Tie')

        else:# Dealer is not busted. compare the value to remaning players
            time.sleep(3)
            print("\n\nDealer's turn. Hidden card flipped")
            show_some_player(dealer)
            for i in range(players):
                if (dealer.value > player[i].value) and player[i].value !=0:
                    print(f"\ncompeting dealer's hand with {names[i]}... ")
                    print(f"{names[i]}: {player[i].value} vs dealer: {dealer.value}")
                    time.sleep(3)
                    print("Dealer won")
                    chip_dealer.win_bet(bet[i])
                    chip[i].lose_bet(bet[i])
                elif dealer.value < player[i].value:
                    print(f"\ncompeting dealer's hand with {names[i]}... ")
                    print(f"{names[i]}: {player[i].value} vs dealer: {dealer.value}")
                    time.sleep(3)
                    print(f"{names[i]} defeated dealder. Collecting {bet[i]} for this player")
                    chip[i].win_bet(bet[i])
                    chip_dealer.lose_bet(bet[i])
                elif dealer.value == player[i].value:
                    print(f"\ncompeting dealer's hand with {names[i]}... ")
                    print(f"{names[i]}: {player[i].value} vs dealer: {dealer.value}")
                    time.sleep(3)
                    print("Tie")
                else:
                    pass

        playing = False
        print("\n\n")
        for i in range(players):
            show_chip(i)
    for i in range(players):
        if chip[i].total == 0:
            print(f"player{names[i]} has not enough chips to continue. Game ended")
            game_on = False

    if chip_dealer.total == 0:
        game_on = False

    game_continue = "wrong"
    while game_continue not in ['y','n']:
        try:
            game_continue = input('\n\n100) Another round? type "y" or "n" ')
        except:
            print("invalid input")

    if game_continue == 'n':
        game_on = False

print("end of game")














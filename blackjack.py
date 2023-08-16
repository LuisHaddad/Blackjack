import random
import time
import sys

class Player:
    def __init__(self, name, dealer = True, money = 2000, bet = 100 ):
        self.name = name
        self.dealer = dealer
        self.hand = []
        self.money = money
        self.bet = bet

    def get_hand_value(self): 
        value = 0
        ace_count = 0
        for card in self.hand:
            value += deck_1.cards[card]
            if card == "A":
                ace_count += 1
            while value > 21 and ace_count > 0:
                value -= 10
                ace_count -= 1                   
        return value
    
    def get_card_from_deck(self):
        self.hand.append(deck_1.give_card())
        
class Stack_of_cards: 
    cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    deck = [card for card in cards.keys() for _ in range(0, 4)]
    
    def __init__(self, quantity_of_decks = 8):
        self.quantity_of_decks = quantity_of_decks
        self.deck = (self.quantity_of_decks)*self.deck
        
    def give_card (self):
        random.shuffle(self.deck)
        time.sleep(0.5)
        random.shuffle(self.deck)
        return random.choice(self.deck)
    
def dealers_play():
    while dealer.get_hand_value() < 17:
        dealer.get_card_from_deck()
        time.sleep(2)
        print("\nDealer's cards:   {}    = {}\n".format((" + ".join(dealer.hand)), dealer.get_hand_value()))
    if dealer.get_hand_value() > 21:
        time.sleep(1)
        print("Dealer busted. You win!\n")
        player_1.money += player_1.bet * 2
    else:
        if player_1.get_hand_value() > dealer.get_hand_value():
            time.sleep(1)
            print("You win!\n")
            player_1.money += player_1.bet * 2
        elif player_1.get_hand_value() == dealer.get_hand_value():
            time.sleep(1)
            print("It's a tie. How boring...\n")
            player_1.money += player_1.bet
        elif player_1.get_hand_value() < dealer.get_hand_value():
            time.sleep(1)
            print("You lose, #sad\n")
    return start_turn()

def print_display():
    print("\nDealer's cards:   {}    = {}\n".format((" + ".join(dealer.hand)), dealer.get_hand_value()))
    print("\nYour cards:       {}    = {}\n".format((" + ".join(player_1.hand)), player_1.get_hand_value()))
    
def game_loop():
    while True:
        action = input("\n")
        if action == "h": #hit
            player_1.get_card_from_deck()
            print("\nYour cards:       {}    = {}".format((" + ".join(player_1.hand)), player_1.get_hand_value()))
            if player_1.get_hand_value() > 21:
                print("\nYou busted! You lose\n")
                return start_turn()
        elif action == "d": #double
            player_1.bet *= 2
            player_1.money -= player_1.bet/2
            print("Bet: {}                 Cash: $ {}\n".format(player_1.bet, player_1.money))
            player_1.get_card_from_deck()
            time.sleep(1)
            dealers_play()
        elif action == "s": #stand
            dealers_play()
        elif action == "e": #exit
            return sys.exit()
                   
def start_turn():
    print("You have ${}, please enter your bet: \n".format(int(player_1.money)))
    player_1.bet = input("")
    player_1.bet = int(player_1.bet)
    player_1.money = int(player_1.money)
    player_1.hand = []
    dealer.hand = []
    player_1.get_card_from_deck()
    player_1.get_card_from_deck()
    dealer.get_card_from_deck()
    player_1.money -= player_1.bet
    print("\n-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")
    print("\nBet: {}                 Cash: $ {}\n".format(player_1.bet, player_1.money))
    print("Dealer's cards:   {}    = {}\n".format((" + ".join(dealer.hand)), dealer.get_hand_value()))
    if player_1.get_hand_value() == 21:
        print("Your cards:       {}    = {}\n".format((" + ".join(player_1.hand)), player_1.get_hand_value()))
        print("\nBlackjack!")
        dealer.get_card_from_deck()
        print("Dealer's cards:   {}    = {}\n".format((" + ".join(dealer.hand)), dealer.get_hand_value()))
        if dealer.get_hand_value() == 21:
            print ("\nOMG, it is a tie!")
            player_1.money += player_1.bet
            return start_turn()
        else:
            print ("\nLucky bastard, you win!")
            player_1.money += int(1.5 * player_1.bet)
            return start_turn()
    else:
        print("Your cards:       {}    = {}\n".format((" + ".join(player_1.hand)), player_1.get_hand_value()))
    print("To hit press h, to stand press s, to double press d and to exit press e:   ")
    game_loop()
    
#Iniciar juego

action = ""
deck_1 = Stack_of_cards()
player_1 = Player(False, "Player 1")
dealer = Player("Dealer")
print("----------- Luisito's Blackjack -----------\n")
start_turn()

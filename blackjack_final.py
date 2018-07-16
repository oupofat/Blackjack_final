import random

#records class
class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__
#function definitions

#this grabs a random card number or face card
def deal_random_card():
      #this chunk randoms a suit
    face_card = 0 
    suits = ['of Hearts','of Diamonds', 'of Spades', 'of Clovers']
    suit_pick = random.choice(suits)

    number_card = [2,3,4,5,6,7,10,"Jack", "Queen", "King", "Ace"]
    card_pick = random.choice(number_card)
    if card_pick == ("Jack"):
        face_card = 10
    elif card_pick == ("Queen"):
        face_card = 10
    elif card_pick == ("King"):
        face_card = 10
    #if ace player chooses if they want a 1 or 11.
    elif card_pick == "Ace":
        face_card = int(input("Do you want it to be a 1 or 11?"))
    else:
        face_card = card_pick
    return(face_card,suit_pick)

    #looking at trying to put the hit card into a function
def get_player_cards(total):
    hit_card = 0
    while True:
        if player1.total <= 21:            
            hit_me = input("Would you like a another card, hit or n")
            if hit_me == "hit":
                hit_card = deal_random_card()
                print(hit_card)
                player1.total += hit_card[0]
                print("Your new total is ", player1.total)
            if player1.total >= 22:
                print (player1.total, "You lose")
                return(player1.total)
            if hit_me == "n":
                print("Stay")
                print("Staying on ",player1.total)
                return (player1.total)

#dealer draw cards
def draw_cards_for_dealer(total_dealer):
    draw_card = 0 

    while True:
        if total_dealer <= 16:
            draw_card = deal_random_card()
            print(draw_card)
            total_dealer += draw_card[0]
        if total_dealer >= 17:
            if total_dealer > 21:
                print(total_dealer,"dealer bust")
                return(total_dealer)
            else:
                print(total_dealer, "dealer stays")
                return(total_dealer)


print ("**********************************")
print ("*welcome to the game of Blackjack*")
print ("*      closest to 21 wins        *")
print ("* Don't go over or you will lose *")
print ("**********************************")

#import statements
#counter for player
#player1_card1 = 0
#player1_card2 = 0
#total_player1 = 0

#dealer draw cards
#dealer_card1 = 0 
#dealer_card2 = 0 
#total_dealer = 0 
#records for player one and the dealer.
player1 = Record (
    card1 = 0,
    card2 = 0, 
    total = 0,
    )

dealer = Record(
    dealer_card_one = 0, 
    dealer_card_two = 0, 
    total_dealer = 0,
    )


#variable initialization

#prints player ones cards
player1.card1 = deal_random_card()
print (player1.card1)
player1.card2 = deal_random_card()
print (player1.card2)
#adds the total for the player one and prints it grabbing the first postion in the tuple.
player1.total = (player1.card1[0] + player1.card2[0])
print ("Your total is" , player1.total, "Player one")

#dealer cards section
dealer_card1 = deal_random_card()
print(dealer_card1)
dealer_card2 = deal_random_card()
print(dealer_card2)
#adds the total for the dealer prints it grabbing the first postions in the tuple
total_dealer = (dealer_card1[0] + dealer_card2[0])


#main program

#the actual game play 
def run_game_play_find_winner(dealer, player1):
    if player1 < dealer:
        print("dealer wins")
    if player1 > dealer:
        print("player one wins")
    if player1 == dealer:
        print("its a tie! Push!!")
    
dealer = draw_cards_for_dealer(total_dealer)
#print("dealer",dealer)
if dealer <=21:
  player1 = get_player_cards(player1.total)  
  #print("player1",player1) 
  if player1 <= 21:

    run_game_play_find_winner(dealer,player1)  
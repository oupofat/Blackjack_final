import random
#counter for player
player1_card1 = 0
player1_card2 = 0
total_player1 = 0
face_card = 0
#dealer draw cards
dealer_card1 = 0 
dealer_card2 = 0 
total_dealer = 0 
face_card = 0 
print ("welcome to the game of Blackjack")
print ("closest to 21 wins")
print ("____________________")

#this chunk randoms a suit
suits = ['of Hearts', 'of Diamonds', 'of Spades', 'of Clovers']
suit_pick = random.choice(suits)    

#this grabs a random card number or face card
def get_card_pick():
    number_card = [2,3,4,5,6,7,10,"Jack", "Queen", "King"]
    card_pick = random.choice(number_card)
    if card_pick == ("Jack"):
        face_card = 10
    elif card_pick == ("Queen"):
        face_card = 10
    elif card_pick == ("King"):
        face_card = 10
    #if ace player chooses if they want a 1 or 11.
    elif card_pick == "Ace":
        face_card = int(input("do you want it to be a 1 or 11?"))
    else:
        face_card = card_pick
    return (face_card)

#prints player ones cards
player1_card1 = get_card_pick()
print (player1_card1, suit_pick)
player1_card2 = get_card_pick()
print (player1_card2, suit_pick)
#adds the total for the player one and prints it
total_player1 = player1_card1 + player1_card2
print ("Your total is" , total_player1, "Player one")

#looking at trying to put the hit card into a function
def card_total(total_player1):
    hit_card = 0
    while True:
        if total_player1 <= 21:            
            hit_me = input("do you want a another card, hit or n")
            if hit_me == "hit":
                hit_card = get_card_pick()
                print(hit_card, suit_pick)
                total_player1 += hit_card
                print("Your new total is ", total_player1)
            if total_player1 >= 22:
                print (total_player1, "You lose")
                break
            if hit_me == "n":
                print("Stay")
                print("Staying on ",total_player1)
                return (total_player1)

#dealer cards section
dealer_card1 = get_card_pick()
print(dealer_card1, suit_pick)
dealer_card2 = get_card_pick()
print(dealer_card2, suit_pick)
total_dealer = dealer_card1 + dealer_card2
#dealer draw cards
def dealer_cards (total_dealer):
    draw_card = 0 

    while True:
        if total_dealer <= 16:
            draw_card = get_card_pick()
            print(draw_card, suit_pick)
            total_dealer += draw_card
        if total_dealer >= 17:
            if total_dealer > 21:
                print(total_dealer,"dealer bust")
                stop
                return(total_dealer)
            else:
                print(total_dealer, "dealer stays")
                return(total_dealer)

#the actual game play 
def game_play(dealer, player1):
    if player1 < dealer:
        print("dealer wins")
    if player1 > dealer:
        print("player one wins")
    if player1 == dealer:
        print("its a tie! Push!!")
    
dealer = dealer_cards(total_dealer)
player1 = card_total(total_player1)
game_play(dealer,player1)  
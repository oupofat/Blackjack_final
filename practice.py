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

#this chunk randoms a suit
suits = ['of Hearts', 'of Diamonds', 'of Spades', 'of Clovers']
suit_pick = random.choice(suits)      
#this grabs a random card number or face card
def get_card_pick():
    number_card = [2,3,4,5,6,7,9,10,"Ace","Jack", "Queen", "King"]
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
print (total_player1)
print ("Your total is" , total_player1, "Player one")
#dealer cards section
dealer_card1 = get_card_pick()
dealer_card2 = get_card_pick()
print (dealer_card1,suit_pick, ",", dealer_card2, suit_pick)
total_dealer = dealer_card1 + dealer_card2
print (total_dealer)
#looking at trying to put the hit card into a function
def card_total():
    hit_card = 0
    total = 0
    while True:
        if total <= 21:
            hit_me = input("do you want a another card, hit or n")
            if hit_me == "hit":
                hit_card = get_card_pick()
                hit_card += int(input("add card to your hand "))
                total = hit_card 
                print("Your new total is ", total)
            if hit_card > 21:
                print (total, "You lose")
                return (total)
            if hit_me == "n":
                print("Stay")
                print("Staying on ",total)
                return (total)
total_player1 = card_total()
total_dealer = card_total()
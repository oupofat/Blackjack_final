import random
#counter for players
player1_card1 = 0
player1_card2 = 0
total_player1 = 0
face_card = 0


#this chunk randoms a suit
suits = ['of Hearts', 'of Diamonds', 'of Spades', 'of Clovers']
suit_pick = random.choice(suits)      
#this grabs a random card number or face card
def get_card_pick():
    number_card = [2,3,4,5,6,7,9,10,"Ace","Jack", "Queen"]
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
player1_card1 = get_card_pick()
player1_card2 = get_card_pick()
#prints player ones cards
print (player1_card1, suit_pick)
print (player1_card2, suit_pick)
#adds the total for the player one and prints it
total_player1 = player1_card1 + player1_card2
print (total_player1)
#looking at trying to put the hit card into a function
def card_total():
    hit_card = 0
    total = 0
    while True:
        if total <= 21:
            hit_me = input("do you want a another card, hit or n")
            if hit_me == "hit":
                hit_card = get_card_pick()
                hit_card += int(input("add card to your hand"))
                total = hit_card 
            if hit_card > 21:
                print ("You lose")
                return (total)
            if hit_me == "n":
                print("Stay")
                print(total)
                return (total)
card_total()
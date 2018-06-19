import random
#counter for players
player1_card1 = 0
player1_card2 = 0
player2_card1 = 0
player2_card2 = 0
face_card = 0


#this chunk randoms a suit
suits = ['of Hearts', 'of Diamonds', 'of Spades', 'of Clovers']
suit_pick = random.choice(suits)      

def get_card_pick():
    number_card = [2,3,4,5,6,7,8,9,10,"Ace","Jack", "Queen"]
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
print (player1_card1, suit_pick)
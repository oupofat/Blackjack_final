import random
#counter for players
player1_card1 = 0
player1_card2 = 0
player2_card1 = 0
player2_card2 = 0

#this chunk randoms a suit
suits = ['of Hearts', 'of Diamonds', 'of Spades', 'of Clovers']
suit_pick = random.choice(suits)      
print (suit_pick)

def random_pick():

    number_card = [2,3,4,5,6,7,8,9,10,"ace","Jack", "Queen","King"]
    card_pick = random.choice(number_card)
    print(card_pick)
    if card_pick == ("Jack"):
        face_card = 10
    if card_pick == ("Queen"):
        face_card = 10
    if card_pick == ("King"):
        face_card = 10
    #if ace player chooses if they want a 1 or 11.
    if card_pick == "ace":
        face_card = int(input("do you want it to be a 1 or 11?"))
    print(face_card)
    return (card_pick or face_card)
    
random_pick()  
print(random_pick, suit_pick)
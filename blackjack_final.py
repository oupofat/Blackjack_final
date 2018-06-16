import random

suits = ['hearts', 'diamonds', 'spades', 'clovers']

    
suit_pick = random.choice(suits)

        
print (suit_pick)
number_card = [2,3,4,5,6,7,8,9,10, "Jack", "Queen","King"]
face_cards = {
    Jack : 10,
    Queen : 10,
    King : 10
}
number_pick = random.choice(number_card)
if number_pick == "face_cards":
    
    
print(number_pick, suit_pick)


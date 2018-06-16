import random

suits = ['hearts', 'diamonds', 'spades', 'clovers']

    
suit_pick = random.choice(suits)

        
print (suit_pick)
number_card = [2,3,4,5,6,7,8,9,10,"ace","Jack", "Queen","King"]

number_pick = random.choice(number_card)
face_cards = {
    "Jack" : 10,
    "Queen" : 10,
    "King" : 10,
}
if number_pick == "ace":
    ace_choice = input("do you want it to be a 1 or 11?")
    
    
    
    
print(number_pick, suit_pick)


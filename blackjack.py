dealers_hand = []
players_hand = []

# deck = {'king of hearts': 10, 'king of diamonds': 10, 'king of spades': 10, 'king of clubs': 10, 'queen of hearts': 10, 'queen of diamonds': 10, 'queen of spades': 10, 'queen of clubs': 10, 'jack of hearts': 10, 'jack of diamonds': 10, 'jack of spades': 10, 'jack of clubs': 10, 'nine of hearts': 9, 'nine of diamonds': 9, 'nine of spades': 9, 'nine of clubs': 9, 'eight of hearts': 8, 'eight of diamonds': 8, 'eight of spades': 8, 'eight of clubs': 8, 'seven of hearts': 7, 'seven of diamonds': 7, 'seven of spades': 7, 'seven of clubs': 7, 'six of hearts': 6, 'six of diamonds': 6, 'six of spades': 6, 'six of clubs': 6, 'five of hearts': 5, 'five of diamonds': 5, 'five of spades': 5, 'five of clubs': 5, 'four of hearts': 4, 'four of diamonds': 4, 'four of spades': 4, 'four of clubs': 4, 'three of hearts': 3, 'three of diamonds': 3, 'three of spades': 3, 'three of clubs': 3, 'two of hearts': 2, 'two of diamonds': 2, 'two of spades': 2, 'two of clubs': 2, 'ace of hearts': 11, 'ace of diamonds': 11, 'ace of spades': 11, 'ace of clubs': 11}

# print(deck.items())
# import random
# counter = 4
# while counter > 0:
#     deck.items()
#     players_hand.add(deck.pop(random.choice(deck.items())))
#     dealers_hand.append(deck.pop(random.choice(deck.items())))
#     counter -= 2

deck = [['king of hearts', 10], ['king of diamonds', 10], ['king of spades', 10], ['king of clubs', 10], ['queen of hearts', 10], ['queen of diamonds', 10], ['queen of spades', 10], ['queen of clubs', 10], ['jack of hearts', 10], ['jack of diamonds', 10], ['jack of spades', 10], ['jack of clubs', 10], ['nine of hearts', 9], ['nine of diamonds', 9], ['nine of spades', 9], ['nine of clubs', 9], ['eight of hearts', 8], ['eight of diamonds', 8], ['eight of spades', 8], ['eight of clubs', 8], ['seven of hearts', 7], ['seven of diamonds', 7], ['seven of spades', 7], ['seven of clubs', 7], ['six of hearts', 6], ['six of diamonds', 6], ['six of spades', 6], ['six of clubs', 6], ['five of hearts', 5], ['five of diamonds', 5], ['five of spades', 5], ['five of clubs', 5], ['four of hearts', 4], ['four of diamonds', 4], ['four of spades', 4], ['four of clubs', 4], ['three of hearts', 3], ['three of diamonds', 3], ['three of spades', 3], ['three of clubs', 3], ['two of hearts', 2], ['two of diamonds', 2], ['two of spades', 2], ['two of clubs', 2], ['ace of hearts', 11], ['ace of diamonds', 11], ['ace of spades', 11], ['ace of clubs', 11]]

import random
counter = 4 
while counter > 0:
    players_hand.append(deck.pop(random.randrange(len(deck))))
    dealers_hand.append(deck.pop(random.randrange(len(deck))))
    counter -= 2


print(players_hand)
print(dealers_hand)
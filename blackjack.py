
print('Type your name to start: ')
player_name = input()
print('Welcome to Terminal Blackjack ' + player_name + '!')

dealers_hand = []
players_hand = []
deck = [['king of hearts', 10], ['king of diamonds', 10], ['king of spades', 10], ['king of clubs', 10], ['queen of hearts', 10], ['queen of diamonds', 10], ['queen of spades', 10], ['queen of clubs', 10], ['jack of hearts', 10], ['jack of diamonds', 10], ['jack of spades', 10], ['jack of clubs', 10], ['nine of hearts', 9], ['nine of diamonds', 9], ['nine of spades', 9], ['nine of clubs', 9], ['eight of hearts', 8], ['eight of diamonds', 8], ['eight of spades', 8], ['eight of clubs', 8], ['seven of hearts', 7], ['seven of diamonds', 7], ['seven of spades', 7], ['seven of clubs', 7], ['six of hearts', 6], ['six of diamonds', 6], ['six of spades', 6], ['six of clubs', 6], ['five of hearts', 5], ['five of diamonds', 5], ['five of spades', 5], ['five of clubs', 5], ['four of hearts', 4], ['four of diamonds', 4], ['four of spades', 4], ['four of clubs', 4], ['three of hearts', 3], ['three of diamonds', 3], ['three of spades', 3], ['three of clubs', 3], ['two of hearts', 2], ['two of diamonds', 2], ['two of spades', 2], ['two of clubs', 2], ['ace of hearts', 11], ['ace of diamonds', 11], ['ace of spades', 11], ['ace of clubs', 11]]

print('The cards are being dealt....')

# OG Fucntion
import random
counter = 4 
while counter > 0:
    players_hand.append(deck.pop(random.randrange(len(deck))))
    dealers_hand.append(deck.pop(random.randrange(len(deck))))
    counter -= 2
# print(players_hand)
# print(dealers_hand)

fullp_hand = [card for hand in players_hand for card in hand]
# print(full_hand)
print('You\'ve been dealt the ' + fullp_hand[0] + ' and the ' + fullp_hand[2])

fulld_hand = [card for hand in dealers_hand for card in hand]
# print(fulld_hand)
print('You\'re playing against ' + fulld_hand[0])
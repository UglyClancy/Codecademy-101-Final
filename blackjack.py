
print('Type your name to start: ')
player_name = input()
print('Welcome to Terminal Blackjack ' + player_name + '!')

dealers_hand = []
players_hand = []
deck = [['king of hearts', 10], ['king of diamonds', 10], ['king of spades', 10], ['king of clubs', 10], ['queen of hearts', 10], ['queen of diamonds', 10], ['queen of spades', 10], ['queen of clubs', 10], ['jack of hearts', 10], ['jack of diamonds', 10], ['jack of spades', 10], ['jack of clubs', 10], ['nine of hearts', 9], ['nine of diamonds', 9], ['nine of spades', 9], ['nine of clubs', 9], ['eight of hearts', 8], ['eight of diamonds', 8], ['eight of spades', 8], ['eight of clubs', 8], ['seven of hearts', 7], ['seven of diamonds', 7], ['seven of spades', 7], ['seven of clubs', 7], ['six of hearts', 6], ['six of diamonds', 6], ['six of spades', 6], ['six of clubs', 6], ['five of hearts', 5], ['five of diamonds', 5], ['five of spades', 5], ['five of clubs', 5], ['four of hearts', 4], ['four of diamonds', 4], ['four of spades', 4], ['four of clubs', 4], ['three of hearts', 3], ['three of diamonds', 3], ['three of spades', 3], ['three of clubs', 3], ['two of hearts', 2], ['two of diamonds', 2], ['two of spades', 2], ['two of clubs', 2], ['ace of hearts', 11], ['ace of diamonds', 11], ['ace of spades', 11], ['ace of clubs', 11]]
# deck = ['king of hearts', 'king of diamonds', 'king of spades', 'king of clubs', 'queen of hearts', 'queen of diamonds', 'queen of spades', 'queen of clubs', 'jack of hearts', 'jack of diamonds', 'jack of spades', 'jack of clubs', 'nine of hearts', 'nine of diamonds', 'nine of spades', 'nine of clubs', 'eight of hearts', 'eight of diamonds', 'eight of spades', 'eight of clubs', 'seven of hearts', 'seven of diamonds', 'seven of spades', 'seven of clubs', 'six of hearts', 'six of diamonds', 'six of spades', 'six of clubs', 'five of hearts', 'five of diamonds', 'five of spades', 'five of clubs', 'four of hearts', 'four of diamonds', 'four of spades', 'four of clubs', 'three of hearts', 'three of diamonds', 'three of spades', 'three of clubs', 'two of hearts', 'two of diamonds', 'two of spades', 'two of clubs', 'ace of hearts', 'ace of diamonds', 'ace of spades', 'ace of clubs']

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
# print(fullp_hand)
print('You\'ve been dealt the ' + fullp_hand[0] + ' and the ' + fullp_hand[2])

fulld_hand = [card for hand in dealers_hand for card in hand]
# print(fulld_hand)
print('You\'re playing against ' + fulld_hand[0])

print('Would you like to hit or stay: ')
# hit_or_stay = input()
counter2 = 3
while counter2 > 0:
    hit_or_stay = input()
    if hit_or_stay == 'hit':
        players_hand.append(deck.pop(random.randrange(len(deck))))
        print(players_hand)
        print('Would you like to hit or stay: ') 
        counter2 -= 1
    elif hit_or_stay == 'stay':
        break

fullp_hand = [card for hand in players_hand for card in hand]

for cards in fullp_hand:
    if(type(cards) == str):
        print('Your hand consists of: ' + cards)

player_points = 0
for cards in fullp_hand:
    if(type(cards) == int):
        player_points += cards
# print(player_points)

dealer_points = 0
for cards in fulld_hand:
    if(type(cards) == int):
        dealer_points += cards
# print(dealer_points)

if player_points > dealer_points:
    print('You beat the dealer! We have a winner!')
elif player_points == 21 and player_points > dealer_points:
    print('Blackjack! You win!')
elif player_points == dealer_points:
    print('We have a tie! You lose nothing.')
elif player_points < dealer_points:
    print('Oh you lost! Tough luck, better try again next time.')

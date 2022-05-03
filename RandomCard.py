import random

card = random.randint(1, 13)
suit = random.randint(1, 4)

if card == 1:
    card = "Ace"
elif card == 11:
    card = "Jack"
elif card == 12:
    card = "Queen"
elif card == 13:
    card = "King"

if suit == 1:
    suit = "Diamonds"
elif suit == 2:
    suit = "Hearts"
elif suit == 3:
    suit = "Clubs"
elif suit == 4:
    suit = "Spades"

print('Your random card is:', card, 'of', suit + ".")

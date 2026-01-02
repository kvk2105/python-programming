import random
suits = ['hearts', 'spades', 'diamonds', 'clubs']
ranks = ['A','2','3','4','5','6','7','8','9','10','J','K','Q']
cards = []

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

# print (cards) 
def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt = []
    for n in range(number):
        cards_dealt.append(cards.pop())
    return cards_dealt


# print (random.shuffle(cards))
# print (cards)
card = cards.pop()
# print ('card is: ',card)

shuffle()
card = deal(2)[0]
print(card[1])
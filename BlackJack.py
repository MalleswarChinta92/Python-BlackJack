import random

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def firstDeal(self):
        card1 = self.cards.pop()
        card2 = self.cards.pop()
        card3 = self.cards.pop()
        card4 = self.cards.pop()
        return ([card1, card3], [card2, card4])
    def drawCard(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def addCard(self, card):
        self.cards.append(card)
        if (card.rank == 'Ace'):
            self.aces = self.aces + 1
        self.value += card.value
    def adjustAces(self):
        pass
    def isDirectBlackJack(self):
        if len(self.cards) == 2:
            if (self.cards[0].value + self.cards[1].value == 21):
                return True
        return False

class Chips():
    def __init__(self,total=100,bet=5):
        self.total = total
        self.bet = bet
    def winBet(self):
        print(f'User won a bet of {self.bet}')
        self.total += self.bet
    def loseBet(self):
        print(f'User lost a bet of {self.bet}')
        self.total -= self.bet

def showFullCards(cards):
    print('-----------------')
    for card in cards:
        print(card)

def showPartialCards(cards):
    print('-----------------')
    card = cards[0]
    print(card)

def bet():
    while True:
        try:
            bet = int(input('Enter bet '))
        except:
            print('Give a numerical value')
            continue
        else:
            if (bet > chips.total):
                print(f'Enter bet less than {chips.total}')
                continue
            elif (bet == 0):
                print('Bet cannot be zero')
                continue
            else:
                break
    chips.bet = bet

suits = ('Heart', 'Diamond', 'Spade', 'Club')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
'Seven': 7, 'Eight': 8, 'Nine': 9, 'Jack': 10, 'Queen': 10, 'King': 10,
'Ace': 11}

chips = Chips()

while True:
    if chips.total == 0:
        print('You are poor')
        break
    bet()
    dealerWin = False 
    playerWin = False
    deck = Deck()
    deck.shuffle()
    (dealerCards,playerCards) = deck.firstDeal()
    print('Dealer cards')
    showPartialCards(dealerCards)
    print('\nplayer cards')
    showFullCards(playerCards)
    hand = Hand()
    for card in playerCards:
        hand.addCard(card)
    print(hand.value)

    while playerWin == False and dealerWin == False:
        if (hand.isDirectBlackJack()):
            playerWin = True
            chips.bet = chips.bet * 1.5
            chips.winBet()
            break
        elif(hand.value == 21):
            playerWin = True
            chips.winBet()
            break
        elif(hand.value > 21):
            dealerWin = True
            chips.loseBet()
            break
        while True:
            try:
                userAction = int(input('choose 1 for HIT 2 for Stand'))
            except TypeError:
                print('please select 1 or 2')
                continue
            else:
                if userAction != 1 and userAction != 2:
                    print('please select 1 or 2')
                    continue
                else:
                    break
        if(userAction == 1):
            drawCard = deck.drawCard()
            print('HIT with')
            print(drawCard)
            hand.addCard(drawCard)
            showFullCards(hand.cards)
            print(hand.value)
            continue
        else:
            dealerValue = 0
            print('\n dealer cards')
            showFullCards(dealerCards)
            for card in dealerCards:
                dealerValue += card.value
            if(dealerValue == 21):
                dealerWin = True
                chips.loseBet()
                break
            while(dealerValue < 17):
                drawCard = deck.drawCard()
                print(f'dealer card {drawCard}')
                dealerValue += drawCard.value
            print(f'Dealer {dealerValue}')
            print(f'Player {hand.value}')
            if (dealerValue > 21):
                playerWin = True
                chips.winBet()
            elif(dealerValue > hand.value):
                dealerWin = True
                chips.loseBet()
            elif(hand.value > dealerValue):
                playerWin = True
                chips.winBet()
            else:
                print('Push')
            break
    playAgain = input('input Y to play again')
    if(playAgain == 'Y'):
        continue
    else:
        break
import random
from re import A
class Game:
    def __init__(self, deck, playerList, cardList1, cardList2, cardList3, cardList4):
        playerList.append(Players("Player",deck, cardList1,cardList2, cardList3, cardList4))
        playerList.append(Players("Bot1",deck, cardList1,cardList2, cardList3, cardList4))
        playerList.append(Players("Bot2",deck, cardList1,cardList2, cardList3, cardList4))
        playerList.append(Players("Bot3",deck, cardList1,cardList2, cardList3, cardList4))
        playerList[0].next = playerList[1]
        playerList[1].next = playerList[2]
        playerList[2].next = playerList[3]
        playerList[3].next = playerList[0]
        self.currentCard = random.choice(deck)
        self.currentPlayer = playerList[0]
        while True:
            print(self.currentCard.color, (self.currentCard.number))
            self.currentCard = self.currentPlayer.play( self.currentPlayer.name ,deck, self.currentCard, cardList1,cardList2, cardList3, cardList4)
            self.currentPlayer = self.currentPlayer.next 
class Deck:
    def form_deck(deck): 
        deck.append(Cards("blue", 4))
        deck.append(Cards("blue", 5))
        deck.append(Cards("blue", 6))
        deck.append(Cards("blue", 7))
        deck.append(Cards("blue", 8))
        deck.append(Cards("blue", 9))
        deck.append(Cards("blue", 10)) # plus 2
        deck.append(Cards("blue", 11)) # reverse
        deck.append(Cards("blue", 12)) # shush
        deck.append(Cards("red", 0))
        deck.append(Cards("red", 1))
        deck.append(Cards("red", 2))
        deck.append(Cards("red", 3))
        deck.append(Cards("red", 4))
        deck.append(Cards("red", 5))
        deck.append(Cards("red", 6))
        deck.append(Cards("red", 7))
        deck.append(Cards("red", 8))
        deck.append(Cards("red", 9))
        deck.append(Cards("red", 10)) # plus 2
        deck.append(Cards("red", 11)) # reverse
        deck.append(Cards("red", 12)) # shush
        deck.append(Cards("yellow", 0))
        deck.append(Cards("yellow", 1))
        deck.append(Cards("yellow", 2))
        deck.append(Cards("yellow", 3))
        deck.append(Cards("yellow", 4))
        deck.append(Cards("yellow", 5))
        deck.append(Cards("yellow", 6))
        deck.append(Cards("yellow", 7))
        deck.append(Cards("yellow", 8))
        deck.append(Cards("yellow", 9))
        deck.append(Cards("yellow", 10)) # plus 2
        deck.append(Cards("yellow", 11)) # reverse
        deck.append(Cards("yellow", 12)) # shush
        deck.append(Cards("green", 0))
        deck.append(Cards("green", 1))
        deck.append(Cards("green", 2))
        deck.append(Cards("green", 3))
        deck.append(Cards("green", 4))
        deck.append(Cards("green", 5))
        deck.append(Cards("green", 6))
        deck.append(Cards("green", 7))
        deck.append(Cards("green", 8))
        deck.append(Cards("green", 9))
        deck.append(Cards("green", 10)) #plus2
        deck.append(Cards("green", 11)) #reverse
        deck.append(Cards("green", 12)) #shush
        deck.append(Cards("none", 10))
        deck.append(Cards("none", 10))
        deck.append(Cards("none", 10))
        deck.append(Cards("none", 10))
        deck.append(Cards("none", 0))
        deck.append(Cards("none", 0))
        deck.append(Cards("blue", 0))
        deck.append(Cards("blue", 1))
        deck.append(Cards("blue", 2))
        deck.append(Cards("blue", 3))
class Players:
    def __init__(self,name,deck,cardList1, cardList2, cardList3, cardList4):
        self.name = name
        self.cardNumber = 0
        for i in range(7):
            self.draw(deck, cardList1,cardList2, cardList3, cardList4)
        #self.next
    def draw(self,deck,cardList1,cardList2,cardList3,cardList4):
        if self.name == "Player":
            cardList1.append(random.choice(deck))
        elif self.name == "Bot1":
            cardList2.append(random.choice(deck))
        elif self.name == "Bot2":
            cardList3.append(random.choice(deck))
        elif self.name == "Bot3":
            cardList4.append(random.choice(deck))
        #deck.remove(cardList[self.cardNumber])
        self.cardNumber += 1
    def play(self, name, deck, currentCard, cardList1, cardList2, cardList3, cardList4):
        if name == "Player":
            a = False
            for i in cardList1:
                if currentCard.number == i.number or currentCard.color == i.color:
                    a = True
                    break
            if a:
                while (True):
                    for t in range(self.cardNumber):
                        print(cardList1[t].color, cardList1[t].number)
                    choice = int(input("Enter the index of the card you want to play.\n"))
                    if currentCard.number == cardList1[choice].number or currentCard.color == cardList1[choice].color:
                        currentCard = cardList1[choice]
                        cardList1.remove(cardList1[choice])
                        break
            else:
                self.draw(deck, cardList1,cardList2, cardList3, cardList4)   
        else:
            print("It's ", name, "'s turn")
            bool = False
            if self.name == "Bot1":
                for i in cardList2:
                    if currentCard.number == i.number or currentCard.color == i.color:
                        currentCard = i
                        cardList2.remove(i)
                        bool = True # i index(F) or element(T)of list
                        #append this card to deck maybe.
            elif self.name == "Bot2":
                for i in cardList3:
                    if currentCard.number == i.number or currentCard.color == i.color:
                        currentCard = i
                        cardList3.remove(i)
                        bool = True # i index(F) or element(T)of list
                        #append this card to deck maybe.
            elif self.name == "Bot3":
                for i in cardList4:
                    if currentCard.number == i.number or currentCard.color == i.color:
                        currentCard = i
                        cardList4.remove(i) 
                        bool = True # i index(F) or element(T)of list
                        #append this card to deck maybe.
            if bool == False:
                self.draw(deck, cardList1,cardList2, cardList3, cardList4)
class Cards:
    def __init__(self,color,number):
        self.color = color
        self.number = number
    def plus(self, currentPlayer):
        if self.number == 11:
            for i in range(2):
                currentPlayer.next.draw()
    def reverse(self, player):
        if self.number == 11:
            if player[0].next == player[1]:
                player[3].next = player[2]
                player[2].next = player[1]
                player[1].next = player[0]
                player[0].next = player[3]
            else:
                player[0].next = player[1]
                player[1].next = player[2]
                player[2].next = player[3]
                player[3].next = player[0]
    def shush(self, currentPlayer):
        if self.number == 12:
            currentPlayer = currentPlayer.next


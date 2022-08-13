class Players:
    def __init__(self):
        self.cardNumber = 7
        #self.cardList = for i in self.cardNumber 
    def draw(self):
        self.cardList[cardNumber] = deck[0]
        deck.pop(0)
        self.cardNumber += 1
    def play(self):
        for i in self.cardList:
            if currentCard.number == i.number or currentCard.color == i.color:
                currentCard = i
                self.cardList.remove(i) # i index(F) or element(T)of list
        self.draw(self)
class Cards:
    def __init__(self,color,number,plus,reverse,shush):
        self.color = color
        self.number = number
        self.plus = plus
        self.reverse = reverse
        self.shush = shush
    def plus(self, currentPlayer):
        if self.plus != 0:
            for i in self.plus:
                currentPlayer.next.draw()
    def reverse(self, *player):
        if self.reverse == True:
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
        if self.shush == True:
            currentPlayer = currentPlayer.next


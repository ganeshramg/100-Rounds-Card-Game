#Deck of card game with maximum 100 rounds
#Whoever won maximum number of rounds wins the game

from random import shuffle

signs = 'H S D C'.split()
numbers = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

deck = []

#List of lists containing symbol and number makes the deck
for sign in signs:
    for number in numbers:
        deck.append([sign,number])

#Player Class
class Player:
    def __init__(self,name,deck,roundsWon=0):
        self.name = name
        self.deck = deck
        self.roundsWon = roundsWon

    def placeCard(self):
        return self.deck.pop(0)


#Game Class
class Game:
    def __init__(self):
        self.board = []

    def returnCards(self):
        return self.board


print("---shuffling deck---")
shuffle(deck)

# input player name

name1 = input("Enter your name : ")
print("---Creating Players---")

# Creating player instances
player1 = Player(name1,deck[:26])
player2 = Player('Computer',deck[26:])

# list of player instances
players = [player1,player2]

print("Welcome {}".format(name1))
print("{} vs Computer".format(name1))

#New Game instance created
game = Game()

print("Game Starts!")

#To update number of rounds and drawss
round=1
draws=0

while((len(player1.deck)>0) & (len(player2.deck)>0)):

    if(round==101):
        break

    for player in players:
        board = game.board
        board.append(player.placeCard())


    print("\nRound {}".format(round))
    print(board)


    if(numbers.index(board[0][1])>numbers.index(board[1][1])):
        print("{} wins round {}".format(player1.name,round))
        player1.roundsWon+=1
        player1.deck.extend(game.returnCards())


    elif(numbers.index(board[0][1])<numbers.index(board[1][1])):
        print("{} wins round {}".format(player2.name,round))
        player2.deck.extend(game.returnCards())
        player2.roundsWon+=1


    else:
        print("DRAW")
        draws+=1

    game.board = []  #Empty the board

    round+=1

print('\n')
print("{} has {} cards remaining\n".format(player1.name,len(player1.deck)))
print("{} has {} cards remaining\n".format(player2.name,len(player2.deck)))

print("{} number of draws".format(draws))

print("{} has won {} rounds".format(player1.name,player1.roundsWon))
print("{} has won {} rounds".format(player2.name,player2.roundsWon))

if(player1.roundsWon>player2.roundsWon):
    print("{} wins the game!!".format(player1.name))
else:
    print("{} wins the game!!".format(player2.name))

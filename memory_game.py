'''
Name: Estephanos B. Jebessa
CSC 201
Programming Project 4--Memory Game

Program Description: This program is a graphics-based computer memory game where two users compete to see who can find the
most matches. The game consists of a board of 24 cards with 12 different images. The goal of the game is to find a match for the card you click on.
The two players are distinguished by the color of the X marked on the matched cards.
The program uses Board class, which draws a board of 24 cards, and Card class which draws a single card and flips it to show the image.


Documentation of assistance (who and what):


'''
from graphics import *
from board import *
from card import *
import time

PLAYER_ONE = 'red'
PLAYER_TWO = 'blue'

def giveInstructions():
    '''
    This function provides instructions on how to play the game.
    '''
    instructWin = GraphWin("How to play", 700, 300)
    instructWin.setBackground('cyan')
    instructions = Text(Point(350, 150),
                        "Two players take turns to find matching cards.\n\n"
                        "Player one has red color and player two has blue color.\n\n"
                        "Player one goes first.\n\n"
                        "Click on two cards to flip them over.\n\n"
                        "Your turn continues as long as you find matches.\n\n"
                        "Click to begin the game.")
    instructions.setSize(18)                    
    instructions.draw(instructWin)
    instructWin.getMouse()
    instructWin.close()
    
    
def markCards(window, currentPlayer, card1, card2, firstPlayerList, secondPlayerList):  
    '''
    This function marks the matched cards with an X with the color of the corresponding player using the Card method markMatched.
    It then adds the cards to the corresponding player's list.

    Params:
    window(GraphWin): Window where the game takes place.
    currentPlayer(string): status of whose turn it is: player one or player two.
    card1(Card): the first picked card
    card2(Card): second picked card
    firstPlayerList(List): a list that contains the cards that the first player got matched.
    secondPlayerList(List): a list that contains the cards that the second player got matched.
    '''
    
    if currentPlayer == PLAYER_ONE:
        card1.markMatched(window, PLAYER_ONE)
        card2.markMatched(window, PLAYER_ONE)
        firstPlayerList.append(card1)
        firstPlayerList.append(card2)
        
    elif currentPlayer == PLAYER_TWO:
        card1.markMatched(window, PLAYER_TWO)
        card2.markMatched(window, PLAYER_TWO)
        secondPlayerList.append(card1)
        secondPlayerList.append(card2)

def changePlayer(window, card1, card2, currentPlayer):
    '''
    This function switches the turn from the first player to the second player and vice versa then flips the back.
    It returns which player's turn it is currently.

    Params:
    window(GraphWin): Window where the game takes place.
    currentPlayer(string): status of whose turn it is: player one or player two.
    card1(Card): the first picked card
    card2(Card): second picked card
    '''
    
    if currentPlayer == PLAYER_ONE:
        time.sleep(0.6)
        card1.flip(window)
        card2.flip(window)
        currentPlayer = PLAYER_TWO
        return currentPlayer
    
    elif currentPlayer == PLAYER_TWO:
        time.sleep(0.6)
        card1.flip(window)
        card2.flip(window)
        currentPlayer = PLAYER_ONE
        return currentPlayer

def declareWinner(firstPlayerList, secondPlayerList):
    '''
    This function compares the number of cards each player has matched and displays wchich player won the game on a separate window.

    Params:
    firstPlayerList(List): a list that contains the cards that the first player got matched.
    secondPlayerList(List): a list that contains the cards that the second player got matched.
    '''
    
    if len(firstPlayerList) > len(secondPlayerList):
        winner = 'PLAYER ONE WINS!'
    elif len(firstPlayerList) < len(secondPlayerList):
        winner = 'PLAYER TWO WINS!'
    else:
        winner = "IT'S A TIE!"
        
    winnerWin = GraphWin("How to play", 700, 300)
    winnerWin.setBackground('lightgreen')
    winnerText = Text(Point(350, 150), winner)
    winnerText.draw(winnerWin)
    
def playGame(window, gameBoard):
    '''
    This function allows the game to run in a loop until all cards are matched.
    It checks if the click is not outside a card, or not on a card which is already flipped.
    It returns the lists that contain the cards of the two players.

    Params:
    window(GraphWin): Window where the game takes place.
    gameBoard(Board): the main playing board containing the cards.
    '''
    # initialize lists for both players
    firstPlayerList = []
    secondPlayerList = []
    #initialize first player as player one
    currentPlayer = PLAYER_ONE
    
    while not gameBoard.allMatch():
        click1 = window.getMouse()
        # check if first click is a valid click
        while gameBoard.getCardAtPoint(click1) == None or gameBoard.getCardAtPoint(click1) in firstPlayerList or gameBoard.getCardAtPoint(click1) in secondPlayerList:
            click1 = window.getMouse()
            
        card1 = gameBoard.getCardAtPoint(click1)
        card1.flip(window)
        
        click2 = window.getMouse()
        # check if second click is a valid click
        while gameBoard.getCardAtPoint(click2) == None or gameBoard.getCardAtPoint(click2) in firstPlayerList or gameBoard.getCardAtPoint(click2) in secondPlayerList or gameBoard.getCardAtPoint(click2) == card1:
            click2 = window.getMouse()
            
        card2 = gameBoard.getCardAtPoint(click2)
        card2.flip(window)
        #check if cards match
        if card1.getSymbol() == card2.getSymbol():
            markCards(window, currentPlayer, card1, card2, firstPlayerList, secondPlayerList)
        else:
            currentPlayer = changePlayer(window, card1, card2, currentPlayer)
    return firstPlayerList, secondPlayerList


def main():
    giveInstructions()
    
    # Icons made by various authors, Available on http://game-icons.net
    images = ['icons/claw.gif', 'icons/dolphin.gif', 'icons/fish.gif',
          'icons/jellyfish.gif', 'icons/seahorse.gif', 'icons/seaweed.gif', 'icons/shell.gif',
          'icons/squid.gif', 'icons/stingray.gif', 'icons/tentacle.gif', 'icons/wave.gif',
          'icons/snail.gif']
    
    window = GraphWin("Memory Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('lightgreen')
    gameBoard = Board(NUM_ROWS, NUM_COLS, images)
    gameBoard.draw(window)
    
    firstPlayerList, secondPlayerList = playGame(window, gameBoard)
    window.close()
    time.sleep(0.4)
    declareWinner(firstPlayerList, secondPlayerList)
    

if __name__ == '__main__':
    main()
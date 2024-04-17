


class TicTacToe():
    
    def __init__(self):
        self.token1 = "X"
        self.token2 = "Y"
        gameOver = False
        boardLine = "{}   {}   |   {}   |   {}  "
        boardBarrier = "  — — — | — — — | — — —"
        spaces = {"a1":" ", "a2":" ", "a3":" ", "b1":" ", "b2":" ", "b3":" ", "c1":" ", "c2":" ", "c3":" "}
        winStates = [("a1","a2","a3"), ("b1","b2","b3"), ("c1","c2","c3"), ("a1","b1","c1"), ("a2","b2","c2"), ("a3","b3","c3"), ("a1","b2","c3"), ("a3","b2","c1")]

    
    def printBoard(self):
        print("    1       2       3")
        print(self.boardLine.format("a", self.spaces["a1"], self.spaces["a2"],self.spaces["a3"] ))
        print(self.boardBarrier)
        print(self.boardLine.format("b", self.spaces["b1"], self.spaces["b2"], self.spaces["b3"]))
        print(self.boardBarrier)
        print(self.boardLine.format("c", self.spaces["c1"], self.spaces["c2"], self.spaces["c3"]))

    
    def checkWin(self):
        for i in self.winStates:
            x = []
            for y in i:
                x.append(self.spaces[y])
            if x.count(self.token1) == 3:
                self.printBoard()
                print(self.token1 + " wins!")
                print("Good Game!")
                self.gameOver = True
            elif x.count(self.token2) == 3:
                self.printBoard()
                print(self.token2+ " wins!")
                print("Good Game!")
                self.gameOver = True
            else:
                continue

    
    def setup(self):
        choice1 = False
        choice2 = False
        
        while choice1 == False:
            isCustom1 = input("Welcome Player 1. The default token for Player1 is 'X'. Would you like to choose a new token? (Y/N): ")
            if isCustom1.capitalize() == "Y":
                customToken = input("Please enter a character for your token: ")
                self.token1 = customToken[0]
                print("The token for Player 1 is: " + self.token1)
                choice1 = True
            else:
                print("The token for Player 1 is: " + self.token1)
                choice1 = True
                
        while choice2 == False:
            isCustom2 = input("Welcome Player 2. The default token for Player2 is 'Y'. Would you like to choose a new token? (Y/N): ").format(self.token1)
            if isCustom2.capitalize() == "Y":
                customToken = input("Please enter a character for your token: ")
                self.token2 = customToken[0]
                choice2 = True
            else:
                choice2 = True

    
    def takeTurn(self, player):
        stamp = player
        finishTurn = False
        while finishTurn == False:
            self.printBoard()
            print(player +", your turn.")
            move = input("Please choose a square by typing the column and row (i.e. for top middle, type 'a2'): ")
            if move in self.spaces and self.spaces[move] == " ":
                self.spaces[move] = player
                finishTurn = True
            else:
                print("Invalid space. Please try again.")
                continue


    def runGame(self):
        self.setup()
        while self.gameOver == False:
            self.takeTurn(self.token1)
            self.checkWin()
            if self.gameOver == True:
                break
            self.takeTurn(self.token2)
            self.checkWin()


newgame = TicTacToe()
newgame.runGame()
#newgame.Setup()
#newgame.checkWin()
#newgame.TakeTurn(newgame.token1)
#newgame.PrintBoard()
#print(newgame.spaces[3])

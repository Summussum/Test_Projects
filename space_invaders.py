
def run_game():
    #setup starting conditions
    a1 = invader(32)
    a2 = invader(36)
    a3 = invader(40)
    gameboard.invader_list.append(a1)
    gameboard.invader_list.append(a2)
    gameboard.invader_list.append(a3)
    gameboard.player_board[defender.pos] = defender.token
    gameboard.printBoard()

    while True:
        gameboard.turn_count += 1
        gameboard.ballistics_move()
        
        defender.action(input("Choose your two actions, then press [enter]: "))
        gameboard.printBoard()
            
        #manage invaders
        [instance.move() for instance in gameboard.invader_list]
        [instance.kill() for instance in gameboard.invader_list]
        if gameboard.turn_count%(13-gameboard.level) == 0:
            gameboard.invader_list.append(invader())
        
        #win condition
        if gameboard.turn_count == 420:
            for i in range(len(gameboard.player_board)):
                if i%2 == 0:
                    gameboard.player_board[i] = defender.token
                    gameboard.gap[i] = " ! "
            gameboard.printBoard()
            print("Congratulations! You've held off the invasion until reinforcements could arive. Earth lives another day!")
            raise SystemExit
        if gameboard.turn_count%35 == 1:
            gameboard.level+=1
        

class Board():
    board = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    gap = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    player_board = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    player_board_def = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    kill_count = 0
    turn_count = 1
    invader_list = []
    level = 1

    def ballistics_move(self):
        for i in range(31, 40, 1):
            self.gap[i] = "   "
        for i in range(30, -1, -1):
            if self.gap[i] == " ! ":
                self.gap[i] = "   "
                self.gap[i+10] = " ! "
    
    def row_draw(self, *arg):
        printer = ""
        for i in range(len(arg)):
            printer += f"|{arg[i]}|\n"
        return printer

    def printBoard(self):
        row4=""
        row3=""
        row2=""
        row1=""
        gap4=""
        gap3=""
        gap2=""
        gap1=""
        playerspace =""
        
        for space in range(31, 41, 1):
            row4 += self.board[space]
        for space in range(21, 31, 1):
            row3 += self.board[space]
        for space in range(11, 21, 1):
            row2 += self.board[space]
        for space in range(1, 11, 1):
            row1 += self.board[space]
        
        for item in range(30, 40, 1):
            gap4 += self.gap[item]
        for item in range(20, 30, 1):
            gap3 += self.gap[item]
        for item in range(10, 20, 1):
            gap2 += self.gap[item]
        for item in range(0, 10, 1):
            gap1 += self.gap[item]

        for space in self.player_board:
            playerspace += space
        
        print ("\nActions:   [a]=left   [d]=right   [w]=fire(max 2 missiles)   [q]=quit game")
        print("Level:", self.level)
        print("Kill Count: " + str(self.kill_count) + "        Turn Count: " + str(self.turn_count))
        print(self.row_draw(row4,gap4,row3,gap3,row2,gap2,row1,gap1,playerspace))
        

class invader():
    pos = 40
    token = "p0q"

    def __init__(self, i =40):
        self.pos = i
        Board.board[self.pos] = self.token
        
    def move(self):
        Board.board[self.pos] = "   "
        self.pos -= 1
        Board.board[self.pos] = self.token
        if self.pos <= 0:
            print("Game over! The invasion has landed!")
            raise SystemExit

    def kill(self):
        strike_zone = []
        for space in range(len(gameboard.gap)):
            if gameboard.gap[space] == " ! ":
                strike_zone.append(space)
        if self.pos in strike_zone:
            gameboard.kill_count += 1
            gameboard.board[self.pos] = "   "
            gameboard.gap[self.pos] = "   "

            for i, element in enumerate(gameboard.invader_list):
                if gameboard.invader_list[i] == self:
                    gameboard.invader_list.pop(i)
            del self
    

class defender():

    def __init__(self):
        self.pos = 4
        self.token = "oAo"

    def action(self, action):
        #action = "w"
        gameboard.player_board[defender.pos] = "   "
        for i in range(0,2,1): 
            if i >= len(action):
                break
            if action[i] == "q":
                raise SystemExit
                break
            if action[i] == "d":
                defender.right()
            elif action[i] == "a":
                defender.left()
            elif action[i] == "w" and gameboard.gap.count(" ! ") < 2:
            #elif action[i] =="w":
                defender.fire()
        gameboard.player_board[defender.pos] = defender.token

    
    def right(self):
        if self.pos < 9:
            self.pos += 1
    
    def left(self):
        if self.pos > 0:
            self.pos -= 1

    def fire(self):
        Board.gap[self.pos] = " ! "
  

defender = defender()
gameboard = Board()
run_game()
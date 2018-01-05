from gameboard import GameBoard
import time
from highscores import HighScores
from inputtool import InputTool

class Game:

    def __init__(self):
        self.num_rows = 9
        self.num_cols = 9
        self.num_mines = 10

        self.screen = "1"
        self.screenMap = {
            "1": "main_menu_screen",
            "2": "play_game_screen",
            "3": "help_screen",
            "4": "settings_screen",
            "5": "high_scores_screen",
            "6": "exit",
            "7": "lose_screen",
            "8": "win_screen"
        }
        self.difficulty = "1"
        self.difficultyMap = {
            "1": "easy",
            "2": "medium",
            "3": "hard"
        }
        self.firstTurn = True
        self.start_time = time.time()
        self.mines_remaining = self.num_mines
        self.score = 0
        self.name = ""

    def header(self, text):
        print("=" * 100)
        print(text)
        print("-" * len(text))

    def mainMenu(self):
        self.header("Minesweeper")

        inputTool = InputTool({"2": "Play", "3": "Help", "4": "Settings", "5": "High Scores", "6": "Exit"})
        self.screen = inputTool.getInput()

        # set up and reset the game
        if (self.screen == "2"):
            self.firstTurn = True

            if (self.difficulty == "1"):
                self.num_rows = 9
                self.num_cols = 9
                self.num_mines = 10
                self.mines_remaining = 10
            elif (self.difficulty == "2"):
                self.num_rows = 12
                self.num_cols = 12
                self.num_mines = 24
                self.mines_remaining = 24
            elif (self.difficulty == "3"):
                self.num_rows = 16
                self.num_cols = 16
                self.num_mines = 40
                self.mines_remaining = 40

            self.game_board = GameBoard(self.num_rows, self.num_cols, self.num_mines)
            self.game_board.createBoard()
            self.game_board.placeMines()
            self.game_board.fillBoard()

            self.start_time = time.time()

    def playGameScreen(self):
        self.header("Play")

        current_time = time.time()
        self.score = int(current_time - self.start_time)

        print("Score - " + str(self.score))
        print("Mines Remaining - " + str(self.mines_remaining))

        # display of the back end 2D array of the game board from the GameBoard class
        print(self.game_board)

        inputTool = InputTool({"1": "Flip", "2": "Flag/Mark"})
        action = inputTool.getInput()
        
        # validate input for column and row 
        while True:
            try:
                icol = int(input("[ENTER] || Column | - ")) - 1
            except:
                continue

            if (0 <= icol < self.num_cols):
                break

        while True:
            try:
                irow = int(input("[ENTER] || Row | - ")) - 1
            except:
                continue

            if (0 <= irow < self.num_rows):
                break
        
        # guarantee that the user guesses an empty space on the first guess
        if (self.firstTurn):
            self.game_board.guaranteeEmptyCell(irow, icol)

        # flipping
        if (action == "1" and not (self.game_board.board[irow][icol].isFlagged or self.game_board.board[irow][icol].isMarked)):
            # flip the tile the user guessed
            self.game_board.board[irow][icol].flip()

            # if the user guesses an empty tile...
            if (self.game_board.board[irow][icol].isEmpty()):
                self.game_board.clearEmptyCells(irow, icol)

            # if the users loses...
            if (self.game_board.hasLost(irow, icol)):
                self.screen = "7"

            # if the user wins...
            if (self.game_board.hasWon()):
                current_time = time.time()
                self.score = int(current_time - self.start_time)
                self.screen = "8"

            self.firstTurn = False
        # flagging
        elif (action == "2" and self.firstTurn == False and self.game_board.board[irow][icol].isFlipped == False):
            self.game_board.board[irow][icol].clicks += 1
        
            if (self.game_board.board[irow][icol].clicks % 3 == 1):
                self.game_board.board[irow][icol].isFlagged = True
                self.mines_remaining -= 1
            elif (self.game_board.board[irow][icol].clicks % 3 == 2):
                self.game_board.board[irow][icol].isMarked = True
                self.game_board.board[irow][icol].isFlagged = False
                self.mines_remaining += 1
            else:
                self.game_board.board[irow][icol].isMarked = False

    def helpScreen(self):
        self.header("Help")

        instructions = [
            "* To win, open all the cells which do not contain a mine.",
            "* Try to win as quickly as possible.",
            "* If you guess a cell with a mine, you lose.",
            "* Every non-mine cell will tell you the total number of mines in the eight neighboring cells.",
            "* To open a square, point at the square and click on it.",
            "* To mark a square you think is a mine with a flag, point and right-click.",
            "* Right-click twice to mark a cell that you are unsure about.",
            "* The first square you open is never a mine.",
            "* The upper left corner contains the number of mines left to find.",
            "* The upper right corner contains a time counter.",
            "* Good luck sweeping!"
        ]

        for i in instructions:
            print(i)

        inputTool = InputTool({"1": "Main Menu", "6": "Exit"})
        self.screen = inputTool.getInput()

    def settingsScreen(self):
        self.header("Settings")

        inputTool = InputTool({"1": "Easy", "2": "Medium", "3": "Hard"})
        self.difficulty = inputTool.getInput()

        inputTool = InputTool({"1": "Main Menu", "6": "Exit"})
        self.screen = inputTool.getInput()

    def highScoreScreen(self):
        self.header("High Scores")

        hs = HighScores().outputData()

        for i, s in enumerate(hs):
            name, score = s
            print(str(i + 1) + ") " + name +  ("." * (25 - len(name))) + str(score)) 

        inputTool = InputTool({"1": "Main Menu", "6": "Exit"})
        self.screen = inputTool.getInput()

    def loseScreen(self):
        self.header("Game Over!")  
        self.game_board.revealMines()

        print(self.game_board)

        inputTool = InputTool({"1": "Main Menu", "6": "Exit"})
        self.screen = inputTool.getInput()
    
    def winScreen(self):
        self.header("You Win!")
        print("Score: " + str(self.score))
        print(self.game_board)

        self.name = input("Enter your name: ")

        # add score to JSON file
        HighScores().addData(self.name, self.score)

        inputTool = InputTool({"1": "Main Menu", "6": "Exit"})
        self.screen = inputTool.getInput()

    def gameLoop(self):
        """
        - menu system and game loop
        """
        while self.screenMap[self.screen] != "exit":
            # main menu screen
            if (self.screenMap[self.screen] == "main_menu_screen"):
                self.mainMenu()
            # help screen
            elif (self.screenMap[self.screen] == "help_screen"):
                self.helpScreen()
            # settings screen
            elif (self.screenMap[self.screen] == "settings_screen"):
                self.settingsScreen()
            # high scores screen
            elif (self.screenMap[self.screen] == "high_scores_screen"):
                self.highScoreScreen()
            # play game screen
            elif (self.screenMap[self.screen] == "play_game_screen"):
                self.playGameScreen()
            # lose screen
            elif (self.screenMap[self.screen] == "lose_screen"):
                self.loseScreen()
            # win screen
            elif (self.screenMap[self.screen] == "win_screen"):
                self.winScreen()

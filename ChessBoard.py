from PawnPiece import PawnPiece
from BishopPiece import BishopPiece
from RookPiece import RookPiece
from KnightPiece import KnightPiece
from KingPiece import KingPiece
from QueenPiece import QueenPiece

class ChessBoard:
    """
    Represents the game board.
    """

    def __init__(self):
        self.gameGrid = [[None] * 8 for _ in range(8)]
        self.gameOver = False
        self.winner = None

        # Place white pieces
        self.gameGrid[0][0] = RookPiece("White")
        self.gameGrid[0][1] = KnightPiece("White")
        self.gameGrid[0][2] = BishopPiece("White")
        self.gameGrid[0][3] = QueenPiece("White")
        self.gameGrid[0][4] = KingPiece("White")
        self.gameGrid[0][5] = BishopPiece("White")
        self.gameGrid[0][6] = KnightPiece("White")
        self.gameGrid[0][7] = RookPiece("White")
        for i in range(8):
            self.gameGrid[1][i] = PawnPiece("White")
        #

        # Place black pieces
        self.gameGrid[7][0] = RookPiece("Black")
        self.gameGrid[7][1] = KnightPiece("Black")
        self.gameGrid[7][2] = BishopPiece("Black")
        self.gameGrid[7][3] = QueenPiece("Black")
        self.gameGrid[7][4] = KingPiece("Black")
        self.gameGrid[7][5] = BishopPiece("Black")
        self.gameGrid[7][6] = KnightPiece("Black")
        self.gameGrid[7][7] = RookPiece("Black")
        for i in range(8):
            self.gameGrid[6][i] = PawnPiece("Black")
        #

        self.printBoard()
    #

    def printBoard(self):
        for letter in ["","A","B","C","D","E","F","G","H"]:
            print(letter, end="\t")
        #
        print(f"\n=====================================================================")
        for row in range(8):
            print(f"{row + 1}   |", end="\t")
            for col in self.gameGrid[row]:
                if col == None:
                    print(col, end="\t")
                else:
                    print(col.pieceType, end="\t")
            #
            print()
        #
        print()
    #

    def movePiece(self,locFrom,locTo):
        row1 = int(locFrom[1]) - 1
        col1 = ord(locFrom[0]) - ord('A')
        row2 = int(locTo[1]) - 1
        col2 = ord(locTo[0]) - ord('A')
        print(row1, col1, row2, col2)

        # Ensure a piece exists at the initial location
        piece = self.gameGrid[row1][col1]
        if piece is None:
            print("No piece at starting location.")
            return False
        #

        secPt = (row2, col2)
        print(secPt)
        
        # Check for valid path
        validPaths = sorted(self.gameGrid[row1][col1].getValidPaths((row1,col1),self.gameGrid))
        print(validPaths)
        if (row2, col2) not in validPaths:
            print("Invalid move.")
            return False

        # Check for winning condition
        if isinstance(self.gameGrid[row2][col2], KingPiece): 
            self.gameOver = True
            print(f"Game over! Adriean won!\n")
        #

        temp = self.gameGrid[int(row1)][int(col1)]
        self.gameGrid[row1][col1] = None
        if isinstance(temp, PawnPiece):
            temp.hasMoved = True
        self.gameGrid[row2][col2] = temp

    #

    def play(self):
        while(True):
            spot1 = input("Piece to move (or Q to quit): ")

            if spot1 == "Q":
                break
            #

            spot2 = input("Move to: ")
            print()
            board.movePiece(spot1,spot2)

            self.printBoard()

            if board.gameOver == True:
                break
            #
        #
    #
#

# ===== TEST SECTION =====

if __name__ == "__main__":

    board = ChessBoard()
    board.play()
    
    
    
#
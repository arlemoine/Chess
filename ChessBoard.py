from PawnPiece import PawnPiece
from BishopPiece import BishopPiece
from RookPiece import RookPiece

class ChessBoard:
    """
    Represents the game board.
    """

    def __init__(self):
        self.gameGrid = [[None] * 8 for _ in range(8)]
        self.gameOver = False
        self.winner = None

        # # Place Rooks
        # self.gameGrid[0][0] = self.gameGrid[0][7] = self.gameGrid[7][0] = self.gameGrid[7][7] = "R"

        # # Place Knights
        # self.gameGrid[0][1] = self.gameGrid[0][6] = self.gameGrid[7][1] = self.gameGrid[7][6] = "H"

        # # Place Bishops
        # self.gameGrid[0][2] = self.gameGrid[0][5] = self.gameGrid[7][2] = self.gameGrid[7][5] = "B"

        # # Place Queen
        # self.gameGrid[0][3] = self.gameGrid[7][3] = "Q"

        # # Place King
        # self.gameGrid[0][4] = self.gameGrid[7][4] = "K"

        # # Place Pawns
        # self.gameGrid[1] = ["P"] * 8
        # self.gameGrid[6] = ["P"] * 8

        # TEST PIECES
        self.gameGrid[7][7] = RookPiece("White")
        self.gameGrid[6][6] = RookPiece("White")
        self.gameGrid[3][7] = RookPiece("White")

        self.printBoard()
    #

    def printBoard(self):
        for letter in ["","A","B","C","D","E","F","G","H"]:
            print(letter, end="\t")
        #
        print()
        for row in range(8):
            print(row + 1, end="\t")
            for col in self.gameGrid[row]:
                if col == None:
                    print(col, end="\t")
                else:
                    print(col.pieceType, end="\t")
            #
            print()
        #
    #

    def movePiece(self,locFrom,locTo):
        row1 = int(locFrom[1]) - 1
        col1 = ord(locFrom[0]) - ord('A')
        row2 = int(locTo[1]) - 1
        col2 = ord(locTo[0]) - ord('A')

        # Check for winning condition
        if self.gameGrid[row2][col2] == "K":
            self.gameOver = True
            print(f"Game over! Adriean won!\n")
        #

        temp = self.gameGrid[int(row1)][int(col1)]
        self.gameGrid[row1][col1] = None
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
    # board.play()
    board.gameGrid[7][7].getValidPaths((7,7),board.gameGrid)
    
    
#
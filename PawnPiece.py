from ChessPiece import ChessPiece

class PawnPiece(ChessPiece):
    """
    Represents the pawn piece.
    """

    def __init__(self, color):
        super().__init__(color)
        self.pieceType = f"({color[0]})P"
        self.hasMoved = False

        # Determine direction of travel vertically, based on team
        if color == "Black":
            self.linearAdvancement = -1
        else:
            self.linearAdvancement = 1
        #
    #

    def getValidPaths(self, location, gameGrid):
        validPaths = []
        row = location[0]
        col = location[1]

        # Grant an extra jump if the pawn has not yet moved in the game
        if self.hasMoved == False:
            allowedJumps = 2
        else:
            allowedJumps = 1
        #

        # Check for diagonal attacks
        tempRow = row + self.linearAdvancement
        # Diagonal left
        tempCol = col - 1
        print(f"tempCol = {tempCol}")
        if tempCol > -1 and tempCol < 8:
            if gameGrid[tempRow][tempCol] != None:
                if gameGrid[tempRow][tempCol].color != self.color:
                    validPaths.append((tempRow, tempCol))
                #
            #
        #
        # Diagonal right
        tempCol = tempCol + 2
        print(f"tempCol = {tempCol}")
        if tempCol > -1 and tempCol < 8:
            if gameGrid[tempRow][tempCol] != None:
                if gameGrid[tempRow][tempCol].color != self.color:             
                    validPaths.append((tempRow, tempCol))
                #
            #
        #

        # Check for vertical movement
        if gameGrid[tempRow][col] == None:
            validPaths.append((tempRow, col))
        # Checks to see if it is the first turn of the pawn for an extra jump
            if self.hasMoved == False and gameGrid[tempRow + self.linearAdvancement][col] == None:
                validPaths.append((tempRow + self.linearAdvancement, col))
            #
        #

        # print(validPaths) # FOR TESTING PURPOSES
    #
#

# ===== TEST =====

if __name__ == "__main__":
    print()
#
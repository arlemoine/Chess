from ChessPiece import ChessPiece

class KnightPiece(ChessPiece):
    """
    Represents the knight piece.
    """

    def __init__(self, color):
        super().__init__(color)
        self.pieceType = f"({color[0]})H"
    #

    def getValidPaths(self, location, gameGrid):
        validPaths = []
        row = location[0]
        col = location[1]

        # Check upward-dominant positions
        tempRow = row - 2
        if tempRow > -1:
            tempCol = col - 1
            if tempCol > -1:
                if gameGrid[tempRow][tempCol] == None:
                    validPaths.append((tempRow, tempCol))
                #
                elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                    validPaths.append((tempRow, tempCol))
                #
            #
            tempCol = tempCol + 2
            if tempCol < 8:
                if gameGrid[tempRow][tempCol] == None:
                    validPaths.append((tempRow, tempCol))
                #
                elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                    validPaths.append((tempRow, tempCol))
                #
            #
        #

        # Check downward-dominant positions
        tempRow = row + 2
        if tempRow < 8:
            tempCol = col - 1
            if tempCol > -1:
                if gameGrid[tempRow][tempCol] == None:
                    validPaths.append((tempRow, tempCol))
                #
                elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                    validPaths.append((tempRow, tempCol))
                #
            #
            tempCol = tempCol + 2
            if tempCol < 8:
                if gameGrid[tempRow][tempCol] == None:
                    validPaths.append((tempRow, tempCol))
                #
                elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                    validPaths.append((tempRow, tempCol))
                #
            #
        #

        # Check leftward-dominant positions
        tempCol = col - 2
        if tempCol > -1:
            tempRow = row - 1
            if tempRow > -1:
                if gameGrid[tempRow][tempCol] == None:
                    validPaths.append((tempRow, tempCol))
                #
                elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                    validPaths.append((tempRow, tempCol))
                #
            #
            tempRow = tempRow + 2
            if tempRow < 8:
                if gameGrid[tempRow][tempCol] == None:
                    validPaths.append((tempRow, tempCol))
                #
                elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                    validPaths.append((tempRow, tempCol))
                #
            #
        #

        # Check rightward-dominant positions
        tempCol = col + 2
        if tempCol < 8:
            tempRow = row - 1
            if tempRow > -1:
                if gameGrid[tempRow][tempCol] == None:
                    validPaths.append((tempRow, tempCol))
                #
                elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                    validPaths.append((tempRow, tempCol))
                #
            #
            tempRow = tempRow + 2
            if tempRow < 8:
                if gameGrid[tempRow][tempCol] == None:
                    validPaths.append((tempRow, tempCol))
                #
                elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                    validPaths.append((tempRow, tempCol))
                #
            #
        #

        # print(validPaths) # FOR TESTING
    #
#

# ===== TEST =====

if __name__ == "__main__":
    print()
#
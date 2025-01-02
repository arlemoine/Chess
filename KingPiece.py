from ChessPiece import ChessPiece

class KingPiece(ChessPiece):
    """
    Represents the king piece.
    """
    def __init__(self, color):
        super().__init__(color)
        self.pieceType = f"({color[0]})K"
    #

    def getValidPaths(self, location, gameGrid):
        validPaths = []
        row = location[0]
        col = location[1]
        tempRow = row
        tempCol = col

        tempRow = tempRow - 1
        if tempRow > -1:
            if gameGrid[tempRow][tempCol] == None:
                validPaths.append((tempRow, tempCol))
            elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                validPaths.append((tempRow, tempCol))
            #
        #

        tempCol = tempCol - 1
        if tempCol > -1:
            if gameGrid[tempRow][tempCol] == None:
                validPaths.append((tempRow, tempCol))
            elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                validPaths.append((tempRow, tempCol))
            #
        #

        tempRow = tempRow + 1
        if gameGrid[tempRow][tempCol] == None:
            validPaths.append((tempRow, tempCol))
        elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
            validPaths.append((tempRow, tempCol))
        #

        tempRow = tempRow + 1
        if tempRow < 8:
            if gameGrid[tempRow][tempCol] == None:
                validPaths.append((tempRow, tempCol))
            elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                validPaths.append((tempRow, tempCol))
            #
        #

        tempCol = tempCol + 1
        if gameGrid[tempRow][tempCol] == None:
            validPaths.append((tempRow, tempCol))
        elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
            validPaths.append((tempRow, tempCol))
        #

        tempCol = tempCol + 1
        if tempCol < 8:
            if gameGrid[tempRow][tempCol] == None:
                validPaths.append((tempRow, tempCol))
            elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                validPaths.append((tempRow, tempCol))
            #
        #

        tempRow = tempRow - 1
        if gameGrid[tempRow][tempCol] == None:
            validPaths.append((tempRow, tempCol))
        elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
            validPaths.append((tempRow, tempCol))
        #

        tempRow = tempRow - 1
        if gameGrid[tempRow][tempCol] == None:
            validPaths.append((tempRow, tempCol))
        elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
            validPaths.append((tempRow, tempCol))
        #

        # print(validPaths) # FOR TESTING
    #
#

# ===== TEST =====

if __name__ == "__main__":
    print()
#
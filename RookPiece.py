from ChessPiece import ChessPiece

class RookPiece(ChessPiece):
    """
    Represents the rook piece.
    """

    def __init__(self, color):
        super().__init__(color)
        self.pieceType = f"({color[0]})R"
    #

    def getValidPaths(self, location, gameGrid):
        validPaths = []
        row = location[0]
        col = location[1]

        # Move up and left diagonally
        tempRow = row
        tempCol = col
        while tempRow > 0 and tempCol > 0:
            tempRow = tempRow - 1
            tempCol = tempCol - 1
            if gameGrid[tempRow][tempCol] == None:
                validPaths.append((tempRow, tempCol))
            elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                validPaths.append((tempRow, tempCol))
                break
            else:
                break
            #
        #
        # Move up and right diagonally
        tempRow = row
        tempCol = col
        while tempRow > 0 and tempCol < 7:
            tempRow = tempRow - 1
            tempCol = tempCol + 1
            if gameGrid[tempRow][tempCol] == None:
                validPaths.append((tempRow, tempCol))
            elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                validPaths.append((tempRow, tempCol))
                break
            else:
                break
            #
        #
        # Move down and left diagonally
        tempRow = row
        tempCol = col
        while tempRow < 7 and tempCol > 0:
            tempRow = tempRow + 1
            tempCol = tempCol - 1
            if gameGrid[tempRow][tempCol] == None:
                validPaths.append((tempRow, tempCol))
            elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                validPaths.append((tempRow, tempCol))
                break
            else:
                break
            #
        #
        # Move down and right diagonally
        tempRow = row
        tempCol = col
        while tempRow < 7 and tempCol < 7:
            tempRow = tempRow + 1
            tempCol = tempCol + 1
            if gameGrid[tempRow][tempCol] == None:
                validPaths.append((tempRow, tempCol))
            elif gameGrid[tempRow][tempCol].color != gameGrid[row][col].color:
                validPaths.append((tempRow, tempCol))
                break
            else:
                break
            #
        #

        # print(validPaths) # FOR TESTING
    #
#

# ===== TEST =====

if __name__ == "__main__":
    print()
#
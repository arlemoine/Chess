from ChessPiece import ChessPiece

class BishopPiece(ChessPiece):
    """
    Represents the bishop piece.
    """

    def __init__(self, color):
        super().__init__(color)
        self.pieceType = f"({color[0]})B"
    #

    def getValidPaths(self, location, gameGrid):
        validPaths = []
        row = location[0]
        col = location[1]
        tempRow = row
        tempCol = col

        # Move left
        while tempCol > 0:
            tempCol = tempCol - 1
            if gameGrid[row][tempCol] == None:
                validPaths.append((row, tempCol))
            elif gameGrid[row][tempCol].color != gameGrid[row][col].color:
                validPaths.append((row, tempCol))
                break
            else:
                break
            #
        #

        # Move right
        tempCol = col
        while tempCol < 7:
            tempCol = tempCol + 1
            if gameGrid[row][tempCol] == None:
                validPaths.append((row, tempCol))
            elif gameGrid[row][tempCol].color != gameGrid[row][col].color:
                validPaths.append((row, tempCol))
                break
            else:
                break
            #
        #

        # Move up
        while tempRow > 0:
            tempRow = tempRow - 1
            if gameGrid[tempRow][col] == None:
                validPaths.append((tempRow, col))
            elif gameGrid[tempRow][col].color != gameGrid[row][col].color:
                validPaths.append((tempRow, col))
                break
            else:
                break
            #
        #
        
        # Move down
        tempRow = row
        while tempRow < 7:
            tempRow = tempRow + 1
            if gameGrid[tempRow][col] == None:
                validPaths.append((tempRow, col))
            elif gameGrid[tempRow][col].color != gameGrid[row][col].color:
                validPaths.append((tempRow, col))
                break
            else:
                break
            #
        #

        return validPaths
        # print(validPaths) # FOR TESTING
    #
#

# ===== TEST =====

if __name__ == "__main__":
    print()
#
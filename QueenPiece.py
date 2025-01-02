from ChessPiece import ChessPiece

class QueenPiece(ChessPiece):
    """
    Represents the queen piece.
    """

    def __init__(self, color):
        super().__init__(color)
        self.pieceType = f"({color[0]})Q"
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

        print(sorted(validPaths))
    #
#

# ===== TEST =====

if __name__ == "__main__":
    print()
#
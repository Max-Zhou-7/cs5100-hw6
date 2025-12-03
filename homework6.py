import time
import numpy as np
from gridgame import *

##############################################################################################################################

# You can visualize what your code is doing by setting the GUI argument in the following line to true.
# The render_delay_sec argument allows you to slow down the animation, to be able to see each step more clearly.

# For your final submission, please set the GUI option to False.

# The gs argument controls the grid size. You should experiment with various sizes to ensure your code generalizes.
# Please do not modify or remove lines 18 and 19.

##############################################################################################################################

game = ShapePlacementGrid(GUI=True, render_delay_sec=0.5, gs=6, num_colored_boxes=5)
shapePos, currentShapeIndex, currentColorIndex, grid, placedShapes, done = game.execute('export')
np.savetxt('initial_grid.txt', grid, fmt="%d")

##############################################################################################################################

# Initialization

# shapePos is the current position of the brush.

# currentShapeIndex is the index of the current brush type being placed (order specified in gridgame.py, and assignment instructions).

# currentColorIndex is the index of the current color being placed (order specified in gridgame.py, and assignment instructions).

# grid represents the current state of the board. 
    
    # -1 indicates an empty cell
    # 0 indicates a cell colored in the first color (indigo by default)
    # 1 indicates a cell colored in the second color (taupe by default)
    # 2 indicates a cell colored in the third color (veridian by default)
    # 3 indicates a cell colored in the fourth color (peach by default)

# placedShapes is a list of shapes that have currently been placed on the board.
    
    # Each shape is represented as a list containing three elements: a) the brush type (number between 0-8), 
    # b) the location of the shape (coordinates of top-left cell of the shape) and c) color of the shape (number between 0-3)

    # For instance [0, (0,0), 2] represents a shape spanning a single cell in the color 2=veridian, placed at the top left cell in the grid.

# done is a Boolean that represents whether coloring constraints are satisfied. Updated by the gridgames.py file.

##############################################################################################################################

shapePos, currentShapeIndex, currentColorIndex, grid, placedShapes, done = game.execute('export')

print(shapePos, currentShapeIndex, currentColorIndex, grid, placedShapes, done)


####################################################
# Timing your code's execution for the leaderboard.
####################################################

start = time.time()  # <- do not modify this.



##########################################
# Write all your code in the area below. 
##########################################



'''

YOUR CODE HERE


'''
def place_shape(currentShapeIndex, currentColorIndex, grid, shapePos):
    arr = game.shapes[currentShapeIndex]
    for i, row in enumerate(arr):
        for j, cell in enumerate(row):
            if cell:
                grid[shapePos[1]+i][shapePos[0]+j]= currentColorIndex
    return grid

def find_first_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == -1:
                return i,j
    return None
            
def remove_shape(currentShapeIndex, grid, shapePos):
    arr = game.shapes[currentShapeIndex]
    for i, row in enumerate(arr):
        for j, cell in enumerate(row):
            if cell: 
                grid[shapePos[1]+i][shapePos[0]+j] = -1
    return grid
    
def solve(grid, shapes, placedShapes):
    empty = find_first_empty(grid)
    if empty == None:
        return game.checkGrid(grid)
    i,j = empty
    for shapeId in range(len(shapes)):
        if game.canPlace(grid, shapes[shapeId],[j,i] ):
            colorId = game.getAvailableColor(grid, j, i)
            if colorId is not None:
                place_shape(shapeId, colorId, grid, [j,i])
                placedShapes.append((shapeId, [j,i], colorId))
     
            
                if solve(grid, shapes, placedShapes):
                    return True
                
                remove_shape(shapeId, grid, [j,i])
                placedShapes.pop()

    return False



result = solve(game.grid, game.shapes, game.placedShapes)
# print(result)
shapePos, currentShapeIndex, currentColorIndex, grid, placedShapes, done = game.execute('export')
done = game.checkGrid(grid)
print(shapePos, currentShapeIndex, currentColorIndex, grid, placedShapes, done)

########################################

# Do not modify any of the code below. 

########################################

end=time.time()

np.savetxt('grid.txt', grid, fmt="%d")
with open("shapes.txt", "w") as outfile:
    outfile.write(str(placedShapes))
with open("time.txt", "w") as outfile:
    outfile.write(str(end-start))

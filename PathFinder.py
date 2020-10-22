import numpy as np 
from moveSequence import posCheck

maxrow = 5 
maxcol = 6 

maze = np.zeros([maxrow,maxcol])


startPos = [2,0]
xs,ys = startPos 
goalPos = [2,3]
xg,yg = goalPos


def Heuristics(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2

for i  in range(len(maze)):
    for j in range(len(maze[i])):
        maze[i][j] = Heuristics(i,j,xg,yg)

DeadState = -1000
prevStateList = []
Goal = False  
 
obstacles = [[ 1 , 1 ],[ 1 , 2 ],[ 2 , 2 ],[ 3 , 1 ],[ 2 , 4 ],[ 3 , 4 ]]
 
for obstacle in obstacles:
    x,y = obstacle
    maze[x][y] = np.Infinity


print("Our Maze: ")
print(maze)


currentXPosition = xs 
currentYPosition = ys 
totalCost = 0 
pathList = []
counter = 0 
previousMove = ()

while Goal==False:
    bestmove , action = posCheck( currentXPosition , currentYPosition , maxrow , maxcol , maze , totalCost, previousMove )
    # next course of action
    if action == -1: 
        print("We can never reach as there is no path to goal. ")
        Goal = True
    else :
        if bestmove == previousMove : 
            
            maze[currentXPosition][currentYPosition] = np.Infinity
            currentXPosition , currentYPosition = pathList.pop()
            
            if pathList == []:
                previousMove = ()
            else:
                previousMove = pathList[-1]    

            #subtract the path cost (as we return to the previous state)
            if ( action==0 or action==1 ) :
                totalCost -= 2
            else:
                totalCost -= 1
        
        elif bestmove == (xg,yg):
            # We reached our goal , stop the search instantly
            pathList.append((currentXPosition,currentYPosition))
            pathList.append(bestmove)
            print("Best Path to take would be: ")
            print(pathList)
            Goal = True
            
        else:         
            pathList.append((currentXPosition , currentYPosition))
            previousMove = pathList[-1]
            
            currentXPosition , currentYPosition = bestmove           
            if ( action==0 or action==1 ) :
                totalCost += 2
            else:
                totalCost += 1        
        









 
    
    
    

import numpy as np 

def checkMoves(outOfBoundsList, pastCost ):
    counter = 0
    score = [ np.Infinity , np.Infinity , np.Infinity , np.Infinity ]
    for outOfBounds in outOfBoundsList:
        if outOfBounds == False and counter<=1:
           score[counter] = 2 + pastCost
        if outOfBounds == False and counter>1:
           score[counter] = 1 + pastCost
        counter = counter + 1        
    return score        

def isDeadState(scores , moves , HeuristicMatrix ):  
    
    counter = 0 
    for score  in scores :
        x , y = moves[ counter ]
        if score != np.Infinity and HeuristicMatrix[x][y] != np.Infinity :
           scores[counter] = score + HeuristicMatrix[x][y]               
        if score != np.Infinity and HeuristicMatrix[x][y] == np.Infinity :
           scores[counter] = np.Infinity
        counter = counter + 1        
    return scores


def posCheck(i, j , row , column , HeuristicMatrix , pastCost , previousMove ):
    isOutOfBounds = [False,False,False,False]
    positionScore = [0,0,0,0]
    moves = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    if( i-1 < 0 ) :
            isOutOfBounds[0] = True
    if( i+1 > row-1 ) :
            isOutOfBounds[1] = True
    if( j-1 < 0 ):
            isOutOfBounds[2] = True
    if( j+1 > column-1 ) :
            isOutOfBounds[3] = True
    scores = checkMoves( isOutOfBounds , pastCost  )  
    scores = isDeadState(scores , moves , HeuristicMatrix )
    
          
    return bestmove(scores, moves , previousMove) 

def bestmove(scores, moves, previousMove): 
    if previousMove != () :
        count = 0
        minimumScore = np.Infinity
        minimumIndex = -1
        previousMoveIndex = moves.index(previousMove)
        minIndex = moves.index(previousMove)
        for score in scores:
            if count != previousMoveIndex:
               if score < minimumScore:
                   minimumScore = score
                   minimumIndex = count
            count = count + 1
        if minimumScore == np.Infinity :
            return previousMove , previousMoveIndex
        else:    
            return moves[minimumIndex] , minimumIndex
    
    else:        
        minimumScore = min(scores)
        if minimumScore == np.Infinity:
            return (),-1        
        else:
            minIndex = scores.index(minimumScore)
            return moves[minIndex],minIndex  



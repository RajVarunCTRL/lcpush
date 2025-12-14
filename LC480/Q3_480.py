def minMoves(balance):
    if sum(balance)<0:
        return -1
    n = len(balance)
    posInd = []
    idx= -1
    for i in range(n):
       if balance[i]<0:
            idx = i 
            break
    
    if idx == -1: return 0
        
    temp = abs(balance[idx])
    
    for i in range(n):
        if balance[i]>0:
            dis = abs(idx-i)
            # Min func
            if dis<=n - dis:
                shortDis = dis
            else:
                shortDis = n-dis
            posInd.append((shortDis, balance[i]))
    
    moves = 0
    posInd.sort(key=lambda x: x[0])
    
    for dis, val in posInd:
        #  Min func
        
        if temp <= val:
            t = temp
        else:
            t = val
            
        moves += t*dis
        temp -= t
        
        if temp == 0: break
    return moves
            
# tcs
balance = [[5,1,-4],[1,2,-5,2],[-3,2]]
for i in range(len(balance)):
    print(minMoves(balance[i]))
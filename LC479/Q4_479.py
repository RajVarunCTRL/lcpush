def maxSubgraphScore(n, edges, good):
    
    map_tree = [[] for _ in range(n)]
    for u,v in edges:
        map_tree[u].append(v)
        map_tree[v].append(u)
    scoresub = [0]*n
    final = [0]*n
    
    def getval(node):
        return 1 if good[node]==1 else -1  
    
    def dfs_bu(curr,parent):
        tot = getval(curr)
        for temp in map_tree[curr]:
            if temp!=parent:
                dfs_bu(temp,curr)
                
                bval = scoresub[temp]
                if bval>0:
                    tot += bval
        scoresub[curr] = tot
    def dfs_td(curr,parent,upval):
        currtot = scoresub[curr]
        if upval>0:
            currtot += upval
        final[curr] = currtot
        
        for temp in map_tree[curr]:
            if temp!=parent:
                temp1 = scoresub[temp]
                if temp1<0:
                    temp1 = 0
                passingval = currtot - temp1
                dfs_td(temp,curr,passingval)
                
    dfs_bu(0,-1)
    dfs_td(0,-1,0)
    
    return final

# O1

# n = 3
# edges = [[0,1],[1,2]]
# good = [1,0,1]

# O2
n = 5
edges = [[1,0],[1,2],[1,3],[3,4]]
good = [0,1,0,1,1]
print(maxSubgraphScore(n,edges,good))
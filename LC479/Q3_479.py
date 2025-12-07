import bisect
def totalScore(hp, damage,requirement):
    n = len(damage)
    tot_score = 0
    
    pref_damage = [0]*(n+1)
    
    for i in range(n):
        pref_damage[i+1] = pref_damage[i] + damage[i]
    
    for i in range(n):
        tar = pref_damage[i+1] - hp + requirement[i]
        idx = bisect.bisect_left(pref_damage, tar, 0, i+1)
        
        if idx<=i:
            cnt = (i-idx+1)
            tot_score += cnt 
    return tot_score

hp = [11,2]
damage = [[3,6,7],[10000,1],[1,1]]
requirement = [[4,2,5],[1,1]]

print(totalScore(hp[1],damage[1],requirement[1]))

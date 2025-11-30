import bisect

def minimumDistance(nums):
    
    def revnum(v):
        s = 0
        while v > 0:
            s = s * 10 + (v % 10)
            v //= 10
        return s
    
    posi = {}
    for i,val in enumerate(nums):
        if val not in posi:
            posi[val] = []
        posi[val].append(i)
    best = 10**18
    
    for i,val in enumerate(nums):
        rev = revnum(val)
        if rev in posi:
            l = posi[rev]
            pos = bisect.bisect_right(l,i)
            if pos < len(l):
                gap = l[pos] - i
                if gap < best:
                    best = gap
    return best if best != 10**18 else -1

nums = [[12,21,45,33,54],[120,21],[21,120],[9,9]]
for arr_num in nums:
    print(minimumDistance(arr_num))
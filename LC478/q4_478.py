# Redacted never to be completed again. RIP for the TLE

def minOperationsQueries(nums, k, queries):
    
    mod = [v % k for v in nums]

    pre = [{}]
    curr = {}

    pre[0] = curr.copy()
    for val in mod:
        curr[val] = curr.get(val, 0) + 1
        pre.append(curr.copy())

    res = []

    for left, right in queries:

        length = right - left + 1
        key = mod[left]
        cnt = pre[right+1].get(key, 0) - pre[left].get(key, 0)

        if cnt != length:
            res.append(-1)
            continue

        arr = nums[left:right+1]
        arr.sort()
        tar = arr[length // 2]

        moves = 0
        for x in arr:
            moves += abs(x - tar) // k

        res.append(moves)

    return res

# nums = [1,4,7]
# k = 3
# queries = [[0,1],[0,2]]

nums = [1,2,4]
k = 2
queries = [[0,2],[0,0],[1,2]]

print(minOperationsQueries(nums,k,queries))
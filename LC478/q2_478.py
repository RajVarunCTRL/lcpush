def maxSubstrings(s):
    used = set()
    count = 0
    
    for ch in s:
        if ch not in used:
            used.add(ch)
            count += 1
    
    return count

    
s = ["abab","abcd","aaaa"]
for id in s:
    
    print(maxSubstrings(id))
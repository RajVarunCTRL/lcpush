def countGoodSubarrays(nums):
    n = len(nums)
    
    right_bound = [n] * n
    left_bound = [-1] * n
    
    next_pos = [n] * 32  
    last_pos = [-1] * 32  
    
    lastSeen = {}
    
    # rightboundary
    
    for i in range(n - 1, -1, -1):
        num = nums[i]
        for bit in range(32):
            if (num & (1 << bit)) == 0:
                right_bound[i] = min(right_bound[i], next_pos[bit])
        
        for bit in range(32):
            if (num & (1 << bit)) != 0:
                next_pos[bit] = i

    # leftboundary
    
    for i in range(n):
        num = nums[i]
        lb = -1
        for bit in range(32):
            if (num & (1 << bit)) == 0:
                lb = max(lb, last_pos[bit])
        
        if num in lastSeen:
            lb = max(lb, lastSeen[num])
            
        left_bound[i] = lb
        
        for bit in range(32):
            if (num & (1 << bit)) != 0:
                last_pos[bit] = i
        lastSeen[num] = i
        
    total_good = 0
    for i in range(n):
        left_choices = i - left_bound[i]
        right_choices = right_bound[i] - i
        total_good += left_choices * right_choices
        
    return total_good



nums = [[4,2,3],[1,3,1]] # res =  4 , 6
for numSub in nums:
    print(countGoodSubarrays(numSub))
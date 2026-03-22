from collections import deque
def minRemovals(nums, target):
    curr_xor = 0
    avail_nums = list(set(nums))
    queue = deque([(0, 0)])  
    visited_states = {0}
    
    for num in nums:
        curr_xor^=num
    
    tar_to_remv = curr_xor ^ target
    
    if tar_to_remv == 0:
        return 0
    
    if tar_to_remv in avail_nums:
        return 1
    
    while queue:
        curr_val, steps = queue.popleft()
        
        for num in avail_nums:
            next_val = curr_val ^ num
            
            if next_val == tar_to_remv:
                return steps + 1
                
            if next_val not in visited_states:
                visited_states.add(next_val)
                queue.append((next_val, steps + 1))
                
    return -1

nums = [1,2,3]
target = 2
res = minRemovals(nums,target)    
print(res)
        
                
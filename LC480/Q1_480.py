def absDifference(nums,k) -> int:
    nums.sort()
    return abs(sum(nums[-k:]) - sum(nums[:k]))
    
# Idk the inputs
    
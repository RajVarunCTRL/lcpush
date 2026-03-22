
def uniformArray(nums1):
    # Q1. 
    # nums1 contains distinct integers of n.
    # construnct anotehr array of nums 2 of len n, 
    # nums2 are either all orr do even.
    
    # smallest number is odd
    mv = min(nums1)
    if mv%2!=0:
        return True 
    
    for num in nums1:
        if num%2 != 0:
            return False
    return True

nums1 = [1,4,7]
uniformArray(nums1)

    
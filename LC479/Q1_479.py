def sortByReflection(nums):
    def tempFunc(n):
        binary_str = bin(n)[2:]
        reversed_binary_str = binary_str[::-1]
        
        return int(reversed_binary_str, 2)
    
    nums.sort(key=lambda x: tempFunc(x))
    
    return nums

input_nums = [8,2]
print(sortByReflection(input_nums))
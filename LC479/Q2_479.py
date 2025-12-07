def largestPrime(n:int)->int:
    if n<2:
        return 0
    
    
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False
    
    for prim in range(2,int(n**0.5)+1):
        if is_prime[prim]:
            for multiple in range(prim*prim,n+1,prim):
                is_prime[multiple] = False
    maxPrimSum = 0
    curr_sum = 0
    
    
    for num in range(2,n+1):
        if is_prime[num]:
            curr_sum += num
        if curr_sum>n:
            break
        if is_prime[curr_sum]:
            maxPrimSum = curr_sum
    return maxPrimSum

ins = [20,2]
for i in ins:
    print(largestPrime(i))
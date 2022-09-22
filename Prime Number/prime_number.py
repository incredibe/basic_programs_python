# Prime number: A number is a prime number if it is divisible by itself and 1 , so the number factors for any prime number is 2.
# The approach is by taking factors of given number.
# You can use any method.

import math
# Taking 'A' variable as input from the user
A=int(input())  
# Creating a function
def solve(A):
    i = 1
    # Taking sqrt of A. The reason for taking sqrt of A is for faster process
    sq = math.sqrt(A)
    #Intaially count is 0
    count = 0
    # Counting the factors by using While loop
    while i <= sq:
        if A % i == 0:
            if i != A/i:
                count += 2
            else:
                count += 1
            
        i += 1
    # If count is 2 then it is prime 
    if count == 2:
        return 1
    else:
        return 0
        
print(solve(A))

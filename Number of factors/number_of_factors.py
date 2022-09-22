import math
N=int(input())
i = 1
sq = math.sqrt(N)
count = 0
while i <= sq:
    if N % i == 0:
        if i != N/i:
            count += 2
        else:
            count += 1
        
    i += 1
    
print(count)

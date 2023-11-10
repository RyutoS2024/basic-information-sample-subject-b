import math

def findPrimeNumber(maxNum: int):
    
    pnList = []
    
    for i in (2, maxNum+1, 1):
        divideFlag = True
        
        sqrt_i = int(math.sqrt(i)) # iの正の平方根の整数部分を計算する
        if int(math.sqrt(i)) < 2:
            continue
        
        print(math.sqrt(i))
        
        for j in range(2, int(math.sqrt(i)), 1):
            print(j)
            if (i % j == 0):
                divideFlag = False
                continue
            
        if (divideFlag == True):
            pnList.append(i)
            
    return pnList
    
print(findPrimeNumber(10))
    
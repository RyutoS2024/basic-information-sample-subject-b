def gcd(num1: int, num2: int): 
    x = num1
    y = num2
    
    # xとyが一致しないときに繰り返す
    while (x != y):
        # xがyよりも大きいとき
        if (x > y):
            x = x - y # xからyを引く
        # yがxよりも大きいとき
        else:
            y = y - x # yからxを引く
            
    # xとyが一致するときxを返す
    return x
    
print(gcd(36, 60))
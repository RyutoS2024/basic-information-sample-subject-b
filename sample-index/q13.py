from typing import List

# 2文探索法
def search(data: List[int], target: int):
    
    low = 1
    high = len(data)
    
    while (low <= high):
        middle = (low + high) // 2 # 計算結果の商を求める
        if (data[middle] < target):
            low = middle
        elif (data[middle] > target):
            high = middle
        else:
            return middle
        
    return -1
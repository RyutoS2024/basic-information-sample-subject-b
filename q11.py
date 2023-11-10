from typing import List

def binSort(data: List[int]):
    n = len(data)
    bins = [None] * n
        
    for i in range(0, n):
        bins[data[i]] = data[i]
        
    return bins

print(binSort([1, 5, 2, 0, 3, 4]))
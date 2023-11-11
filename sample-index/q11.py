from typing import List

def binSort(data: List[int]):
    n = len(data)
    bins = [None] * n
        
    for i in range(0, n):
        bins[data[i]] = data[i]
        
    return bins

# Pythonは配列の要素が0から始まるためプログラム要素-1をする
print(f'ア{binSort([1, 5, 2, 0, 3, 4])}')
print(f'イ{binSort([2, 0, 3, 3, 4, 1])}')
print(f'ウ{binSort([3, 1, 0, 4, 5, 1])}')
print(f'エ{binSort([4, 2, 3, 2, 1, 5])}')
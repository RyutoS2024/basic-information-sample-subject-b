data = [2, 1, 3, 5, 4]

def sort(first: int, last: int):
    pivit = data[(first + last) // 2]
    i = first
    j = last
    
    while True:
        while (data[i] < pivit):
            i = i + 1
        
        while (pivit < data[j]):
            j = j + 1
        
        if (i >= j):
            return
        
        i = i + 1
        j = j - 1
        
        if (first < i - 1):
            sort(first, i - 1)
        
        if (j + 1 < last):
            sort(j + 1, last)
from typing import List

def simRatio(s1: List[str], s2: List[str]):
    cnt = 0
    
    if (len(s1) != len(s2)):
        return -1
    
    for i in range(0, len(s1)):
        if (s1[i] == s2[i]):
            cnt = cnt + 1
            
    return cnt / len(s1)    

s1 = ['a', 'p', 'p', 'l', 'e']
s2 = ['a', 'p', 'p', 'l', 'e']
s2 = ['a', 'p', 'r', 'i', 'l']
s2 = ['m', 'e', 'l', 'o', 'n']
s2 = ['p', 'e', 'n']

print(simRatio(s1, s2))
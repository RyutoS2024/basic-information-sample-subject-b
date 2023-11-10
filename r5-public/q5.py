from typing import List
import math

def calcCosineSimilarity(vector1: List[float], vector2: List[float]):
    
    temp = 0
    numerator = 0
    
    for i in range(0, len(vector1)):
        numerator = numerator + (vector1[i] * vector2[i])
        
    for i in range(0, len(vector1)):
        temp = temp + vector1[i] ** 2
        
    denominator = math.sqrt(temp)
    
    temp = 0
    
    for i in range(0, len(vector2)):
        temp = temp + vector2[i] ** 2
        
    denominator = denominator * (math.sqrt(temp))
    
    similarity = numerator / denominator
    return similarity

vector1 = [2, 3, 4, 5, 6]
vector2 = [1, 2, 3, 4, 5]

print(calcCosineSimilarity(vector1, vector2))
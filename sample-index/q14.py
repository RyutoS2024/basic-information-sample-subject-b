from typing import List
import math

def findRank(sortedData: List[float], p:  float):
    
    i = math.ceil(p * (len(sortedData) - 1)) # 小数点を切り上げる
    return sortedData[i]



def summarize(sortedData: List[float]):
    rankData = []
    p = [0, 0.25, 0.5, 0.75, 1]
    
    for i in range(0, len(p)):
        rankData.append(findRank(sortedData, p[i]))
        
    return rankData

dataList = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

print(summarize(dataList))

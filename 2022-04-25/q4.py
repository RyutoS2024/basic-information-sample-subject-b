from typing import List

# 2次元配列
matrix = [
    [3, 0, 0, 0, 0], # i=0
    [0, 2, 2, 0, 0], # i=1
    [0, 0, 0, 1, 3], # i=2
    [0, 0, 0, 2, 0], # i=3
    [0, 0, 0, 0, 1] # i=4
]

# 与えられた行列を整数型配列の配列に変換する
def transformSparseMatrix(matrix: List[List[int]]):
    
    # 要素数が0の配列を3つ持つ2次元配列
    sparseMatrix = [
        [],
        [],
        []
    ]
    
    for i in range(0, len(matrix)): # 外側の配列をループする
        for j in range(0, len(matrix[i])): # 内側の配列をループする
            if (matrix[i][j] != 0): # 内側の配列が0でないとき
                sparseMatrix[0].append(i + 1) # sparseMatrixの1つ目の配列にi+1の値を追加する
                sparseMatrix[1].append(j + 1) # sparseMatrixの2つ目の配列にj+1の値を追加する
                sparseMatrix[2].append(matrix[i][j]) # sparseMatrixの3つ目の配列にmatrix[i][j]の値を追加する
    
    return sparseMatrix # 作成した2次元配列を返す

print(transformSparseMatrix(matrix))
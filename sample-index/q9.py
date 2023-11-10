tree = [
    [2,3],
    [4,5],
    [6,7],
    [8,9],
    [10,11],
    [12,13],
    [14],
    [],
    [],
    [],
    [],
    [],
    [],
    []
    ]

def order(n: int):
    # 要素数が2と等しいとき
    if (len(tree[n-1]) == 2):
        order(tree[n-1][0])
        print(n, end=', ') # 改行を「, 」に変換する
        order(tree[n-1][1])
    # 要素数が1と等しいとき
    elif (len(tree[n-1]) == 1):
        order(tree[n-1][0])
        print(n, end=', ')
    # 要素数が0のとき
    else:
        print(n, end=', ')
        
order(1) 
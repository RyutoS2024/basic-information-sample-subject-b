# 関数 add は，引数で指定された正の整数 value を大域の整数型の配列 hashArray に格納する。
# 格納できた場合は true を返し，格納できなかった場合は false を返す。
# ここで，整数 value を hashArray のどの要素に格納すべきかを，関数 calcHash1 及びcalcHash2 を利用して決める。
# 手続 test は，関数 add を呼び出して，hashArray に正の整数を格納する。
# 手続 test の処理が終了した直後の hashArray の内容は，　である。


hashArray = []
hashArray = [-1, -1, -1, -1, -1]

def add(value: int):
    i = calcHash1(value)
    if (hashArray[i] == -1):
        hashArray[i] = value
        return True
    else:
        i = calcHash2(value)
        if (hashArray[i] == -1):
            hashArray[i] = value
            return True
        
    return False

def calcHash1(value: int):
    return (value % len(hashArray)) 


def calcHash2(value: int):
    return ((value + 3) % len(hashArray)) 

def test():
    add(3)
    add(18)
    add(11)
    
test()
print(hashArray)
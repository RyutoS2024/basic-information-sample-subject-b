# 整数型の配列arrayの要素数を逆順にする
array = [1, 2, 3, 4, 5] # 配列の初期値

fin = len(array) // 2 # 要素数を2で割った商を取得する

# leftを1から(arrayの要素数%2の商)まで1ずつ増やす
for left in range(0, fin): # Pythonでは要素番号は0から始まる

    right = len(array) - (left + 1) # 配列の右にある数値を取得するため，インデックス数を求める
    tmp = array[right] # 配列の右に位置する数値をtmpに代入する
    array[right] = array[left] # 配列の左にある数値を右の数値に更新する
    array[left] = tmp # 配列の右にあった数値を左の数値に更新する
    
print(array) # 並び替えた配列を出力する
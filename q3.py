def makeNewArray(array_in: list[int]):
    # 空の配列を用意する
    array_out = []
    # 配列の1つ目の値をarray_outに追加する
    array_out.append(array_in[0])
    
    # iを1~5までループする
    for i in range(1, len(array_in)):
        # 配列（array_out）の最後の値を取得する
        tail = array_out[len(array_out) - 1]
        # 配列（array_out）の最後の値とarray_in[i]の値を足して，配列（array_out）に追加する
        array_out.append(tail + array_in[i])
    
    return array_out

print(makeNewArray([3, 2, 1, 6, 5, 4]))
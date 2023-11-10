def fizzBuzz(num: int):
    if (num % 3 == 0 and num % 5 == 0): #この条件式がtrueのとき他の処理は実行されない
        result = '3と5で割り切れる'
    elif (num % 3 == 0):
        result = '3で割り切れる' # 1つ目がfalseでこの条件式がtrueのとき出力される
    elif (num % 5 == 0):
        result = '5で割り切れる' # 1, 2つ目がfalseでこの条件式がtrueのとき出力される
    else:
        result = '3でも5でも割り切れない' # すべてfalseのときに出力される
    
    return result

print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(15))
print(fizzBuzz(17))
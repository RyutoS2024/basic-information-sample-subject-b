def fee(age):
    ret = 0
    # 0歳から3歳まで
    if (age <= 3):
        ret = 100
    # 4歳から9歳まで
    elif (age <= 9):
        ret = 300
    # 10歳以上
    else:
        ret = 500
    return ret

print(f'ageが3歳のとき{fee(3)}')
print(f'ageが4歳のとき{fee(4)}')
print(f'ageが9歳のとき{fee(9)}')
print(f'ageが10歳のとき{fee(10)}')
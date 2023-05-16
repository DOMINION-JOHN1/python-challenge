def get_multiples(arrayA,num):
    arrayA = [2, 4, 6, 8, 10, 12, 14]
    num = 2
    return [x for x in arrayA if x % num == 0]
result = get_multiples('arrayA','num')
print(result)



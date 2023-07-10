arrayA = [2, 4, 6, 8, 10, 12, 14]
num = 2


def get_multiples():
    return [x for x in arrayA if x % num == 0]


print(get_multiples())

def find_multiples_in_array():
    num = int(input("Enter a number: "))
    arr = input("Enter a list of numbers separated by spaces: ").split(',')
    arr = [int(x) for x in arr]
    for x in arr:
        if x % num == 0:
            print(x)


find_multiples_in_array()


def multi_calc(*array):
    num=float(input("enter value here; "))
    for i in array:
         print((i%num)==0)


multi_calc(7,6,5,4,3,6,7,8,7,67,65,43,89)

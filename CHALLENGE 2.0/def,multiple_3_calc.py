def multi_calc(*array):
    num=float(input("enter value here; "))
    for i in array:
         if i%num==0:
             print(i)

multi_calc(7,8,9,0,888,90,87,67,6,67,889,88,987)

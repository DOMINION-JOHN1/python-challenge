def triangle_num(a, b, c):
    if (a + b > c) and (b + c > a) and (c + a > b):
        return True
    else:
        return False

## you can change the parameters of this function to test different numbers
print(triangle_num(4,5,6))




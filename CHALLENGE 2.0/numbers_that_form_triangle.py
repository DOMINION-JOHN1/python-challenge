def triangle_num(num1, num2, num3):
    if (num1 + num2 > num3) and (num2 + num3 > num1) and (num3 + num1 > num2):
        return True
    else:
        return False


# you can change the parameters of this function to test different numbers
print(triangle_num(4, 8, 6))

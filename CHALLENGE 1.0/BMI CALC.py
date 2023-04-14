def bmi_calc(w,h):
    w=int(input('please input your weight here: '))
    h=int(input('please input your height here: '))
    bmi=(w*703)/(h**2)
    if bmi<18.5:
        print(f'Underweight:{w}')
    elif bmi<24.9:
        print(f'Normal:{w}')
    elif bmi<30:
        print(f'Overweight:{w}')
    else:
        print(f'obese:{w}')



bmi_calc('w','h')

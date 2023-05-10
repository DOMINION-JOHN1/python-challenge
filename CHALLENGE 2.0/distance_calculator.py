def calculate_distance():
    x1=float(input("enter value here; "))
    y1=float(input("enter value here; "))
    x2 = float(input("enter value here; "))
    y2=float(input("enter value here; "))
    d=(((x2-x1)**2) +((y2-y1)**2))**0.5
    print(d)

calculate_distance()
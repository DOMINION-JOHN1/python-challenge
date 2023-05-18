def calculate_distance(x1, y1, x2, y2):
    if isinstance(x1, str):
        x1 = int(x1)
    if isinstance(x2, str):
        x2 = int(x2)
    if isinstance(y1, str):
        y1 = int(y1)
    return (((x2-x1)**2) + ((y2-y1)**2))**0.5
# call the function and input the desired variables


print(calculate_distance(4, 5, '7', 7))

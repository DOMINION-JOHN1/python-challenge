def check_triangle(side1, side2, side3):
    # Check if any values are missing
    if None in [side1, side2, side3]:
        raise ValueError("Some values are missing. Please provide three numbers.")

    # Convert strings to numbers if necessary
    if isinstance(side1, str):
        side1 = int(side1)
    if isinstance(side2, str):
        side2 = int(side2)
    if isinstance(side3, str):
        side3 = int(side3)

    # Check triangle inequality
    if side1+side2 > side3 and side2+side3 > side1 and side3+side1 > side2:
        return True
    else:
        return False


print(check_triangle(4, 5, '8'))

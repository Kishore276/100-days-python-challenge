def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    elif x > 0 and y < 0:
        return "Quadrant IV"
    elif x == 0 and y == 0:
        return "Origin"
    elif x == 0:
        return "On the Y-axis"
    elif y == 0:
        return "On the X-axis"
x, y = 3, -4
quadrant = find_quadrant(x, y)
print(f"The point ({x}, {y}) lies in: {quadrant}")
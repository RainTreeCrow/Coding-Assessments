# Square Sanctuary Placement

# Bono, an environmentalist, is planning to set up a wildlife sanctuary
# on a large plot of land with several trees.
# Due to donor requirements, the sanctuary must:
# Occupy a perfectly square piece of land.
# Have a tree at each corner of the square.
# Planning permissions specify that the sanctuary boundary must be entirely fenced with electric fencing.
# Bono has a budget of £2 million, with the following costs:
# Electric fencing costs £40 per meter.
# Land costs £10 per square meter.

# Given a list of tree coordinates, create an efficient algorithm
# to determine the area of the largest possible square sanctuary Bono can build within the budget.
# The function should return the area as an integer.

def calc_cost(length):
    return length * 160 + 10 * length ** 2 < 2000000

def sol(x, y):
    points = list(zip(x, y))
    max_area = 0
    for i in range(len(x)):
        for j in range(i + 1, len(y)):
            x1, y1 = x[i], y[i]
            x2, y2 = x[j], y[j]
            area = ((x1 - x2) ** 2 + (y1 - y2) ** 2) / 2
            length = area ** 0.5
            if area > max_area:
                if calc_cost(length):
                    xm = (x1 + x2) / 2
                    ym = (y1 + y2) / 2
                    x3, y3 = xm + (y1 - ym), ym + (xm - x1)
                    x4, y4 = xm - (y1 - ym), ym - (xm - x1)
                    if (x3, y3) in points and (x4, y4) in points:
                        max_area = area
    return round(max_area)
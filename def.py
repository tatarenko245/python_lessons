def cylinder(h, r):
    side = 2 * 3.14 * r * h
    circle = 3.14 * r ** 2
    full = side + 2 * circle
    return full


figure1 = cylinder(4, 3)
figure2 = cylinder(5,4)
print(figure1)
print(figure2)

x, y = [int(x) for x in input().split()]

counter = 0


def f():
    global counter, x, y
    while y % 2 == 0:
        y = y // 2
        counter += 1

    if y > x:
        y = (y + 1) // 2
        counter += 2

    # print(counter)

    if x >= y:
        counter += x - y
        return
    else:
        f()


f()
print(counter)

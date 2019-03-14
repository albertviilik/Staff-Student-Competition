fishes_count = int(input())
sizes = [int(size) for size in input().split()]

dict = dict()

dict[sizes[0]] = 0

for index, size in enumerate(sizes):
    if index == 0:
        print(0)
    else:
        items = dict.items()
        (smaller, value_smaller) = max([(value, key) for value, key in items if value < size])
        bigger, value_bigger = min([(value, key) for value, key in items if value > size])
        if bigger == None:
            dict[smaller + size] = value_smaller + 1

        print(value_smaller)
        # if smaller + size < current:
        # dict[]

rows = int(input())
cols = int(input())

# grid = [([0] * cols) for i in range(rows)]
grid = [None] * rows

for row_number in range(rows):
    # for col_number in range(cols):
    grid[row_number] = [int(x) for x in input().split()]

size = int(input())

# print(len(grid[0]))

max_oil = 0

# starting_area = grid[0:size][0:size]
starting_area = [x[0:size] for x in grid[0:size]]
# print(len(starting_area[1]))

max_oil = sum(sum(arr) for arr in starting_area)
# print(max_oil)


for i in range(cols - size + 1):
    # starting_area = [x[i:size] for x in grid[i:size]]
    # sum_oil = sum(sum(arr) for arr in starting_area)
    # if sum_oil > max_oil:
    #     max_oil = sum_oil
    for j in range(rows - size + 1):
        # print(i, j)
        # print(rows, cols)
        starting_area = [x[i:i + size] for x in grid[j:j + size]]
        sum_oil = sum(sum(arr) for arr in starting_area)
        # print(sum_oil)
        if sum_oil > max_oil:
            max_oil = sum_oil

print(max_oil)

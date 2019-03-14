# start_row = int(input())
# start_column = int(input())
# end_row = int(input())
# end_column = int(input())

# from math import abs

[start_row, start_column, end_row, end_column] = [int(x) for x in input().split()]

parity_start = (start_row + start_column) % 2
parity_end = (end_row + end_column) % 2
if parity_start != parity_end:
    print(-1)
    exit()

if (start_row, start_column) == (end_row, end_column):
    print(0)
    exit()


def same_diagonal(x1, y1, x2, y2):
    if x1 - y1 == x2 - y2:
        return True
    if x1 + y1 == x2 + y2:
        return True
    return False


def same_diagonal2(x1, y1, x2, y2):
    # return abs(x1 - x2) // abs(y1 - y2) == 1
    return abs(x1 - x2) == abs(y1 - y2)


# if same_diagonal(start_row, start_column, end_row, end_column):
if same_diagonal2(start_row, start_column, end_row, end_column):
    print(1)
else:
    print(2)

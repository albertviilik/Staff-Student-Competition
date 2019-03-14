from queue import Queue

start, end = [int(x) for x in input().split()]

if start > end:
    print(start - end)
    exit()

if start == end:
    print(0)
    exit()

queue = Queue()
# print(queue)

queue.put(start)

min_steps = [-1] * (2 * end + 1)

min_steps[start] = 0


#
# while queue.empty() == False:
#     populate_steps(min_steps, queue, queue.get())

def populate_steps(min_steps, queue, current_value):
    twice_index = 2 * current_value
    previous_index = current_value - 1
    current_steps = min_steps[current_value]
    # queue.put(twice_index)
    # queue.put(previous_index)
    if twice_index < len(min_steps):
        # queue.put(twice_index)
        if min_steps[twice_index] == -1:
            min_steps[twice_index] = current_steps + 1
            queue.put(twice_index)
        # else:
        #     min_steps[twice_index] = min(min_steps[twice_index], current_steps + 1)
    if previous_index > 0:
        # queue.put(previous_index)
        if min_steps[previous_index] == -1:
            min_steps[previous_index] = current_steps + 1
            queue.put(previous_index)
        # else:
        #     min_steps[previous_index] = min(min_steps[previous_index], current_steps + 1)

    if current_value == end:
        print(min_steps[current_value])
        exit()


while queue.empty() == False:
    populate_steps(min_steps, queue, queue.get())

print(min_steps[end])

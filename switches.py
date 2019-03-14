

inn = str(input())

counter = 0
c = 0
for i in inn:
    if i == '0':
        counter += 2 ** c
    c += 1

print(counter)

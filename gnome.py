maxNum, rowsToGet = [int(x) for x in input().split()]

inputMem = []
notYet = []
result = []

for i in range(rowsToGet):
    inputMem.append(int(input()))

all = list(range(1, maxNum + 1))

for i in all:
    if i not in inputMem:
        notYet.append(i)

toRemove = []
lastNum = 0
# for i in inputMem:
#     if lastNum > i:
#         result.append(i)
#         lastNum = i
#         continue
#     for notYetVal in notYet:
#         if notYetVal < i:
#             toRemove.append(notYetVal)
#     for val in toRemove:
#         result.append(val)
#         notYet.remove(val)
#     toRemove = []
#     result.append(i)
#     lastNum = i

# count = 0
# for index, i in enumerate(inputMem):
#     if lastNum > i:
#         lastNum = i
#         continue
#     for notYetVal in notYet:
#         if notYetVal < i:
#             result.insert(index-1+count, i)
#             count += 1
#             notYet.remove(i)
#     count = 0
#     lastNum = i

# count = 0
index = 0
while index < len(inputMem):
    if lastNum > inputMem[index]:
        lastNum = inputMem[index]
        continue
    for notYetVal in notYet:
        if notYetVal < inputMem[index]:
            inputMem.insert(index, inputMem[index])
            index += 1
            toRemove.append(notYetVal)
    for val in toRemove:
        notYet.remove(val)
    toRemove = []
    lastNum = inputMem[index]
    index += 1

for i in inputMem:
    print(i)

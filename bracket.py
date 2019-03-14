# import sys
# # for arg in sys.argv[1:]:
# #   print arg
# arg = sys.argv[1:][0]

leftList = []
dic = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}

for i in input():
    try:
        if i in ["(", "[", "{", "<"]:
            leftList.append(i)

        elif dic[leftList[-1]] != i:
            print("NO")
            break

        else:
            leftList.pop(-1)
    except:
        print("NO")
        break
else:
    if leftList:
        print("NO")
    else:
        print("YES")

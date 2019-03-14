i = int(input())

dic = {}
dic[0] = True

for k in range(0, i):
    m = int(input())
    newdic = {}
    for n in dic:
        newdic[(m + n) % 360] = True
        newdic[(n - m + 360) % 360] = True
    dic = newdic

if 0 in dic.keys():
    print("YES")
else:
    print("NO")

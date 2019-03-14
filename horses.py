from collections import defaultdict

n, k = [int(x) for x in input().split()]

dic = defaultdict(int)

mx = 0
for i in [int(x) for x in input().split()]:
    dic[i] = dic[i] + 1
    mx = max(mx, i)

# print(dic)

ans = 0
# for j in range(1, k):
#    count -= dic[j]

for h in range(k, mx + 1):
    buf = 0
    for j in sorted(dic.keys()):
        if j < h:
            continue
        buf += (j // h) * dic[j]
        # print(str(j) + " " + str(dic[j]) + "  " + str(h))
    ans = max(ans, buf * h)
    # print(str(h) + "  " + str(dic[h]) + " " + str(buf * h))
    # count -= dic[h]

print(ans)

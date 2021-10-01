n = int(input())
all = list(map(int, input().split(' ')))
save = 0
for i in range(n):
    cnt = 0
    a = -99999999999
    for j in range(i+1, n):
        inc = (all[j] - all[i]) / (j - i)
        if inc > a:
            cnt += 1
            a = inc
    a = 99999999999
    for j in range(i-1, -1, -1):
        inc = (all[j] - all[i]) / (j - i)
        if inc < a:
            cnt += 1
            a = inc
    if cnt > save:
        save = cnt
print(save)
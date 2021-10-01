n = int(input())
bricks = [(0, 0, 0, 0)]

for i in range(1, n + 1):
    wd, ht, wt = map(int, input().split())
    bricks.append((i, wd, ht, wt))

bricks.sort(key=lambda x: x[3]) #무게로 정렬

A = [0] * (n + 1)
for j in range(1, n + 1):
    for k in range(0, j):
        if bricks[j][1] > bricks[k][1]:
            A[j] = max(A[j], A[k] + bricks[j][2])

max_value = max(A)
i = n
result = []

while i > 0:
    if max_value == A[i]:
        result.append(bricks[i][0])
        max_value -= bricks[i][2]
    i -= 1

result.reverse()
print(len(result))
for r in result:
    print(r)
import sys
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def dfs(x, y, h):
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]
        if (0 <= nx < n) and (0 <= ny < n) and not v[nx][ny] and nList[nx][ny] > h:
            v[nx][ny] = True
            dfs(nx, ny, h)

n = int(sys.stdin.readline())
nList = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
numMax = max(map(max, nList))

ans = 1
for k in range(numMax):
    v = [[False] * n for _ in range(n)]
    s = 0
    for i in range(n):
        for j in range(n):
            if nList[i][j] > k and not v[i][j]:
                s += 1
                v[i][j] = True
                dfs(i, j, k)
    ans = max(ans, s)

print(ans)
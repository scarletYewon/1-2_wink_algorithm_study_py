N = int(input())#몇개?
p, m = [], []
ms=0

for _ in range(N):
    n = int(input())#뭐?

    if n > 1:
        p.append(n)
    elif n == 1:
        ms += 1 #1이면 걍 더하고 넘어감
    else:
        m.append(n)

p.sort(reverse=True)
m.sort()
#plus봐줌
if len(p) % 2 == 0:
    for i in range(0, len(p), 2):
        ms += p[i] * p[i + 1]
else:
    for i in range(0, len(p) - 1, 2):
        ms += p[i] * p[i + 1]
    ms += p[len(p) - 1]
#minus봐줌
if len(m) % 2 == 0:
    for i in range(0, len(m), 2):
        ms += m[i] * m[i + 1]
else:
    for i in range(0, len(m) - 1, 2):
        ms += m[i] * m[i + 1]
    ms += m[len(m) - 1]
print(ms)#젤큰거
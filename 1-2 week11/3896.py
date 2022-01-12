#미완성
#미완성
#미완성
#미완성
#미완성
#미완성

import sys

n=1299709
a = [False,False] + [True]*(n-1)
primes=[]
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    cnt = 0
    for i in range(n):
        if primes[k - i] == False:
            cnt += 1
        else:
            break
    for i in range(n):
        if primes[k + i] == False:
            cnt += 1
        else:
            break
    print(cnt)
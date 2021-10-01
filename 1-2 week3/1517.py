import sys

read = lambda: sys.stdin.readline().rstrip()

def merge_sort(start, end):
    global cnt, A

    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        a, b = start, mid + 1
        temp = []

        while a <= mid and b <= end:
            if A[a] <= A[b]:
                temp.append(A[a])
                a += 1
            else:
                temp.append(A[b])
                b += 1
                cnt += (mid - a + 1)

        if a <= mid:
            temp = temp + A[a:mid + 1]
        if b <= end:
            temp = temp + A[b:end + 1]

        for i in range(len(temp)):
            A[start + i] = temp[i]
cnt = 0
N = int(read())
A = list(map(int, read().split()))
merge_sort(0, N - 1)
print(cnt)



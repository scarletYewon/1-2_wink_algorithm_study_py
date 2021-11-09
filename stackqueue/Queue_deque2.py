#collections.deque 사용
# 리스트보다 시간복잡도 훨씬 빠름 (O(1))
# 내부적으로 doubly 링크드 리스트로 구현되어 있기 때문

from collections import deque

dq = deque([])

dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
print(dq)


# print(dq.pop()) -> 이렇게하면 stack됨,, popleft로 써야뎀


print(dq.popleft())
print(dq.popleft())
print(dq.popleft())
print(dq.popleft())
print(dq)
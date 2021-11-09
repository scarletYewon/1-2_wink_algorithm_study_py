# Queue 모듈 사용
# Queue 모듈에서 put은 항목 추가, get은 항목 제거,반환

import queue

q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)

print(q.get())
print(q.get())
print(q.get())
print(q.get())
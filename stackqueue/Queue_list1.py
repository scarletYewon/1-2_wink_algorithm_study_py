# 리스트 사용
# 리스트를 사용했을 경우 enqueue의 시간복잡도는 O(1), dequeue는 O(N)
# 추가는 큐의 맨 끝에서만 일어나지만
# 첫번쨰 원소 삭제시 두번쨰 원소부터 마지막 까지 모든 원소를 왼쪽으로 한칸씩 옮겨주어야 하기 때문

class ListQueue(object):
    def __init__(self):
        self.queue = []

    def dequeue(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)

    def enqueue(self,n):
        self.queue.append(n)

    def printQueue(self):
        print(self.queue)

if __name__ == "__main__":
    lq = ListQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)
    lq.enqueue(5)
    lq.printQueue()
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    lq.printQueue()

stack_list = list()

# 푸쉬 함수
def push(data):
    stack_list.append(data)

# 팝 함수
def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

# 푸쉬 보여줌
for i in range(5):
    print(i)
    push(i)
print("push end")

# 팝 보여줌
for i in range(5):
    print(pop())
    if i == 4:
        print("pop end")
def recursive(data):
    if data < 0:
        print("재귀 stack")
    else:
        print(data)
        recursive(data-1)
        print(data)

recursive(4)
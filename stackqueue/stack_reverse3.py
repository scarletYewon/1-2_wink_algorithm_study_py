word = input('Input a word: ')
world_list = list(word)

result=[]
for _ in range(len(world_list)):
    result.append(world_list.pop())
print(result)
print(''.join(result))

#걍 이거하면 되긴 함
# print(word[::-1])
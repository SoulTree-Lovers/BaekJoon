# 그룹 단어 체커

class ListStack:
    def __init__(self):
        self.__stack = []
    
    def push(self, x):
        self.__stack.append(x)
    
    def clear(self):
        self.__stack.clear()
    
    def pop(self):
        return self.__stack.pop()
    
    def top(self):
        if len(self.__stack) == 0:
            return None
        else:
            return self.__stack[-1]

    def isItIn(self, x):
        return x in self.__stack

listStack = ListStack()

n = int(input())

str_list = []

for i in range(n):
    str_list.append(input())

count = 0

for i in str_list:
    listStack.clear()
    bool = True
    for j in range(len(i)):
        if listStack.isItIn(i[j]):
            if listStack.top() != i[j]:
                bool = False
                continue

            else:
                listStack.push(i[j])

        else:
            listStack.push(i[j])

    if bool == True:
        count += 1

print(count)



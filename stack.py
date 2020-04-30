class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return f"Popped items is:{data}"

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return self.stack == []

    def sizeStack(self):
        return len(self.stack)

    def traverse(self):
        print("Stack items are:")
        for i in range(len(self.stack)-1, -1, -1):
            print(self.stack[i], " ", end=" ")
        print()


stack = Stack()
stack.push(10)
stack.push((20))
stack.push(30)
(stack.peek())
print(stack.sizeStack())
stack.push(50)
stack.traverse()
stack.push(40)
stack.traverse()
print(stack.pop())
stack.traverse()

class Queue:
    def __init__(self):
        self.enqueue_stack=[]
        self.dequeue_stack=[]

    def enqueue(self,data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if len(self.enqueue_stack)==0 and len(self.dequeue_stack)==0:
            raise Exception("Stacks are Empty")
            return

        if len(self.dequeue_stack)==0:
            while len(self.enqueue_stack)!=0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()

q=Queue()
q.enqueue(10)
q.enqueue(5)
q.enqueue(20)
print(q.dequeue())
q.enqueue(50)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(40)
q.enqueue(30)
print(q.dequeue())
print(q.dequeue())
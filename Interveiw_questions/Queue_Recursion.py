class Queue:
    def __init__(self):
        self.stack=[]

    def enqueue(self,data):
        self.stack.append(data)

    def dequeue(self):
        if len(self.stack)==1:
            return self.stack.pop()  # this is first item of stack when pushed

        item = self.stack.pop()
        dequeued_item = self.dequeue()  # terminate when len(stack)==1 then it has first item of stack

        # we start appending poped item one by one onto stack
        self.stack.append(item)
        return dequeued_item

q=Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(20)
print(q.dequeue(),q.dequeue())
q.enqueue(50)
print(q.dequeue(),q.dequeue())


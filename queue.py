class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,data):
        self.queue.append(data)
        print(f"enqued item is:{data}")

    def dequeue(self):
        data=self.queue[0]
        del self.queue[0]
        print(f"Dequed item is:{data}")

    def size(self):
        return len(self.queue)

    def traverse(self):
        for i in self.queue:
            print(i," ",end="")
        print()

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.traverse()
q.dequeue()
q.dequeue()
q.traverse()

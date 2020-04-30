CAPACITY = 10


class Heap:
    def __init__(self):
        self.heap = [0] * CAPACITY
        self.heap_size = 0

    def insert(self,item):
        if CAPACITY==self.heap_size:
            return
        self.heap[self.heap_size]=item
        self.heap_size+=1

        # validate heap Properties
        self.fix_up(self.heap_size-1)

    def fix_up(self,index):

        # find index's parent index to check whether it parent > node ?
        parent_index=(index-1)//2

        # go node index(last) to up parent index(0)
        if index>0 and self.heap[index]>self.heap[parent_index]:
            self.swap(index,parent_index)
            self.fix_up(parent_index)

    def swap(self,index1,index2):
        self.heap[index1],self.heap[index2]=self.heap[index2],self.heap[index1]

    def poll(self):
        max = self.heap[0]
        self.swap(0,self.heap_size-1)
        self.heap_size-=1
        self.fix_down(0)
        return max

    def fix_down(self,index):
        left_index=2*index+1
        right_index=2*index+2
        largest_index=index

        # if left child > root(parent) swap it place largest item in last index and forget it index
        # to delete it
        if left_index < self.heap_size and self.heap[left_index] > self.heap[largest_index]:
            largest_index=left_index
        if right_index < self.heap_size and self.heap[right_index] > self.heap[largest_index]:
            largest_index=right_index

        if index!=largest_index:
            self.swap(index,largest_index)
            self.fix_down(largest_index)

    def heap_sort(self):
        size=self.heap_size

        for i in range(0,size):
            max=self.poll()
            print(max)


h=Heap()
h.insert(10)
h.insert(8)
h.insert(12)
h.insert(20)
h.insert(-2)
h.insert(0)
h.insert(1)
h.insert(321)

h.heap_sort()

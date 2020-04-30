CAPACITY = 10


class Heap:
    def __init__(self):
        self.heap = [0] * CAPACITY
        self.heap_size = 0

    # O(1)+validation O(logn)


    def insert(self, item):
        if CAPACITY == self.heap_size:
            print("Capacity exceed")
            return
        self.heap[self.heap_size] = item
        self.heap_size += 1

        # fix validation bottom to up first check child>parent? start from last inserted index
        self.fix_up(self.heap_size - 1)

    def fix_up(self, index):

        # find parent of given index to check child>parent?
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.fix_up(parent_index)
    # O(1)
    def get_max(self):
        return self.heap[0]

    # return max of heap and remove that item from heap -> validation need from up to down
    # take out max(heap[0]) swap it to last index of heap and forget that last index
    def poll(self):
        max = self.get_max()
        self.swap(0, self.heap_size - 1)
        self.heap_size = self.heap_size-1
        self.fix_down(0)
        return max

    def fix_down(self,index):
        index_left=2*index+1
        index_right=2*index+2
        index_largest=index    # root node is largest

        if index_left<self.heap_size and self.heap[index_left]>self.heap[index_largest]:
            index_largest = index_left
        if index_right < self.heap_size and self.heap[index_right]>self.heap[index_largest]:
            index_largest=index_right

        if index!=index_largest:
            self.swap(index,index_largest)
            self.fix_down(index_largest)

    def heap_sort(self):
        size=self.heap_size
        for i in  range(0,size):
            max=self.poll()
            print(max)

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

if __name__=="__main__":
    heap=Heap()
    heap.insert(10)
    heap.insert(8)
    heap.insert(12)
    heap.insert(20)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(1)
    heap.insert(321)

    heap.heap_sort()


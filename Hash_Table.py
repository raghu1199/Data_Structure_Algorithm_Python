class HashTable:
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

    # hash function -> convert key into index of array
    def hash(self, key):
        sum1 = 0
        for i in range(len(key)):
            sum1 = sum1 + ord(key[i])

        return sum1 % self.size

    def put(self, key, data):
        # get index from hash function
        index = self.hash(key)

        # if index already filled -> keys[index] not None
        # check given key == keys[index] if yes then update data
        # no then collision ocuured-> find next empty index
        while self.keys[index] is not None:
            # update data if key == self.keys[index]
            if self.keys[index] == key:
                self.values[index] = data
                return

            index = (index + 1) % self.size

        # if not collision or updated index insert direct to keys and values
        self.keys[index] = key
        self.values[index] = data

    # find given key and if found return value at given index
    # if collision then check next index if not found return None
    def get(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            else:
                index=(index+1) % self.size

        return None

table = HashTable()
table.put("apple",10)
table.put("orange",20)
table.put("car",40)
table.put("raghu",90)

print(table.get("raghu"))
table.put("raghu",60)
print(table.get("raghu"))

class Max_Stack:
    def __init__(self):
        self.main_stack=[]
        self.max_stack=[]

    def push(self,data):
        self.main_stack.append(data)
        if len(self.main_stack)==1:
            self.max_stack.append(data)
            return
        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    def get_max(self):
        return self.max_stack.pop()


st= Max_Stack()
st.push(1000)
st.push(5)
st.push(12)
st.push(100)

print(st.get_max())


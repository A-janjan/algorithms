class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.s = [0] * max_size
        self.num = 0

    def push(self, item):
        if(self.num >= self.max_size):
            raise Exception("Stack Overflow")
        self.s[self.num] = item
        self.num += 1

    def pop(self):
        if(self.num==0):
            raise Exception("Stack is Empty")
        item = self.s[self.num-1]
        self.num -= 1
        return item
    
    def is_empty(self):
        return self.num==0

    def is_full(self):
        return self.num >= self.max_size

    def size(self):
        return self.num
    
    def top(self):
        if(self.num == 0):
            raise Exception("Stack is Empty")
        return self.s[self.num-1]
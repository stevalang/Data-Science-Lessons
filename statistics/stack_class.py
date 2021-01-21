import random

class Stack():
    def __init__(self, lst):
        self.lst = lst

        for _ in self.lst:
            self.length += 1

        self.stack = [None] * self.length

        for i in range(self.length):
            self.stack[i] = self.lst[i]

            if i == self.length -1:
                self.top = self.lst[i]

    def __len__(self):
        return self.length

    def push(self):

        self.length += 1
        tmp = [None] * self.length

        for i in range(self.length - 1):
            tmp[i] = self.stack[i]

        tmp[-1] = self.top
        return tmp

    def peek(self):
        return self.top

    def pop(self):
        self.length -= 1
        tmp = self.top
        tmp_stack = [None] * self.length

        for i in range(self.length):
            tmp_stack[i] = self.stack[i]

        self.stack = tmp_stack
        self.top = self.stack[-1]

        return tmp


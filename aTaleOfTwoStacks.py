class MyQueue():
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    # pushes all nex values to the in stack
    def put(self, value):
        self.stack_in.append(value)

    # peeks and pops from the out stack
    # but first checks if the out stack is empty
    # only moves over new values when out stack is empty
    # (and therefore the new values are needed)
    def peek(self):
        self.fill_stack_out()
        return self.stack_out[-1] # <- instead of getting the length of the array
        # if not using index,
        # you could pop into a variable and push back on

    def pop(self):
        self.fill_stack_out()
        return self.stack_out.pop()

    def fill_stack_out(self):
        if len(self.stack_out) == 0:
            # while len(self.stack_in) > 0:
            #     self.stack_out.append(self.stack_in.pop())

            # alternatively:
            self.stack_out = self.stack_in[::-1]
            self.stack_in = []




queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

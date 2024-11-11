class MyQueue(object):

    # constructor to initialize two stacks
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        self.stack1.push(x)

        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def pop(self):
        return self.stack1.pop()

    def peek(self):
        return self.stack1.top()

    def empty(self):
        return self.stack1.is_empty()

# Helper function
class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()

# Driver code
def main():
    input_queues = [
        [[9, 3, 1, "", "", ""], ["push", "push", "push", "pop", "peek", "empty"]],
        [[10, 6, "", "", ""], ["push", "push", "pop", "empty", "peek"]],
        [[1, 2, 3, "", "", "", "", ""], ["push", "push", "push", "peek", "pop", "pop", "pop", "empty"]],
        [[14, "", 66, ""], ["push", "pop", "push", "pop"]],
        [[4, ""], ["push", "peek"]]]
    for i in range(len(input_queues)):

        print(i + 1, ".\t Starting operations:", sep="")

        # initialize a queue
        queue_obj = MyQueue()
        # loop over all the commands
        for j in range(len(input_queues[i][1])):
            if input_queues[i][1][j] == "push":
                inputstr = input_queues[i][1][j] + \
                           "("+str(input_queues[i][0][j])+")"
                print("\t\t", inputstr, sep="")
                queue_obj.push(input_queues[i][0][j])
            if input_queues[i][1][j] == "pop":
                inputstr = input_queues[i][1][j] + \
                           "("+str(input_queues[i][0][j])+")"
                print("\t\t", inputstr, "   returns ",
                      queue_obj.pop(), sep="")
            if input_queues[i][1][j] == "empty":
                inputstr = input_queues[i][1][j] + \
                           "("+str(input_queues[i][0][j])+")"
                print("\t\t", inputstr, " returns ",
                      queue_obj.empty(), sep="")
            if input_queues[i][1][j] == "peek":
                inputstr = input_queues[i][1][j] + \
                           "("+str(input_queues[i][0][j])+")"
                print("\t\t", inputstr, "  returns ",
                      queue_obj.peek(), sep="")

        print("-" * 100)


if __name__ == "__main__":
    main()

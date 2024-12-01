from stack import Stack

def main():
    stack1 = Stack(10)
    for i in range(10):
        stack1.push(i)
    print(stack1.display())

    stack2 = Stack(5)
    stack2.push(1)
    stack2.push(2)
    stack2.push(3)
    stack2.pop()
    print(stack2.peek())
    print(stack2.size())
    print(stack2.display())

if __name__ == "__main__":
    main()
##----- Class Stack with their Operations -----##
class Stack:
    def __init__(self):
        print("Stack is all set to work on......\n")
        self.stack = []

    def __Insertion__(self):
        self.stack.append((input("Enter Element :: ")))
        print("\nElement Inserted Successfully!!!\n")

    def __Traversion__(self):
        index = 0
        for element in self.stack:
            print(f"Element :: {element}\tAt Index :: {index}")
            index+=1

    def __Pop_LIFO__(self):

        try:
            print("Element Popped ::",self.stack[-1])
            self.stack.remove(self.stack[-1])
            print("\nElement Popped Successfully!!!\n")
        except IndexError:
            print("Stack is empty!!!\n")

##----- END of this Class -----##


##----- Class Test to Start Operation of Stack -----##
class Test:
    def __init__(self):
        self.StackObject = Stack()

    def __Menu__(self):
        print("1. Insertion\n2. Traversion\n3. Pop ( LIFO )\n4. Exit\n\nEnter Your Choice :: ",end="")
        self.choice = input()

    def __StartOperation__(self):
        while True:
            self.__Menu__()
            if self.choice == '1':
                self.StackObject.__Insertion__()
            elif self.choice == '2':
                self.StackObject.__Traversion__()
            elif self.choice == '3':
                self.StackObject.__Pop_LIFO__()
            elif self.choice == '4':
                exit(0)
            else:
                print("\nWrong Choice....\n")

##----- END of this Class -----##

tstobj = Test()
tstobj.__StartOperation__()
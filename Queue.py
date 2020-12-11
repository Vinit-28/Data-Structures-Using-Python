##----- Class Queue with their Operations -----##
class Queue:
    def __init__(self):
        print("Queue is all set to work on......\n")
        self.Queue = []

    def __Insertion__(self):
        self.Queue.append((input("Enter Element :: ")))
        print("\nElement Inserted Successfully!!!\n")

    def __Traversion__(self):
        index = 0
        for element in self.Queue:
            print(f"Element :: {element}\tAt Index :: {index}")
            index+=1

    def __Pop_FIFO__(self):
        try:
            print("Element Popped ::",self.Queue[0])
            self.Queue.remove(self.Queue[0])
            print("\nElement Popped Successfully!!!\n")
        except IndexError:
            print("Queue is empty!!!\n")

##----- END of this Class -----##


##----- Class Test to Start Operation of Queue -----##
class Test:
    def __init__(self):
        self.QueueObject = Queue()

    def __Menu__(self):
        print("1. Insertion\n2. Traversion\n3. Pop ( FIFO )\n4. Exit\n\nEnter Your Choice :: ",end="")
        self.choice = input()

    def __StartOperation__(self):
        while True:
            self.__Menu__()
            if self.choice == '1':
                self.QueueObject.__Insertion__()
            elif self.choice == '2':
                self.QueueObject.__Traversion__()
            elif self.choice == '3':
                self.QueueObject.__Pop_FIFO__()
            elif self.choice == '4':
                exit(0)
            else:
                print("\nWrong Choice....\n")

##----- END of this Class -----##

tstobj = Test()
tstobj.__StartOperation__()
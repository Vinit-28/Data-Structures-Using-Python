
##---------- Class HeapDs to perform operation on Heap Data Structure ----------##
class HeapDS:
    def __init__(self):
        print("\nHeap Data-Structure is all set to work on...")
        self.Database = []
        self.Index = self.choice = self.temp = 0
        self.CurrentIndex = -1
        input("\nPress any Key to Start Working on Heap Data-Structure !!!!! \n")
        self.__Menu__()

    def __Menu__(self):
        while True:
            self.choice = input("\n1. Insertion\n2. Traversion\n3. Searching\n4. Deletion\n5. Exit\n\nEnter Your Choice :: ")

            if self.choice == '1':
                self.__Insertion__()
            elif self.choice == '5':
                exit(0)
            elif len(self.Database) == 0:
                print("\nHeap Data-Structure is Empty....\nPlease Insert Data Elements First...\n")
            elif self.choice == '2':
                self.__Traversion__()
            elif self.choice == '3':
                self.__Searching__()
            elif self.choice == '4':
                self.__Deletion__()
            else:
                print("\nWrong Choice.... Choose Again...... \n")


    def __Insertion__(self):
        self.Database.append(int(input("Enter Data Element :: ")))
        self.CurrentIndex += 1
        self.Index = (self.CurrentIndex-1)//2
        self.temp = self.CurrentIndex

        if self.CurrentIndex > 0:

            while self.Database[self.temp] > self.Database[self.Index]:
                self.Database[self.temp],self.Database[self.Index] = self.Database[self.Index],self.Database[self.temp]

                self.temp = self.Index
                self.Index = (self.Index-1)//2
                if self.Index < 0:
                    break
        print("\nData Inserted Successfully !!!..\n")

    def __Traversion__(self):
        print("\n",self.Database)


    def __Deletion__(self):
        print("\nOnly Root-Element can be deleted only....\n")
        print("Deleting Element --------> ",self.Database[0])

        self.temp = self.Database[-1]
        self.Database.remove(self.temp)
        self.Index = 0
        self.CurrentIndex -= 1

        while True:
            if ((self.Index*2)+1) <len(self.Database) and ((self.Index*2)+2) < len(self.Database):
                if self.Database[(self.Index*2)+1] > self.Database[(self.Index*2)+2]:
                    self.Database[self.Index] = self.Database[(self.Index*2)+1]
                    self.Index = (self.Index*2)+1
                else:
                    self.Database[self.Index] = self.Database[(self.Index*2)+2]
                    self.Index = (self.Index*2)+2

            elif ((self.Index*2)+1) <len(self.Database) or ((self.Index*2)+2) < len(self.Database):
                if ((self.Index*2)+1) <len(self.Database):
                    self.Database[self.Index] = self.Database[(self.Index*2)+1]
                    self.Index = (self.Index*2)+1
                else:
                    self.Database[self.Index] = self.Database[(self.Index * 2) + 2]
                    self.Index = (self.Index * 2) + 2

            else:
                break

        try:
            self.Database[self.Index] = self.temp
        except:
            pass
        print("\nData Element Deleted Successfully !!!!\n")


    def __Searching__(self):
        self.choice = input("\n1. Find Parent\n2. Find Child\n\nEnter Your Choice :: ")
        self.Index = 0

        if self.choice == '1':
            self.temp = int(input("\nEnter Data Element to find their Parent Node :: "))
            while self.Index < len(self.Database):
                if self.Database[self.Index] == self.temp:
                    if not (self.Index-1)//2 < 0:
                        print(f"\nParent :: {self.Database[(self.Index-1)//2]}\t\tChild :: {self.Database[self.Index]}\n")
                    else:
                        print(f"\nIts a Root Data Element :: {self.temp}")
                    return

                self.Index+=1

        elif self.choice == '2':
            self.temp = int(input("\nEnter Data Element to find their Child Nodes :: "))
            while self.Index < len(self.Database):
                if self.Database[self.Index] == self.temp:
                    if (self.Index*2)+1 < len(self.Database):
                        print("\nLeft Node Element ::",self.Database[(self.Index*2)+1])
                    else:
                        print("\nLeft Node Element :: None")

                    if (self.Index*2)+2 < len(self.Database):
                        print("\nRight Node Element ::",self.Database[(self.Index*2)+2])
                    else:
                        print("\nRight Node Element :: None")
                    return


                self.Index+=1


        else:
            print("\nWrong Choice .......\n")
            return

        print("\nInvalid Data Element ......\n")

##---------- END of this Class ----------##


##---------- Making object of class HeapDS to work on Heap Data Structure ----------##
TestObject = HeapDS()
##----- Class to Crate Nodes -----##
class Node:
    def __init__(self,Data=0):
        self.Data = Data
        self.LeftNode = None
        self.RightNode = None

##----- END of this Class -----##


##----- Class to Work on BinarySearchTree -----##
class BinarySearchTree:
    def __init__(self):
        print("\nBinary Search Tree is all set to work on\n")
        self.Start = self.choice = self.temp = self.beforetemp = None
        self.LastMove = 'NoMoveYet'
        self.DataList = []
        input("Hit any Key to Start Operations on BinarySearchTree.......")
        self.__Menu__()

    def __Menu__(self):
        while True:
            print("\n1. Insertion\n2. Traversion\n3. Deletion\n4. Exit\n")
            self.choice = input("Enter You Choice :: ")
            if self.choice == '1':
                self.__Insertion__()
            elif self.choice == '2':
                self.__Traversion__()
            elif self.choice == '3':
                self.__Deletion__()
            elif self.choice == '4':
                exit(0)
            else:
                print("\nWrong Choice..... Choose Again...\n")


    def __Insertion__(self):
        NewNode = Node()
        NewNode.Data = int(input("\nEnter Node Data :: "))

        if not self.__FixNodeInTree__(NewNode = NewNode):
            print("\nUnable to Insert NewNode ......\nReason  :::  Node Data Already Exits....\n\n")
        else:
            print("\nNode Inserted Successfully!!!.....\n")


    def __FixNodeInTree__(self,NewNode):

        if self.Start == None:
            self.Start = NewNode

        else:
            self.temp = self.beforetemp = self.Start
            while self.temp !=  None:
                if NewNode.Data < self.temp.Data:
                    print("Left")
                    self.beforetemp = self.temp
                    self.temp = self.temp.LeftNode
                    self.LastMove = 'Left'

                elif NewNode.Data > self.temp.Data:
                    print("Right")
                    self.beforetemp = self.temp
                    self.temp = self.temp.RightNode
                    self.LastMove = 'Right'

                else:
                    return False

            if self.LastMove == 'Left':
                self.beforetemp.LeftNode = NewNode
            elif self.LastMove == 'Right':
                self.beforetemp.RightNode = NewNode

        return True


    def __Traversion__(self):
        self.choice = input("\n1. Pre-Order Traversion -----> RootNode-LeftNode-RightNode\n2. In-Order Traversion -----> LeftNode-RootNode-RightNode\n3. Post-Order Traversion -----> LeftNode-RightNode-RootNode\n\nEnter Your Choice :: ")
        if self.choice == '1':
            self.__ALLTraversions__(temp = self.Start)
        elif self.choice == '2':
            self.__ALLTraversions__(temp = self.Start)
        elif self.choice == '3':
            self.__ALLTraversions__(temp = self.Start)
        else:
            print("\nWrong Choice.........\n")


    def __ALLTraversions__(self,temp):
        if self.choice == '1':
            print(temp.Data,end="\t")

        if temp.LeftNode != None:
            self.__ALLTraversions__(temp = temp.LeftNode)

        if self.choice == '2':
            print(temp.Data, end="\t")

        if temp.RightNode != None:
            self.__ALLTraversions__(temp = temp.RightNode)

        if self.choice == '3':
            print(temp.Data, end="\t")


    def __FindData__(self,Data):
        self.temp = self.beforetemp = self.Start
        self.LastMove = "Root"
        while self.temp != None:
                if Data < self.temp.Data:
                    self.beforetemp = self.temp
                    self.temp = self.temp.LeftNode
                    self.LastMove = "Left"
                elif Data > self.temp.Data:
                    self.beforetemp = self.temp
                    self.temp = self.temp.RightNode
                    self.LastMove = "Right"
                else:
                    return True

        return False


    def __GetListOfData__(self,temp):
        if self.choice == '1':
            self.DataList.append(temp.Data)

        if temp.LeftNode != None:
            self.__GetListOfData__(temp=temp.LeftNode)

        if self.choice == '2':
            self.DataList.append(temp.Data)

        if temp.RightNode != None:
            self.__GetListOfData__(temp=temp.RightNode)

        if self.choice == '3':
            self.DataList.append(temp.Data)


    def __SetReferencings__(self,ReferenceToSet):
        if self.LastMove == 'Left':
            self.beforetemp.LeftNode = ReferenceToSet
        elif self.LastMove == 'Right':
            self.beforetemp.RightNode = ReferenceToSet
        elif self.LastMove == 'Root':
            self.Start = ReferenceToSet


    def __PerformDeletion__(self,tempvar):
        if tempvar.LeftNode != None:
            self.__PerformDeletion__(tempvar.LeftNode)
        elif tempvar.RightNode != None:
            self.__PerformDeletion__(tempvar.RightNode)

        del  tempvar


    def __MakeNewSubtree__(self):
        NewStartingPoint = Node(Data = self.DataList[0])

        for Data in self.DataList[1:]:
            NewNode = Node(Data=Data)
            tempvar = beforetempvar = NewStartingPoint
            LastMove = ''

            while tempvar !=None:
                if NewNode.Data < tempvar.Data:
                    beforetempvar = tempvar
                    tempvar=tempvar.LeftNode
                    LastMove = "Left"
                elif NewNode.Data > tempvar.Data:
                    beforetempvar = tempvar
                    tempvar = tempvar.RightNode
                    LastMove = "Right"

            if LastMove == 'Left':
                beforetempvar.LeftNode = NewNode
            elif LastMove == 'Right':
                beforetempvar.RightNode = NewNode

        return NewStartingPoint



    def __Deletion__(self):
        DataToDelete = int(input("\nEnter Data to Delete :: "))
        self.DataList = []
        DataFound = self.__FindData__(Data = DataToDelete)

        if DataFound:
            self.choice = '1'
            self.__GetListOfData__(self.temp)
            print(len(self.DataList))
            self.DataList = self.DataList[1:]

            if len(self.DataList) == 0:
                self.__SetReferencings__(ReferenceToSet = None)

            elif len(self.DataList) < 3:
                self.__PerformDeletion__(tempvar = self.temp)
                NewSubTreeReference = self.__MakeNewSubtree__()
                self.__SetReferencings__(ReferenceToSet = NewSubTreeReference)

            else:
                self.choice = input("\nHow to Insert LeftOver Nodes .....\n\n1. Pre-Order\n2. In-Order\n3. Post-Order\n\nEnter Your Choice :: ")
                if self.choice == '1' or self.choice == '2' or self.choice == '3':
                    self.DataList = []
                    self.__GetListOfData__(temp = self.temp)
                    self.DataList.remove(DataToDelete)
                    self.__PerformDeletion__(tempvar=self.temp)
                    NewSubTreeReference = self.__MakeNewSubtree__()
                    self.__SetReferencings__(ReferenceToSet = NewSubTreeReference)
                else:
                    print("\nWrong Choice.....\n")
                    return
            print("\nData/Node Deleted Successfully!!!...\n")
        else:
            print("\nData Not Found..... Invalid Data Element....\n")


##----- END of this Class -----##


##----- Creating BinarySearchTree/Object of Class BinarySearchTree -----##
TestObject = BinarySearchTree()
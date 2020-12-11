##----- Class to Crate Nodes-----##
class Node:
    def __init__(self,Data=0):
        self.Data = Data
        self.Next = None
        self.Previous = None
##----- END of this Class -----##


##----- Class to Work on DoublyCircularLinkedList-----##
class DoublyCircularLinkedList:
    def __init__(self):
        print("\nDoubly Circular Linked List is all set to work on\n")
        self.Start = self.LastNode = None
        self.choice = 0
        self.Begin = self.Last = None
        input("Hit any Key to Start Operations on DoublyCircularLinkedList.......")
        self.__Menu__()

    def __Menu__(self):
        while True:
            print("\n1. Insertion\n2. Traversion\n3. Deletion\n4. Exit")
            self.choice = input("\nEnter Your Choice : ")
            if self.choice == '1':
                self.__Insertion__()
            elif self.choice == '4':
                exit(0)
            elif self.Begin == None:
                print("\nLinkedList is Empty.... not able to perform this operation......")
            elif self.choice == '2':
                self.__Traversion__()
            elif self.choice == '3':
                self.__Deletion__()
            else:
                print("\nWrong Choice... Choose Again....\n")


    def __Insertion__(self):
        if self.Begin != None:
            self.choice = input(f"1. Insertion before {self.Begin}  ---> First Data Element\n2. Insertion after {self.Last}  ---> Last Data Element\n\nEnter Your Choice : ")
            if self.choice == '1':
                self.__InsertionAtBeginning__()
            elif self.choice == '2':
                self.__InsertionAtLast__()
            else:
                print("\nWrong Choice")

        else:
            self.__InsertionAtBeginning__()


    def __InsertionAtBeginning__(self):
        NewNode = Node()
        NewNode.Next = self.Start
        NewNode.Data = input("Enter Data :: ")

        if self.Begin == None:
            self.Begin = self.Last = NewNode.Data
            self.LastNode = NewNode
            print("\nData Inserted Successfully!!!")
        else:
            self.Begin = NewNode.Data
            self.Start.Previous = NewNode
            print(f"\n{NewNode.Data} Inserted at Beginning Successfully!!")

        self.Start = NewNode
        NewNode.Previous = self.LastNode
        self.LastNode.Next = NewNode



    def __InsertionAtLast__(self):
        NewNode = Node()
        self.LastNode.Next = NewNode
        NewNode.Previous = self.LastNode
        NewNode.Next = self.Start
        self.LastNode = NewNode
        self.Start.Previous = self.LastNode
        NewNode.Data = input("Enter Data :: ")
        self.Last = NewNode.Data
        print(f"\n{NewNode.Data} Inserted at Last Successfully!!")



    def __Traversion__(self):
        self.choice = input("\n1. Simple Traversion\n2. Reverse Traversion\nEnter Your Choice :: ")
        if self.choice == '1':
            temp = self.Start.Next
            print(f"Data Element :: {self.Start.Data}\t\tNode Address :: {id(self.Start)}\t\tP.N.A :: {id(self.Start.Previous)}\t\tN.N.A :: {id(self.Start.Next)}")

        elif self.choice == '2':
            temp = self.LastNode
        else:
            print("\nWrong Choice.......")
            return

        while temp != self.Start:
            print(f"Data Element :: {temp.Data}\t\tNode Address :: {id(temp)}\t\tP.N.A :: {id(temp.Previous)}\t\tN.N.A :: {id(temp.Next)}")
            if self.choice == '1':
                temp = temp.Next
            else:
                temp = temp.Previous

        if self.choice == '2':
            print(f"Data Element :: {temp.Data}\t\tNode Address :: {id(temp)}\t\tP.N.A :: {id(temp.Previous)}\t\tN.N.A :: {id(temp.Next)}")


    def __Refresh_LastNode_And_Data__(self):
        if self.Start == None:
            self.Begin = self.Last = None
            return

        # self.Start.Previous = None
        self.LastNode = self.Start
        while self.LastNode.Next != self.Start:
            self.LastNode = self.LastNode.Next
        self.Last = self.LastNode.Data
        self.Begin = self.Start.Data


    def __Deletion__(self):
        DataToDelete = input("Enter Data Element/Node Address to Delete :: ")

        if DataToDelete == self.Start.Data or DataToDelete == str(id(self.Start)):
            if self.Start == self.Start.Next:
                self.Start = None
            else:
                self.Start = self.Start.Next
                self.Start.Previous = self.LastNode
                self.LastNode.Next = self.Start
            print("\nData/Node Deleted Successfully!!!")
            self.__Refresh_LastNode_And_Data__()
        else:
            before_temp = self.Start
            temp = self.Start.Next
            while temp != self.Start:
                if temp.Data == DataToDelete or DataToDelete == str(id(temp)):
                    before_temp.Next = temp.Next
                    try:
                        temp.Next.Previous = before_temp
                    except:
                        pass
                    del temp
                    print("\nData/Node Deleted Successfully!!!")
                    self.__Refresh_LastNode_And_Data__()
                    return
                before_temp = temp
                temp = temp.Next

            print("\nData Not Found.... Invalid Data Element.....")

##----- END of this Class -----##


##----- Creating LinkedList/Object of Class DoublyCircularLinkedList -----##
TestObject = DoublyCircularLinkedList()
# node class
class Node:
    # default value of data and link is none if no data is passed
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    # method to update the data of the Node
    def updateData(self, data):
        self.data = data

    # method to set Link for the Next Node
    def setLink(self, node):
        self.link = node

    # method returns data stored in the Node
    def getData(self):
        return self.data

    # method returns address of the next Node // goes to the Next Node
    def getNextNode(self):
        return self.link

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # method adds elements to the left of the Linked List
    def addToStart(self, data):     # 21
        # create a temporary node
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode
        if self.tail is None:
            self.tail = self.head

    # method adds elements to the right of the Linked List
    def addToEnd(self, data):   # data = 16
        start = self.head
        if start is None:
            self.addToStart(data)
        else:
            tempNode = Node(data)   # data = 16 : link = None
            while start.getNextNode():
                start = start.getNextNode()
            start.setLink(tempNode)
            del tempNode
            self.tail = start.getNextNode()
        return True

    # method displays Linked List
    def display(self):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False

        while start:
            print(str(start.getData()), end=" ")
            start = start.link
            if start:
                print("-->", end=" ")
        print()

    # method returns length of linked list
    def length(self):
        start = self.head
        size = 0
        while start:     # start != None
            size += 1
            start = start.getNextNode()
        # print(size)
        return size

    # method returns index of the received data
    def index(self, data):
        start = self.head
        position = 1

        while start:
            if start.getData() == data:
                return position
            else:
                position += 1
                start = start.getNextNode()

    # method removes item passed from the Linked List
    def remove(self, item):
        start = self.head
        previous = None
        found = False

        # search element in list
        while not found:
            if start.getData() == item:
                found = True
            else:
                previous = start
                start = start.getNextNode()

        # if previous is None then the data is found at first position
        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setLink(start.getNextNode())
        return found

    # method returns max element from the List
    def Max(self):
        start = self.head
        largest = start.getData()
        while start:
            if largest < start.getData():
                largest = start.getData()
            start = start.getNextNode()
        return largest

    # method returns minimum element of Linked list
    def Min(self):
        start = self.head
        smallest = start.getData()
        while start:
            if smallest > start.getData():
                smallest = start.getData()
            start = start.getNextNode()
        return smallest

    # method pushes element to the Linked List
    def push(self, data):
        self.addToEnd(data)
        return True

        # method removes and returns the last element from the Linked List
    def pop(self):
        start = self.head
        previous = None

        while start.getNextNode():
            previous = start
            start = start.getNextNode()

        if previous is None:
            self.head = None
        else:
            previous.setLink(None)
            data = start.getData()
            del start
            return data

    # method to clear LinkedList
    def clear(self):
        self.head = None
        return True

    # method returns count of Element received
    def count(self, element):
        start = self.head
        count1 = 0
        while start:
            if start.getData() == element:
                count1 += 1
            start = start.getNextNode()
        return count1

    def displayfirst(self, k):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False

        while start and k:
            print(str(start.getData()), end=" ")
            start = start.link
            k -= 1

            if start and k:
                print("-->", end=" ")

        if k != 0:
            print("not enough element")
        else:
            print()


    def push(self, data):
        self.addToEnd(data)
        return True


    def reversenew(self, list_a):
        start = self.head
        while start:
            list_a.addToStart(start.getData())
            start = start.getNextNode()

    def reverse(self):
        prev = None
        now = self.head
        next = None
        while now:
            next = now.link
            now.setLink(prev)
            prev = now
            now = next
        self.head = prev

    # 4. Copy the Linked List
    def copy_list(self, newlist):
        start = self.head
        while start:
            newlist.addToEnd(start.getData())
            start = start.getNextNode()


    def convlist(self):
        start = self.head
        clist = []
        while start:
            clist.append(start.getData())
            start = start.getNextNode()
        print(clist)


    def sorted(self):
        start = self.head
        next_node = start.getNextNode()
        checker = 0

        while next_node:
            if next_node.getData() > start.getData():
                if checker == 0:
                    checker = 1
                elif checker == -1:
                    return False
            elif next_node.getData() < start.getData():
                if checker == 0:
                    checker = -1
                elif checker == 1:
                    return False
            start = next_node
            next_node = next_node.getNextNode()
        return True

    #swap
    def swap(self, x, y):
        prev_node1 = None
        prev_node2 = None
        node1 = self.head
        node2 = self.head

        if self.head is None:
            print("Empty List!!!")
            return False
        if x == y:
            print("Same input")
            return False

        while node1 != 0 and node1.data != x:
            prev_node1 = node1
            node1 = node1.link
        while node2 != 0 and node2.data != y:
            prev_node2 = node2
            node2 = node2.link

        if node1 != 0 and node2 != 0:
            if prev_node1 != 0:
                prev_node1.link = node2
            else:
                self.head = node2

            if prev_node2 != 0:
                prev_node2.link = node1
            else:
                self.head = node1


            temp = node1.link
            node1.link = node2.link
            node2.link = temp
        else:
            print("Swapping is not possible")



# creating LinkedList
myList = LinkedList()
myList1 = LinkedList()
myList2 = LinkedList()

# adding some elements to the start of LinkedList
myList.addToStart(5)
myList.addToStart(4)
myList.addToStart(3)
myList.addToStart(2)
myList.addToStart(1)
# 1 -> 2 -> 3 -> 4 -> 5 -> None


myList.display()


#1st k() element
myList.displayfirst(3)

# push O(1)
myList.push(6)
myList.display()

#reverse
myList.reversenew(myList1)
myList.reverse()
myList1.display()
print()

#copy
print("Copied LL")
myList.copy_list(myList2)
myList2.display()
print()
#convert to list
print("List =")
myList.convlist()
print()
#sorted
print("Is it sorted?")
print(myList.sorted())
print()

#swap
print("Swap")
myList.swap(2, 5)
myList.display()
print(myList.sorted())
print()

# adding some elements to the End of the LinkedList
# myList.addToEnd(12)
# myList.addToEnd(13)
# myList.addToEnd(3)
# myList.display()
# 1 -> 2 -> 3 -> 4 -> 5 -> 13 -> 3 -> 31
# printing Length
# print(myList.length())
#
# # printing index of an element
# print(myList.index(12))
#
# # removing an element
# print(myList.remove(12))
#
# myList.display()
#
# # printing max and min element
# print(myList.Max())
# print(myList.Min())
#
# # pushing and popping elements
# print(myList.push(31))
# myList.display()
# print(myList.pop())
# myList.display()
#
# # printing count of particular element in the List
# print(myList.count(3))
#
# print(myList.clear())
# myList.display()


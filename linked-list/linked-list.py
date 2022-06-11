class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def includes(self, item):
        item = self.head
        if(item.value != item):
            while(item.value != item):
                item = item.next
            return True
        else:
            return True
   
    def insert(self, value):
        Node1 = Node(value)
        Node1.next = self.head
        self.head = Node1

    def toString(self):
        current_v = self.head
        if (current_v != None):
            list = []
            while (current_v != None):
                print("{", current_v.value,end = " } -> ")
                list.append(current_v.value)
                current_v = current_v.next
            print(end = "NULL")
            return list
        else:
            return "Empty list"

if __name__ == '__main__':
    pass

    # ll = LinkedList()
    # ll.insert(1)
    # ll.insert(2)
    # ll.insert(3)
    # ll.insert(4)

    # str(ll.toString())
    # print(ll.head.value)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, data):
        newNode = Node(data)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def prepend(self, x):
        temp = Node(x)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head = temp
        self.length += 1
        return True

    def append(self,x):
        temp = Node(x)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.length += 1
        return True


    def printLL(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next

    def popLL(self):
        if  self.head.next == None:
            self.head = None
            self.tail = None
            self.length = 0
            pop_value = None
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            pop_value = curr.next.data
            curr.next = None
            self.tail = curr
            self.length -= 1
        return pop_value

    def prepopLL(self):
        if self.length == 0:
            return None
        prepop_value = self.head.data
        self.head = self.head.next
        self.length -=1
        return prepop_value

    def size(self):
        return self.length

    def insertLL(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def detectLoop(self):
        h = set()
        curr = self.head
        while curr:
            if curr.data in h:
                return True
            h.add(curr.data)
            curr = curr.next
        return False

    def detectLoopFloyd(self):
        slow = self.head
        fast = slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

L =LinkedList(20)
L.append(4)
L.append(15)
L.append(10)

L.head.next.next.next.next = L.head
print(L.detectLoop())
print(L.detectLoopFloyd())
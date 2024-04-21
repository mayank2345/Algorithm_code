class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next
    print()


def iteRevK(head, k):
    curr = head
    prev,next = None,None
    count = 0
    while curr != None :
        if next != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count +=1


    head.next = curr
    return prev



head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)

printList(head)

head = iteRevK(head, 3)

printList(head)
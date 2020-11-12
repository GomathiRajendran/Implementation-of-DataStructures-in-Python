import SinglyLinkedList

def reverseLinkedList(myLL):
    previous = None
    current = myLL.head
    while(current != None):
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    myLL.head = previous


if __name__ == '__main__':
    myLL = SinglyLinkedList.LinkedList()
    for i in range(10, 0, -1):
        myLL.insertAtStart(i)

    print('Original Linked List:', end = ' ')
    myLL.printLinkedList()
    print()
    print('Reversed Linked List:', end = ' ')
    reverseLinkedList(myLL)
    myLL.printLinkedList()
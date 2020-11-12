import SinglyLinkedList

def findLength(linkedlist):
    count = 0
    temp = linkedlist.head
    while(temp != None):
        count += 1
        temp = temp.next
    return count
   
if __name__ == "__main__":
    
    myLL = SinglyLinkedList.LinkedList()
    for i in range(10):
        myLL.insertAtStart(i)
    myLL.printLinkedList()
    print()
    print('Length:', findLength(myLL))

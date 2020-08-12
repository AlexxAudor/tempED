class Nodo:
    def __init__(self, data = None, next = None):
       self.data = data
       self.next = next
 
class ListaSimple: 
    def __init__(self):
        self.head = None
    

    def addFront(self, data):
        self.head = Nodo(data=data, next=self.head)  
 

    def is_empty(self):
        return self.head == None
 

    def addEnd(self, data):
        if not self.head:
            self.head = Nodo(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Nodo(data=data)

    def deleteNode(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data
 
   
    def printList( self ):
        Nodo = self.head
        while Nodo != None:
            print(Nodo.data, end =" ")
            Nodo = Nodo.next
 
lista = ListaSimple() 
lista.addFront(5) 
lista.addEnd(8) 
lista.addFront(9) 
lista.addEnd(4)

 
lista.printList() 
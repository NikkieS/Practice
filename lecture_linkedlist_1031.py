class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def getLength(self):
        return self.nodeCount

    def popAt(self, pos):
        
        if pos < 1 or pos > self.nodeCount :
            raise IndexError

        else :
            r = self.getAt(pos).data
            # 노드 1개 삭제
            if self.nodeCount == 1 and pos == 1:
                self.head = None
                self.tail = None
            
            # 맨 처음 노드 삭제
            elif pos == 1 :
                self.head = self.head.next
            
            # 맨 끝 노드 삭제
            elif pos == self.nodeCount :
                self.getAt(pos-1).next = None
                self.tail = self.getAt(pos-1)

            # 중간 노드 삭제
            else :
                self.getAt(pos-1).next = self.getAt(pos+1)

            self.nodeCount -= 1
        
        return r
        
    def traverse(self):
        L = []
        curr = self.head
        while curr is not None :
            L.append(curr.data)
            curr = curr.next 
        return L


    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount


def solution(x):
    return 0

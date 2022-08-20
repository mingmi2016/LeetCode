import numpy as np

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def initList(self,data):
        #   创建头节点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        #   逐个为data内的数据创建节点，建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r
    
    def printList(self,head):
        if head == None: return
        node = head
        while node != None:
            print(node.val,end =' ')
            node = node.next

arr = input("please input first linkList:")
num = [int(n) for n in arr.split()]
intss1 = np.array(num)


arr = input("please input second linkList:")
num = [int(n) for n in arr.split()]j
intss2 = np.array(num)

l = LinkList()
l1 = l.initList(intss1)
l2 = l.initList(intss2)



total = 0     #用来存储两个节点的和
next1 = 0     #判断下一位是否要加1

result = 
while l1 != None && l2 != None:
    













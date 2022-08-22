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
num = [int(n) for n in arr.split()]
intss2 = np.array(num)

l = LinkList()
l1 = l.initList(intss1)
l2 = l.initList(intss2)



total = 0     #用来存储两个节点的和
next1 = 0     #判断下一位是否要加1

#这个地方初始化是0，这个节点到最后是用不到的，最后返回的result.next,直接就把这个舍弃了
result = ListNode(0)   #套路，这个result指针是一直不动的，最后返回结果
cur = result    #套路，这个cur是在for循环的时候移动的

while (l1 != None and l2 != None):
    total = l1.val + l2.val +next1 
    cur.next = ListNode(total % 10)
    next1 = total / 10
    l1 = l1.next
    l2 = l2.next
    cur = cur.next

while l1 != None:
    total = l1.val + next1
    cur.next = ListNode(total % 10)
    next1 = total / 10
    l1 = l1.next
    cur = cur.next


while l2 != None:
    total = l2.val + next1
    cur.next = ListNode(total % 10)
    next1 = total / 10
    l2 = l2.next
    cur = cur.next


if next1 != 0:
    cur.next = ListNode(next1)


# return result.next    #这个地方为什么是返回next ???

#直接把链表打印出来

printcur = result.next
while printcur != None:
    print(printcur.val)
    printcur = printcur.next













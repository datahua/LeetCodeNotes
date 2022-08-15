[TOC]

### 1. Find Loop

~~~python
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    first = head.next
    second = head.next.next
    
    while first != second:
        first = first.next
        second = second.next.next
    
    first = head
    while first != second:
        first = first.next
        second = second.next
        
    return first
~~~

策略: first 从 head.next 开始, second 从 head.next.next 开始. 两边相等时, first 变成 head, 同速向前, 碰到为头



### 2. Merge Linked Lists

~~~python
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def merageLinkedLists(headOne, headTwo):
		p1 = headOne
        p1Prev = None
        p2 = headTwo
        while p1 and p2:
            if p1.value < p2.value:
                p1Prev = p1
                p1 = p1.next
            else:
                if p1Prev is not None:
                    p1Prev.next = p2
                p1Prev = p2
                p2 = p2.next
                p1Prev.next = p1
        if p1 is None:
            p1Prev.next = p2
        return headOne if headOne.value < headTwo.value else headTwo
    
	def mergeLinkedLists(headOne, headTwo):
        dummy = cur = LinkedList(0)
        while headOne and headTwo:
            if headOne.value > headTwo.value:
                cur.next = headTwo
                headTwo = headTwo.next
            else:
                cur.next = headOne
                headOne = headOne.next
            cur = cur.next
            
        cur.next = headOne if headOne else headTwo
     	return dummy.next
~~~



### 3. Shift Linked List

~~~python
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = next
        
    def shiftLinkedList(head, k):
        length = 1
        oldTail = head
        while oldTail.next:
            oldTail = oldTail.next
            length +=1
        
        offset = abs(k) % length
        if offset == 0:
            return head
        newTailPos = length - offset if k > 0 else offset
        newTail = head
        for i in range(1, newTailPos):
            newTail = newTail.next
        
        newHead = newTail.next
        newTail.next = None
        oldTail.next = head
        
        return newHead
~~~

- 首先量长度
- 同时得到oldTail
- 算 offset = abs(k) module length
- extreme case offset = 0 -> 直接返回
- 算新的tail的位置 **newTailPos**, 为 length - offset 如果 k 为正数, 否则 offset, newTail = head
- for i in range(i, newTailPos): newTail = newTail.next
- 最后理顺 
- oldTail.next = head 旧尾巴连旧头
- newHead = newTail.next 新头为新尾巴的下一个 (因为链表还是连着的)
- newTail.next = None 断尾巴
- return newTail 返回新头


### 4. LRU Cache

~~~python
class LRUCache:
    def __init__(self, maxSize):
        self.cache = {}
        self.maxSize = maxSize or 1
        self.currentSize = 0
        self.listOfMostRecent = DoublyLinkedList()
    
    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.evictLeastRecent()
            else:
                self.currentSize += 1
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            self.replaceKey(key, value)
        self.updateMostRecent(self.cache[key])
        
    def giveValueFromKey(self, key):
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value
    
    def getMostRecentKey(self):
        if self.listOfMostRecent.head is None:
            return None
        return self.listOfMostRecent.head.key
    
    def evictLeastRecent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]
    
    def updateMostRecent(self, node):
        self.listOfMostRecent.setHeadTo(node)
        
    def replaceKey(self, key, value):
        if key not in self.cache:
            raise Exception("The provided key isn't in the cache!")
        self.cache[key].value = value
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def setHeadTo(self, node):
        if self.head = node:
            return
        
       	elif self.head is None:
            self.head = node
            self.tail = node
        
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
            
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node
            
    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
          	return
       	self.tail = self.tail.prev
        self.tail.next = None
        
class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
       	if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None
~~~



### 5. Rearrange Linked List

~~~python
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def rearrangeLinkedList(head, k):
        # 如果三个都相等会如何? 为何要创建三个链表? 
        # 如果三个都等于, 那只有else那个chunk会被执行, 三个if elif else 都会改变第一个结点的next, 只有else那个最后执行生效, 所以output会是大于的数字
        
        sh = st = LinkedList(None)
        eh = et = LinkedList(None)
        gh = gt = LinkedList(None)
        
        cur = head 
        while cur:
            if cur.value < k:
                st.next = cur
                st = st.next
            elif cur.value == k:
                et.next = cur
                et = et.next
            else:
                gt.next = cur
                gt = gt.next
            cur = cur.next
     	
        st.next = eh.next
        et.next = gh.next
         # 如果不写这个的话, greatTail指向哪里? 指向cur那个结点的后面一个结点
        # 假设 倒数第一个是 负数, 倒数第二个是正数, 当倒数第一被第一条件加到前面后, 倒数第二依然指向他
        # 不用 None 做 next, 就会指到那个数, 而不是结束
        gt.next = None
        return sh.next
~~~



- 先建立三个不同的链表头
- 用cur来遍历原链头
- 小的用small接
- 相等用equal接
- 大的用great接
- 然后小尾巴 -> 中头的下一个
- 中尾巴 -> 大头的下一个
- 范围小头的下一个

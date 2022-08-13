### Linked List

[toc]

### Intro

singly linked list: two memory box, one store data, one stores the location of next memory slot

**Noncontiguous memory** : logical sequence of items are not couped with physical sequence of cells in memory.



### Python Implementation

~~~python
class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = None
class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous
~~~

1. in order to traverse a linkedList, a probe is always needed
2. value None serves as a sentinel that stops the process



### 1. Remove duplicates from linked list

~~~python
def removeDuplicatesFromLinkedList(linkedList):
    cur = linkedList
    while cur and cur.next:
        if cur.value == cur.next.value:
            cur.next = cur.next.next
        else:
            cur = cur.next
	return linkedList

	# sample solution
def removeDuplicatesFromLinkedList(linkedList):
    cur = linkedList
    while cur:
        nextNew = cur.next
        while nextNew is not None and nextNew.value == cur.value:
            nextNew = nextNew.next
		cur.next = nextNew
        cur = cur.next
	return linkedList
~~~



因为要遍历整个linkedList, 所以需要一个dummy

1. 方法一:

while 条件: 当下节点和下个节点存在, 如果当下等于下个节点, 通过改变pointer的方向, 来remove下一个

- 如果要在while中用到cur.next.next, while 条件必须 cur and cur.next 都不是None
- 只有在cur.value != cur.next.value 的时候, 才往前进, 如果相同也前进, 1->1->1->1 这种情况会跳到3号位, 而错过2号位和4号位置的比较

2. 方法二:

- 将cur.next单独列出
- 同样还是要,当下个不是None, 现节点和下个节点值相同时,下个节点往前爬
- 现指针重新指向下个节点
- 现指针往前爬

方法一改变现节点的下个指向, 方法二多了遍历下个节点这一步骤.



### 2. Doublely Linked List Construction

~~~python
# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if not self.tail:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # 1. 首先处理 将 一个结点 从一个结点的链表 加入第一个结点前的情况
        # 2. 其次将结点断链 (用于解决, 要加入的结点是内部结点的情况)
        # 3. 将该结点 前后指针方向给调好
        # 4. 将该结点上一个结点的下指针给调节好 (如果上一个结点为None, 则重新设置头)
        # 5. 将该结点上一个结点的上一个结点定到这个新加入结点
        # 先把加入结点的前后调好, 再调后一个结点的前后, 因为新加入结点的前后, 依赖之前结点的前后
        
        # 如果链表只有一个节点, 且跟要加入的节点是同一个点, 直接return
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        # 将要加入的结点给断链
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        # 处理
        # 为什么这里不用setHead()? 因为setHead调用的也是insertBefore() -> infinite loop
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next=node.next
        nodeToInsert.prev=node
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        # 便利需要dummy 
        node = self.head
        
        # 遍历从1开始
        currentPosition = 1

        # 走到index处
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition +=1

        # node 不是空, 就加到这个前面, 是空就是设置tail
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)
        

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
~~~

setHead(node): 

- 如果空, 设置头尾为node, 返回
- 怎么检查空? 头尾都无
- 如果有, insertBefore(head)



setTail(node)

- 如果空, setHead(node), 返回
- 如果有, insertAfter(tail)



insertBefore(node, nodeToInsert)

- 极端情况: 链表只有一个结点, 这个结点也是nodeToInsert, 直接return, 否则? 也没事似乎
- self.remove(nodeToInsert) 因为有可能要插入的结点是已经存在在链表中的点, 所以需要将这个点移除, 否则可能出现这个结点连接这个结点的情况
- 设置插入的新结点的前后端
- 如果插入点之前是None, 设置成self.head, 不可使用setHead(), 因为setHead()调用了这个函数
- 设置前面那个点的前后



同理

insertAfter(node, nodeToInsert)

- 极端情况, 单结点链表移动仅有结点, 直接return
- remove(nodeToInsert)以防node已经在链表内

- 设置nodeToInsert的前后结点
- 查看是否node.next是None, 是则设置nodeToInsert为self.tail
- 否则设置nodeToInsert.next为node.next
- 最后设置node.next是这个新结点

顺序一定是先将前面那个原先node的next, prev给assign出去之后, 再改变原先node的指向, 不然就丢失



insertAtPosition(position, nodeToInsert):

- 如果位置是1, 就是把头改了, **别忘了return**
- 不然, 设置dummy head开始遍历
- 设置开始位置为1
- 从索引1开始增量, 直到1, while条件为: current不是None and current position 不是position
- 如果node不是空, insertBefore() dummy
- 如果node 空, setTail()



removeNodesWithValue(value)

- 开始dummy 头
- 用dummy有值作为while的条件遍历
- nodeToRemove 作为 node的reference
- node 向前爬
- 值相同则remove nodeToRemove



containsNodeWithValue(value)

- dummy头遍历
- 循环条件为 node 存在 且 node的值不是value
- return 这个node是不是None

remove(node)

- 如果是头, 头变成头的下一个
- 如果是尾, 尾变成尾的上一个
- 如果都不是, removeNodeBindings(node)



removeNodeBindings(node)

- 如果前面有, 前面的下一个是node的下一个
- 如果后面有, 后面的上一个是node的上一个
- node下一个为None
- node上一个为None
- 上一个没有怎么办? 那就是node == head, 在remove中被处理, 同理下一个



### 3. Remove Kth Node From End

~~~python
class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None
        
def removeKthNodeFromEnd(head, k):
    count = 1
    first = second = head
    # F  				  L
    # 0 -> 1 -> 2 -> 3 -> 4
    while counter <= k:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head = head.next
        return
   	while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next
~~~

窗口

first 和 second 中间隔了k, 这样两者同时移动, 当second到None的时候, first就到了倒数第k个

- 第一步,将 second 向前 move 4次
- 检查是否second到None了, 如果second到None了, 说明移动的是第一个
    - 无非常规方法移动第一个, 只能 head 的 value 改成第二个, head 指向 第二个的下一个

- 如果不是None, 则同时移动second和first向前, 但是second到结尾, 不到None, 这样确保first在 被移动的那个node之前
- 将first.next = first.next.next

off-by-one error?

1. 从后面的, 因为后面-1 开始 不是-0开始? 所以count = 1?
2. 还是因为数node数量?
3. len 和 index?



### 4 Sum of Linked Lists

~~~python
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
	def sumOfLinkedLists(linkedListOne, linkedListTwo):
        newLinkedListHeadPointer = LinkedList(0)
        currentNode = newLinkedListHeadPointer
        carry = 0
        
        nodeOne = linkedListOne
        ndoeTwo = linkedListTwo
        
        while nodeOne is not None and nodeTwo is not None or carry != 0:
            valueOne = nodeOne.value if nodeOne is not None else 0
            valueTwo = nodeTwo.value if nodeTwo is not None else 0
            sumOfValues = valueOne + valueTwo + carry
            
            newValue = sumOfValues % 10
            newNode = LinkedList(newValue)
            currentNode.next = newNode
            currentNode = newNode
            
            carry = sumOfValues // 10
            nodeOne = nodeOne.next if nodeOne is not None else None
            nodeTwo = nodeTwo.next if nodeTwo is not None else None
		return newLinkedListHeadPointer.next
~~~

- head, dummy, 一个指, 一个回答
- carry 用来接受余数
- one, two 来 reference linkedListOne linkedListTwo的头
- while条件: 要么 one 有, 要么 two 有, 要么还有余数
- valueOne, valueTwo 接收值 (写细一点, 有就接, 没有就0)
- total += 两个值 + carry
- 创建LinkedList(余数), 用dummy.next 来指
- 10的倍数用carry接
- dummy向前动一个
- one two向前动, 如果有现在有,没有就改成None
- 最后return head.next



### 5. Reverse Linked List

~~~python
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev

def reverseLinkedList(head):
    prev = None
    # 切记不可, prev, head, head.next 因为会先 evalute 右侧, head.next 会变成None, 要考虑assign后, 下一轮的next是不是None.next
    # 好像是从最右边开始计算的
    while head:
        prev, head.next, head = head, prev, head.next
    return prev


	# recursive
def reverseLinkedList(head):
    if not head or not head.next:
        return head
    
    # create an part of the linked list without the head and reverse recursively
    p = reversedLinkedList(head.next)
    head.next.next = head
    head.next = None
    return p
~~~

- 先设置prev为None, 用作将第一个node指向
- while head有值:
    - 用 next 接收原本 head 的 next
    - head.next 指向 prev -> 也就是把第一个开始指向 0, 下一个prev是现在的head
    - prev 为 head, 用作下个指回来
    - head 移动到 head的下一个, 原先refer的
- 最后 return prev 因为最后那一次, head 被变成None了

while 做了什么? 

- head移动到下一个, 
- 现在的head指向前一个, 
- prev用作记录这一个方便下一个head指向

四行是因为, head.next 要被用两次, 先改(断了) 后到, 无法实现 所以用next接收了一个

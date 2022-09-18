# Algorithm Problem Grinding

## Grinding Order: linked List -> Binary Tree -> DFS/BFS(searching) -> dynamic programming -> array -> sort (selection, bubble, quick, merge) -> stack/queue/heap -> graph -> tries -> union find

**comments**

- 8.1.2022:

Let's see to where solving 600 leetcode problems would lead me to!

- 8.10.2022:

I found 10 leetcode problems daily are only do-able if they are all **easy**. So I lower the quota to 5, with meidum and hard level problems ones. 

So, 10 * 10 + 20 * 5 = 200 -> 200 code problems will be solved in August, some of them will be re-do multiple times to ensure the accuracy as accuracy is more important than quantity.

- 8.19.2022:

doing hard questions last two days, will get back to 5 minimum quota tmr

- 9.2.2022:

was moving my place in the last two days, algo dude back

~~~py

# crispy recursive call that connects leaf nodes into a linked List

def connectLeafNodes(currentNode, head=None, previousNode=None):
  if not currentNode:
    return head, previousNode
    
  if isLeafNode(currentNode):
    if previousNode is None:
      head = currentNode
    else:
      previousNode.right = currentNode
    previousNode = currentNode
  leafHead, leftPreviousNode = connectLeafNodes(currentNode.left, head, previousNode)
  return connectLeafNodes(currentNode.right, leftHead, leftPreviousNode)
~~~

- 9.18.2022:

Got an offer of CS master program from Georgia Tech, hard work paid off, took a few days off celebrating it. back today

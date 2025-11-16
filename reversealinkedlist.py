class Node(object):
    def __init__(self,val,next=None):
        self.val = val 
        self.next = next

    def __repr__(self):
        res = str(self.val)
        if self.next:
            res += str(self.next)
        return res

class Solution():
    
    def reverselinkedList3(self,node):
        curr = node
        prev= None
        while curr!=None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr =tmp
        return prev
    
    def reverselinkedUsingStack(self,node):
        stack = []
        prev = None
        curr = node
        while curr!=None:
            stack.append(curr.val)
            curr= curr.next
        
        #head = Node(None)
        #newNode = head
        newNode = Node(None)
        head = newNode
        while len(stack):
            lastnodeval = stack.pop()
            #print(lastnodeval, end='')
            newNode.val= lastnodeval
            prev = newNode
            newNode.next = Node(None)
            newNode = newNode.next


        
        return head
    


node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
#print(node)
#print(Solution().reverselinkedList3(node))
print(Solution().reverselinkedUsingStack(node))
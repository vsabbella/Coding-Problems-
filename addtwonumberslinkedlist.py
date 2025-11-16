class Node(object):
    def __init__(self, val):
        self.val=val
        self.next = None

class Solution:
    def addTwoNumbers(self,l1,l2):
        return self.addTwoNumbersHelperIterative(l1,l2)
        
    
    def addTwoNumbersHelperIterative(self,l1,l2):
        l3= Node(None)
        l3head =l3
        carryover = 0
        while l1!=None or l2!=None:
            l1val=0
            l2val =0
            if(l1.val):
                l1val=l1.val
                l1=l1.next

            if(l2.val):
                l2val =l2.val
                l2=l2.next
            
            #l3.val = carryover
            l3val = l1val+l2val+carryover
            if(l3val>=10):
               l3.val = l3val%10 
               carryover = 1
            else:
                l3.val = l3val
                carryover=0
            l3.next = Node(None)
            l3=l3.next
        if(carryover>0):
            l3.val=Node(1)

        if(not(l3)):
            l3=None
            
        

        return l3head        
        

l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

answer = Solution().addTwoNumbers(l1,l2)
while answer:
    print(answer.val, end='')
    answer=answer.next

print(answer)
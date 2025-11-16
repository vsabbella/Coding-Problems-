class MaxStack(object):
    def __init__(self):
        self.stack = []
        self.maxes = []

    def push(self,val):
        self.stack.append(val)
        if(self.maxes and self.maxes[-1]> val):
            self.maxes.append(self.maxes[-1])
        else:
            self.maxes.append(val)            
         
    def pop(self):
        val = self.stack.pop()
        if(self.maxes):
            self.maxes.pop()
        return val
    
    def max(self):
        return self.maxes[-1]
        
     

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)

print(s.max())
print(s.pop())
print(s.max())
print(s.pop())
print(s.max())
print(s.pop())
print(s.max())
print(s.pop())












# [1,3,2,2,1] , max =  3
#[1,3,2,2]  , max = 3
#[1,3,2,]  , max = 3
#[1,3,]  , max = 3
#[1]  , max = 1
#[1]  , max = 1
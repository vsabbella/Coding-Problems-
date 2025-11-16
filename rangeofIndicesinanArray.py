
class Solution():
    def findrangeofIndices(self, arr, x):
        first = self.binarySearchIterative(arr,x,0,len(arr)-1,True)
        second = self.binarySearchIterative(arr,x,first,len(arr)-1,False)
        return [first,second]
    
    def binarySearchIterative(self, arr,x,low,high,findFirst):
        
        while low<high:
            mid = int((low+high)/2)
            midval = arr[int(mid)]
            if(x == midval):
                return mid
            if(x>midval):
                low=mid+1
            if(x<midval):
                high = mid -1
        return -1


print(Solution().findrangeofIndices([1,3,3,5,6,8,9,9,13] ,9))
    

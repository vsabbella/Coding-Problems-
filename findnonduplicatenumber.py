class Solution(object):
    def findNonDupe_hashmapSol(self,input):
        elementCount = {}
        for num in input:
            elementCount[num] = elementCount.get(num,0)+1

        for key in elementCount.keys():
            value = elementCount.get(key)
            if(value == 1):
                return key
        return 0
    
    def findNonDupe_xor(self,input):
        unique = 0
        for num in input:
            unique ^= num
        
        return unique
    
input = [2,3,3,2,5,8,5,1,8]
print(Solution().findNonDupe_hashmapSol(input))
print(Solution().findNonDupe_xor(input))
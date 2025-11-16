class Solution():
    def reconstructQueue(self,arr):
        arr.sort(key= lambda x:(-x[0],x[1])
                 )
        response =[]
        for pair in arr:
            response.insert(pair[1],pair)
        return response







input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
#print(Solution().reconstructQueue(input))


class SolutionTester():
    def arraySortTest(self,input):
        input.sort(key=lambda x:-x[0])
   
            
        return input

input = [[7, 0], [4, 4], [7, 1], [5, 2], [6, 1], [5, 0]]
response =   SolutionTester().arraySortTest(input)
#esponse.insert(1,2)
print(response)    
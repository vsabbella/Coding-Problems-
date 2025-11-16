import heapq
import collections
class Solution(object):
    def topKFrequentElements(self, nums, k):
        count = collections.defaultdict(int)
        
        for n in nums:
            count[n] += 1

        #{(1:3), (2:2), (3:1} 
        
        heap = []
        for n,c in count.items():
            heap.append((-c,n))

        heapq.heapify(heap)
        #print(heap)    

        result =[]
        result.append(heapq.heappop(heap)[1])
        result.append(heapq.heappop(heap)[1])
        return result
        
   




print(Solution().topKFrequentElements([1,1,1,2,2,3],2))
#[1,2]
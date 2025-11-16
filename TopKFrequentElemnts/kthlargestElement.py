import heapq
def findKthLargest(nums,k):
    return sorted(nums)[len(nums)-k]

def findKthLargest2(nums,k):
    return print(heapq.nlargest(k,nums)[-1])



print(findKthLargest2([3, 5, 2, 4, 6, 8], 3))
# 5









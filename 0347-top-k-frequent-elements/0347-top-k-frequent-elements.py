import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for key in counter: 
            heap.append((counter[key], key))    
        return [y for (x, y) in heapq.nlargest(k, heap)]



        
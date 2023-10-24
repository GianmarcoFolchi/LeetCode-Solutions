class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        freqMap = {}
        result = " "
        for character in s: 
            freqMap[character] = freqMap.get(character, 0) + 1
            
        for (character, frequency) in freqMap.items(): 
            heapq.heappush(heap, [-frequency, character])

        while len(heap) >= 1: 
            if result[-1] == heap[0][1]:
                if len(heap) == 1:
                    return ""
                mostFreq = heapq.heappop(heap)
                secondMostFreq = heapq.heappop(heap)
                result += secondMostFreq[1]
                secondMostFreq[0] += 1 
                heapq.heappush(heap, mostFreq)
                if secondMostFreq[0] != 0:
                    heapq.heappush(heap, secondMostFreq)
                continue
            result += heap[0][1]
            topElement = heapq.heappop(heap)
            topElement[0] += 1
            if topElement[0] != 0:
                heapq.heappush(heap, topElement)

        return result[1:] if len(result) - 1 == len(s) else ""
            
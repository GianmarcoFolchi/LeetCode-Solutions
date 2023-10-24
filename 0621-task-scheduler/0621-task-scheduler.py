class Solution:
    def leastInterval(self, tasks: List[str], cooldown: int) -> int:
        taskCounter = Counter(tasks)
        #add all elements to the heap 
        heap = []
        queue = deque() #(freq, tasks, scheduledTime)
        time = 0 
        for (task, freq) in taskCounter.items(): 
            heapq.heappush(heap, [-freq, task])
            
        while len(heap) > 0 or len(queue) > 0:
            if queue and queue[0][2] == time: 
                heapq.heappush(heap, queue.popleft()[:2])
            if len(heap) > 0:
                itemToProcess = heapq.heappop(heap)
                itemToProcess[0] += 1
                itemToProcess.append(time + cooldown + 1)
                if itemToProcess[0] != 0:
                    queue.append(itemToProcess)
            time += 1
        
        return time
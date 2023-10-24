class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[a, b] for a, b in zip(position, speed)]
        pairs.sort(key = lambda x:-x[0])
        stack = [float("-inf")]
        carFleets = len(position)
        for (pos, carSpeed) in pairs: 
            timeOfArrival = (target - pos) / carSpeed
            if stack[-1] >= timeOfArrival: 
                carFleets -= 1 
            else: 
                stack.append(timeOfArrival)
            
        return carFleets
        
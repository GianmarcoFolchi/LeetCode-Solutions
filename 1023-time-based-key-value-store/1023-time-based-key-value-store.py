from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.timeMap: dict(str, list([int, str])) = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        timeArr = self.timeMap[key]
        result = ""
        if not timeArr: 
            return result
        return binarySearch(timeArr, timestamp)


def binarySearch(arr, timestamp): 
    left, right = 0, len(arr) - 1
    closest = ""
    while left <= right: 
        middle = (left + right) // 2
        if arr[middle][0] > timestamp: 
            right = middle - 1
        elif arr[middle][0] < timestamp: 
            closest = arr[middle][1]
            left = middle + 1
        else: 
            closest = arr[middle][1]
            break

    return closest



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
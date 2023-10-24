class UndergroundSystem:

    def __init__(self):
        self.openTrips: dict[int, list] = {} #id: [t, stationName]
        self.stationAdjList: dict[tuple[str, str], list[int]] = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.openTrips[id] = [t, stationName]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.openTrips: 
            return
        startTime, startStationName = self.openTrips[id]
        del self.openTrips[id]
        if (startStationName, stationName) not in self.stationAdjList: 
            self.stationAdjList[(startStationName, stationName)] = [0, 0]
            
        self.stationAdjList[(startStationName, stationName)][0] += (t - startTime)
        self.stationAdjList[(startStationName, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.stationAdjList: 
            return -1
        averageTime = self.stationAdjList[(startStation, endStation)][0] / self.stationAdjList[(startStation, endStation)][1]
        return averageTime

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
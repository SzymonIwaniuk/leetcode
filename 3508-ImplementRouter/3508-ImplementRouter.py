from collections import deque, defaultdict
import bisect

class Router:

    def __init__(self, memoryLimit: int):
        self.limit_of_packets = memoryLimit
        self.number_of_packets = 0
        self.packet_queue = deque()
        self.packet_set = set()
        self.dest_map = defaultdict(list)


    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.packet_set:
            return False
        
        self.packet_set.add((source, destination, timestamp))

        if self.number_of_packets < self.limit_of_packets:
            self.number_of_packets += 1
        
        else:
            packet = self.packet_queue.popleft()
            self.packet_set.remove(tuple(packet))

            idx = bisect.bisect_left(self.dest_map[packet[1]], packet[2])
            if idx < len(self.dest_map[packet[1]]) and self.dest_map[packet[1]][idx] == packet[2]:
                self.dest_map[packet[1]].pop(idx)

        self.packet_queue.append([source, destination, timestamp])
        self.dest_map[destination].append(timestamp)
        return True


    def forwardPacket(self) -> List[int]:
        if self.number_of_packets > 0:
            self.number_of_packets -= 1
            packet = self.packet_queue.popleft()
            self.packet_set.remove(tuple(packet))

            idx = bisect.bisect_left(self.dest_map[packet[1]], packet[2])
            if idx < len(self.dest_map[packet[1]]) and self.dest_map[packet[1]][idx] == packet[2]:
                self.dest_map[packet[1]].pop(idx)

            return packet
        
        else:
            return []


    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.dest_map[destination]
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)

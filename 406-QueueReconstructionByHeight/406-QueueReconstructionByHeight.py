class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))
        que = []

        for p in people:
            que.insert(p[1], p)
        
        return que

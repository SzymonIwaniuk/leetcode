class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        m = len(players)
        n = len(trainers)
        p = t = 0
        matches = 0

        while p < m and t < n:
            if players[p] <= trainers[t]:
                p += 1
                matches += 1
            t += 1

        return matches

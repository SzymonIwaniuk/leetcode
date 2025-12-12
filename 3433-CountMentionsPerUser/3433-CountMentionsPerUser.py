from typing import List


def handler(
    event: str,
    timestamp: int,
    details: List[str],
    times: List[int],
    mentions: List[int],
    numberOfUsers: int
    ) -> None:
    
    for i in range(numberOfUsers):
        times[i] = max(times[i], timestamp)

    if event == "MESSAGE":
        if details[0] == "ALL":
            for i in range(numberOfUsers):
                mentions[i] += 1

        elif details[0] == "HERE":
            for i in range(numberOfUsers):
                if times[i] == timestamp:
                    mentions[i] += 1

        else:
            for uid in details:
                uid = int(uid)
                mentions[uid] += 1

    else:
        times[int(details[0])] = timestamp + 60 


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        times = [0] * numberOfUsers
        mentions = [0] * numberOfUsers
        events = list(map(lambda x: [x[0], x[1], x[2].replace("id", "").split()], events))
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))

        for event, timestamp, details in events:
            handler(event, int(timestamp), details, times, mentions, numberOfUsers)
        
        return mentions

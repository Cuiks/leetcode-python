from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_len = len(rooms)
        if rooms_len == 0:
            return False
        keys = rooms[0]
        has_done = [0]
        while keys:
            key = keys.pop()
            if key not in has_done:
                has_done.append(key)
            new_keys = rooms[key]
            for new_key in new_keys:
                if new_key in has_done:
                    continue
                keys.append(new_key)
        if len(has_done) == rooms_len:
            return True
        return False


roos = [[1,1],[]]

print(Solution().canVisitAllRooms(rooms=roos))

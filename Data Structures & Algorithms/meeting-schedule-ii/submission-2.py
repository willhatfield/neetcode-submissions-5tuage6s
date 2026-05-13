"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)
        rooms = []

        for meeting in intervals:
            foundHome = False
            for room in rooms:
                good = True

                for time in room:
                    if meeting.start < time.end:
                        good = False
                        
                
                if good:
                    room.append(meeting)
                    foundHome = True
                    break
                
            
            if not foundHome:
                rooms.append([meeting])
                    
        return len(rooms)
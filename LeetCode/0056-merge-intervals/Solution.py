class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        '''
        intervals = [[1,3],[2,6],[8,10],[15,18]]
                        |    |
                           |
                         [1,6]
        
        sort intervals
        Take two intervals
        Check if the first element of the second interval is less than the second element of first element
        If yes merge and append to answer 
        if not append both intervals to res
        '''
        if len(intervals) == 1:
            return intervals

        s_arr = sorted(intervals)
        res = [s_arr[0]]

        i = 1
        while i < len(intervals):
            prev = res[-1]
            cur = s_arr[i]
            print(prev[1], cur[0])

            if prev[1] >= cur[0]:
                res[-1] = [prev[0],max(cur[1],prev[1])]
                i+=1
            else:
                res.append(cur)
                i+=1

        return res

            
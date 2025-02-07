#https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/?envType=daily-question&envId=2025-02-07

from typing import List

Queries = List[List[int]]
Result = List[int]

test_limit = 4
test_queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
answer = [1,2,2,3,4]

from typing import List

Queries = List[List[int]]
Result = List[int]

class Solution:



    def queryResults(self, limit: int, queries: Queries) -> Result:

        ball_colors = [-1] * (limit + 1)

        distinct_colors = set()

        result = []
        print(
            f"{'Idx':<5} | {'Ball Colors':<20} | {'Pos':<3} | {'Col':<3} | {'Distinct Colors':<15} | {'Result':<20}")

        for idx,(position, color) in enumerate(queries, start =1):
            # If the ball in position was uncolored (-1), add the color to the distinct_colors set
            if ball_colors[position] == -1:
                distinct_colors.add(color)
            else:
                # If the ball in position was already colored (>0), remove that color from the set and assign new color
                distinct_colors.discard(ball_colors[position])
                distinct_colors.add(color)

            # Update the color at position and append the color to the ball_colors list
            ball_colors[position] = color
            result.append(len(distinct_colors))
            print(f"{idx:05} | {str(ball_colors):<20} | {position:3} | {color:3} | {str(distinct_colors):<15} | {str(result):<20}")

        return result




if __name__ == '__main__':
    s = Solution()
    print(s.queryResults(test_limit, test_queries))


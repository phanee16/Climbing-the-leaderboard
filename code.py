#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    # Remove duplicates from ranked scores and sort in descending order
    unique_scores = sorted(set(ranked), reverse=True)
    n = len(unique_scores)
    result = []
    j = n-1  # Index of the last score in ranked
    for p in player:
        # Move the index j to the position of the score that is greater than or equal to p
        while j >= 0 and p >= unique_scores[j]:
            j -= 1
        # Append the ranking of p to the result
        result.append(j+2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# Climbing-the-leaderboard (Source = Hackerrank)
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
Example

<img width="204" alt="image" src="https://user-images.githubusercontent.com/47351536/225627852-77a9a6d8-fb67-44f2-8eab-3abe05f8594b.png">


The ranked players will have ranks 1,2 , 2 and 3, respectively. If the player's scores are 70, 80  and 105, their rankings after each game are 4th,3rd  and 1st. Return [4,3,1].

Function Description

Complete the climbingLeaderboard function in the editor below.

climbingLeaderboard has the following parameter(s):

int ranked[n]: the leaderboard scores
int player[m]: the player's scores
Returns

int[m]: the player's rank after each new score
Input Format

The first line contains an integer n, the number of players on the leaderboard.
The next line contains n space-separated integers ranked[i], the leaderboard scores in decreasing order.
The next line contains an integer, m, the number games the player plays.
The last line contains m space-separated integers player[j], the game scores.

Constraints

<img width="410" alt="image" src="https://user-images.githubusercontent.com/47351536/225628802-dd7e2565-7289-465a-a99b-33388a7e21de.png">
Subtask
<img width="223" alt="image" src="https://user-images.githubusercontent.com/47351536/225628892-d07654ca-4ca0-407c-aad1-4ded5236d098.png">


Sample Input :

<img width="842" alt="image" src="https://user-images.githubusercontent.com/47351536/225629122-0d601e61-850b-4b5e-8e74-0db9032792d1.png">

Sample Output : 
<img width="62" alt="image" src="https://user-images.githubusercontent.com/47351536/225629324-eed5e815-f0fe-4a04-a034-baee5c3765fa.png">


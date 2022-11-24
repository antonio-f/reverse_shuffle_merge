# HackerRank's "Reverse Shuffle Merge" problem

This [problem](https://www.hackerrank.com/challenges/reverse-shuffle-merge/problem) is classified as *advanced*, but - in my opinion - it is not so difficult once you realize how to determine the substring A. 

## Example 1
Consider the string "aacbdcbd" and the respective positions

aacbdcbd<br>
87654321 .

To find the substring A, we start moving from position 1, from right to left, in search of the smallest letter in a lexicographic order, which is "a". Then, begin to sweep from position 1, we first encounter "a" at position 7. We cannot form a four letter string because other letters "b", "c" and "d" are not ahead of "a" - they come first in positions from 1 to 6.

So let's try again from the start with "b", the second in lexicographic order; all the remaining letters "a", "c" and "d" are ahead of it. Proceeding right to left, it is easy to see that we can form 

bcda<br>
2347

which is the smallest lexicographically ordered example we can get from the original string. Since the remaining letters are interspersed with "bcda", they constitute necessarily shuffle(A).
So A = "bcda", rev(A) = "adcb", shuffle(A) = "acbd".

## Example 2
As another example, consider the string

xwxyzywz<br>
87654321

and begin to look for "w". It is in position 2, now try for "x"... the first occurrence is in 6 and the string ends. Hence, let's try with "y": an occurrence is in 3. For the same reason as before "x" cannot be included now, but z in position 4 will. Finally, the smallest string A is "wyzx".

## Implementation notes
Obviously, we can start with any letter and drop it when we encounter a smaller one, provided that there is another occurrence of the dropped one further ahead to form the substring A.

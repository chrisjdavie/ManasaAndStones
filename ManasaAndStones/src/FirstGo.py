'''
Solving the Manasa and Stones hackerrank puzzle

https://www.hackerrank.com/challenges/manasa-and-stones

-----------------

Problem Statement

Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. She starts following the trail and notices that two consecutive stones have a difference of either a or b. Legend has it that there is a treasure trove at the end of the trail and if Manasa can guess the value of the last stone, the treasure would be hers. Given that the number on the first stone was 0, find all the possible values for the number on the last stone.

Note: The numbers on the stones are in increasing order.

Input Format 
The first line contains an integer T, i.e. the number of test cases. T test cases follow; each has 3 lines. The first line contains n (the number of stones). The second line contains a, and the third line contains b.

Output Format 
Space-separated list of numbers which are the possible values of the last stone in increasing order.

Constraints 
1<=T<=10 
1<=n,a,b<=103

-----------------

Find the lowest and highest values - (n-1)*a, (n-1)*b (a lowest, b highest).
Find the smallest change if you swapped 1 stone (b-a).
You'd add that each time a stone was swapped.

(unless a == b, then there's only one answer, (n-1)*a

Created on 30 Dec 2015

@author: chris
'''

for _ in range( input() ):
    n = input()-1
    a = input()
    b = input()
    if a != b:
        abMin = min([a,b])
        abMax = max([a,b])
        opList = map(str, range(n*abMin, n*abMax + 1, abMax - abMin))
        print ' '.join(opList)
    else:
        print n*a
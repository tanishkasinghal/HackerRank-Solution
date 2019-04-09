'''
Task
Given an integer,n, perform the following conditional actions:

If is odd, print Weird
If is even and in the inclusive range of to, print Not Weird
If is even and in the inclusive range of to, print Weird
If is even and greater than, print Not Weird

Input Format

A single line containing a positive integer,n.

Constraints
1<=n<=100

Output Format
Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3

Sample Output 0

Weird

Explanation 0
n is odd and odd numbers are weird, so we print Weird.

Sample Input 1

24

Sample Output 1

Not Weird

Explanation 1

n=24
n>20 and is even, so it isn't weird. Thus, we print Not Weird.
'''
n = int(input())
if n%2!=0:
    print("Weird")
else:
    if 2<=n<=5 or n>20:
        print("Not Weird")
    else:
        print("Weird")

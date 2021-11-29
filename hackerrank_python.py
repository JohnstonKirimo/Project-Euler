#Function to check leap year
def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True
    else:
        leap = False

    return leap

#Program to print integers in one line without using string methods
from __future__ import print_function

N = int(input())
print(*range(1,N+1), sep='')

#or
# Enter your code here. Read input from STDIN. Print output to STDOUT
print reduce(lambda x, y: x+y, map(lambda x: str(x+1), range(int(input()))))

print ''.join(str(x+1) for x in range(input()))

Input  = input()
Answer = ''

for i in range(1,Input+1):
    Answer += str(i)

print Answer


#Happiness Change

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = [int(x) for x in input().split()]

array = [int(x) for x in input().split()]
A = {int(x) for x in input().split()}
B = {int(x) for x in input().split()}

happiness = 0

for value in array:
    change = 1 if value in A else -1 if value in B else 0
    happiness += change

print(happiness)

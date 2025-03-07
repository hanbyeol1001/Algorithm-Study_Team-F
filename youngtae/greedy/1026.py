# S의 값을 가장 작게 만들기 위해 A의 수 재배열
# B에 있는 수는 재배열 x
# S의 최솟값 출력

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse= True)
B.sort()

answer = 0
for x, y in zip(A,B):
    answer += x * y
    
print(answer)
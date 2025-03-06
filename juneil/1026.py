import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True) # A의 배열을 마음대로 바꿀 수 있기 때문에 최소값을 얻으려면 하나는 오름차순, 하나는 내림차순으로 정렬하면 된다!
ans = 0
for i in range(N):
    ans += A[i]*B[i]
print(ans)
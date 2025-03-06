import sys

input = sys.stdin.readline
N = int(input())

# DP배열 정의. DP[n]은 n킬로그램을 만들기 위한 최소 봉지 수이다.
# 불가능한 경우는 -1이다
DP = [-1 for i in range(5001)] 
DP[3] = 1
DP[5] = 1

for i in range(5, N+1):
    if DP[i-3] != -1:
        DP[i] = DP[i-3]+1
    
    if DP[i-5] != -1:
        if DP[i] == -1:
            DP[i] = DP[i-5]+1
        else:
            DP[i] = min(DP[i], DP[i-5]+1)

print(DP[N])
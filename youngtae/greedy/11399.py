# 1번부터 N번까지 각 사람이 돈 인출시간 다름
# 모두 인출하는데 필요한 시간의 합 최솟값 출력
# 제일 오래걸리는사람을 뒤로 보내기

# 1번 풀이 O(N^2)
import sys
input = sys.stdin.readline

N = int(input()) # 사람의 수 입력
P_list = list(map(int, input().split())) # 인출 시간 리스트 입력

P_list.sort() # 오름차순 정렬 (그리디 전략 적용)
sum_time = 0
for i in range(1, len(P_list) + 1):
    sum_time += sum(P_list[:i]) # 현재까지 기다린 총 시간 합산

print(sum_time)


# 2번 풀이 O(NlogN)
import sys
input = sys.stdin.readline

N = int(input())  
P_list = list(map(int, input().split()))

P_list.sort()  # 오름차순 정렬

sum_time = 0
prefix_sum = 0  # 이전까지의 합 저장

for p in P_list:
    prefix_sum += p  # 현재 사람의 인출 시간 더하기
    sum_time += prefix_sum  # 총 대기 시간 누적

print(sum_time)
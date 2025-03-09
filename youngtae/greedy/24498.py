# 처음과 마지막이 아닌 탑 하나 선택, 인접한 탑 높이 모두 1 이상이어야함
# 인접한 두 탑 높이 1씩 감소
# 선택한 탑 높이 1 증가
# 가장 큰 탑 높이 구하기
# 인접한 것들 중 최솟값을 선택한 탑에 더한게 최고 높이
# 처음부터 끝까지 돌고 max값을 출력

import sys
input = sys.stdin.readline

N = int(input())
tower_heights = list(map(int, input().split()))

max_height = max(tower_heights) # 반례를 고려하여 초깃값을 처음 탑높이 최댓값으로 설정
for i, height in enumerate(tower_heights): # 탑을 돌면서 각 탑 별 최대높이를 측정
    if i > 0 and i < N - 1:
        # 좌우 탑 높이 중 작은 값을 선택한 탑에 선택한 탑의 높이를 더한값과 현재 max_height와 비교하여 만들 수 있는 최대 탑 높이 저장
        max_height = max(max_height, height + min(tower_heights[i-1], tower_heights[i+1])) 

print(max_height)


# 반례 => 6 1 2 3 2 6 -> 최대 높이 6인데 만들어서 할 수 있는건 최대 5 
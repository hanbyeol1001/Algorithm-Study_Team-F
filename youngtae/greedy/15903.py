# 서로 다른 값을 가진 카드 두장 골라서 합함
# 합한 값을 기존 카드 두장의 값에 덮어씀
# m번 합체후 n장의 카드 모두 합한 값이 놀이의 점수
# 점수 최솟값 출력하기
# 숫자중에 가장 작은 두개의 수를 합치는 것이 최선의 방법
# 합칠 때마다 정렬을 하고 작은것 두개를 합친다

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
card_nums = list(map(int, input().split()))

for _ in range(m):                  # m번 합체
    card_nums.sort()                # 오름차순으로 정렬
    sum_num = sum(card_nums[:2])    # 작은 것 두개 합하기
    card_nums[0] = sum_num          # 합한 값으로 덮어씌우기
    card_nums[1] = sum_num

print(sum(card_nums)) 
    

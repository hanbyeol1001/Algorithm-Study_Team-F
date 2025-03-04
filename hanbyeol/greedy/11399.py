n = int(input())
time = list(map(int, input().split()))

time.sort()  # 대기 시간을 최소화하기 위해 오름차순 정렬

answer = 0
total = 0  # 누적합을 저장할 변수

for t in time:
    total += t  # 현재 사람이 기다려야 하는 시간
    answer += total  # 누적합을 결과에 더함

print(answer)
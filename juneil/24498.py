N = int(input())
tops = list(map(int, input().split()))

ans = max(tops) # 행동을 수행할 수 없는 N<3인 경우에 대해 처리하기위한 초기화

# 주어진 행동을 생각해보면 기준이 되는 탑의 최대 크기는 자기 자신과 양 옆의 탑의 크기중 더 작은 탑의 크기로 결정됨을 알 수 있다
# 더 옆에 있는 탑들을 이용해 기준탑 양옆의 탑의 크기를 키우면 안되는가? 생각해보면 기준탑 양옆의 탑의 크기를 키우기 위해서는 기준탑의 크기가 줄어들어야함을 알 수 있다
for i in range(1, N-1):
    ans = max(ans, min(tops[i-1], tops[i+1])+tops[i])
print(ans)
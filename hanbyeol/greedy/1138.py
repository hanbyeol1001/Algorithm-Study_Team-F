'''
N명의 사람들은 매일 아침 한 줄로 선다. 
사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억한다. 
N명의 사람이 있고, 사람들의 키는 1부터 N까지 모두 다르다.

각 사람들이 기억하는 정보가 주어질 때, 줄을 어떻게 서야 하는지 출력하는 프로그램을 작성하시오.
'''


def func(N, info):
    '''
    주어진 리스트의 원소를 반대 순서로 가지고 와서
    각각의 위치를 그 바로 결정하여 줄을 세운다.
    '''
    line = []
    for i in range(N, 0, -1):
        line.insert(info[i-1], i)
    return line


if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))

    answer = func(n, heights)
    print(*answer)
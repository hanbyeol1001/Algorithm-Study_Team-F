'''
길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.
S = A[0] * B[0] + ... + A[N-1] * B[N-1]
S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

S의 최솟값을 출력하는 프로그램을 작성하시오.
'''


def func(N, A, B):
    '''
    S의 최솟값만 출력하면 되므로, 정렬할 필요는 없다.
    A와 B를 각각 내림차순, 오름차순 한 뒤 S를 구하면 된다.
    '''
    A.sort()
    B.sort(reverse=True)

    S = 0

    for i in range(N):
        S += A[i]*B[i]

    return S


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s = func(n, a, b)
    
    print(s)
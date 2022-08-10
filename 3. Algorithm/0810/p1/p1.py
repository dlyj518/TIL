# 5×5 배열에 무작위로 25개 숫자로 초기화한 후
# 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절댓값을 구하시오.
# 예를 들어 7 값의 이웃한 값은 2,6,8,12이며 차의 절댓값의 합은 12이다.

import sys
sys.stdin=open('input.txt')

#절댓값 함수
def abbs(x):
    return x if x>0 else -x

# test case t
t = int(input())

# 상하좌우 위한 배열 di, dj
di = [0,0,-1,1]
dj = [-1,1,0,0]

for tc in range(1, t+1):
    # 행렬 크기 n
    n = int(input())
    # 행렬 arr
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 합산 s
    s = 0
    # 각 좌표마다 반복
    for i in range(n):
        for j in range(n):
            # 상하좌우이므로 4번 반복
            for k in range(4):
                # 상하좌우 중 하나 한 칸 이동한 좌표
                ni = i + di[k]
                nj = j + dj[k]
                # 범위 내 있는 지 확인
                if 0 <= ni < n and 0 <= nj < n:
                    s += abbs(arr[ni][nj] - arr[i][j])
    print(f'#{tc} {s}')
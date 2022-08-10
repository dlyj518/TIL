import sys
sys.stdin = open('input.txt')

# 테스트 케이스 10개
for tc in range(10):
    # 테스트 케이스 번호 n
    n = int(input())
    # 행렬 arr, 크기는 100×100으로 고정이니 range(100)
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 최고 합 저장할 maxsum 저장
    maxsum = 0
    # 행의 합 출력
    for i in range(100):
        s = sum(arr[i])
        if maxsum < s : maxsum = s
    # 열의 합 출력
    for j in range(100):
        s = sum([arr[a][j] for a in range(100)])
        if maxsum < s: maxsum = s
    # 우하단으로 내려가는 대각선 합
    # arr[k][k]로 구한 뒤 합산
    s = 0
    for k in range(100):
        s += arr[k][k]
    if maxsum < s: maxsum = s
    # 좌하단으로 내려가는 대각선 합
    # arr[k][n-k-1]로 구한 뒤 합산
    s = 0
    for k in range(100):
        s += arr[k][n-k-1]
    if maxsum < s: maxsum = s
    # 출력
    print(f'#{n} {maxsum}')
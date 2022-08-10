import sys
sys.stdin=open('input.txt')

# test case t
t = int(input())

# 우하좌상 위한 배열 di, dj
di = [0,1,0,-1]
dj = [1,0,-1,0]

for tc in range(1, t+1):
    # 행렬 크기 n
    n = int(input())
    # 변경횟수 cnt, 방향전환용 변수 dn 저장
    cnt, dn = 1, 0
    # 현재 위치 i, j 저장
    i, j = 0, 0
    # n×n 집합 구현
    arr = [[0]*n for _ in range(n)]
    # 첫 위치에 1 저장
    arr[0][0] = 1
    # n×n을 다 채울 때 = cnt가 n×n=n²일 때 멈추는 반복문
    while cnt < n**2:
        # cnt 추가
        cnt += 1
        # 이동과정을 위한 while문
        while 1:
            # 방향이동
            # 해당 방향이 집합 안이고 이미 다른 숫자로 안채워졌다면 이동
            if 0 <= i+di[dn] < n and 0<= j+dj[dn] < n and arr[i+di[dn]][j+dj[dn]] == 0:
                i, j = i+di[dn], j+dj[dn]
                break
            # 그렇지 않다면 dn을 바꿔서 방향전환
            # % 4 를 통해서 0~3에서만 바뀌도록
            else: dn = (dn+1)%4
        # 이동한 위치에 번호 넣기
        arr[i][j] = cnt
    # 출력
    # test case 먼저
    print(f'#{tc}')
    # 원소별로 불러온 뒤 줄바꿈 대신 스페이스로
    for x in range(n):
        for y in range(n):
            print(arr[x][y], end=' ')
        # 한 행 끝나면 줄바꿈
        print()
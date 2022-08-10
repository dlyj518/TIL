# 부분집합 합 구하기
# 10개의 정수를 받아 부분집합의 합이 0이 되는 것이 존재하는지 계산하는 함수를 작성

import sys
sys.stdin=open('input.txt')

# test case t
t = int(input())

# 반복
for tc in range(1, t+1):
    # 결과값 저장용 rst(ReSulT)
    rst = 0
    # array 저장
    arr = list(map(int, input().split()))
    # array 길이 n으로 저장
    n = len(arr)
    # 부분집합 구하기
    # 2ⁿ가지 경우 구현, 0은 공집합이니 제외
    for i in range(1,1<<n):
        # 부분집합 합 저장용 s 저장
        s = 0
        for j in range(n):
            # 부분집합 요소 찾기
            if i & (1<<j) :
                # 요소이면 s에 추가
                s += arr[j]
        # 부분집합의 합이 0이면 rst를 1로 변경
        if s == 0 : rst = 1; break
    print(f'#{tc} {rst}')
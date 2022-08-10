import sys
sys.stdin = open('input.txt')

N = int(input())

for tc in range(1, N+1):
    line_number = int(input()) # N개의 라인 수

    # 버스 노선 나타내는 빈 이중리스트 [[1, 2, 3], [2, 3, 4, 5]] 등으로 나타나게
    bus_road = []
    for i in range(1, line_number+1):
        A, B = map(int, input().split())
        # 이중리스트에 담긴위한 빈 리스트
        road = []
        # for문을 range(A, B+1)로 버스 노선의 범위만큼 지정
        for k in range(A, B+1):
            road.append(k) # road 빈 리스트에 한개의 버스 노선을 담고
        bus_road.append(road) # 담은 한개의 버스노선을 큰 리스트에 담음


    P = int(input()) # 정수 P개 값 입력받고
    result = [0] * 5001 # C값이 5000일때를 대비해서 넉넉하게..
    for j in range(1, P+1): # P개 만큼 for문 돌릴 수있게 range 정함
        C = int(input()) # C값을 P개 만큼 입력받음

        for l in range(len(bus_road)): # 버스노선 개수만큼 for문 돌리면서
            if C in bus_road[l]: # 입력받은 C값이 bus_road(버스 노선표) 안에 있으면
                result[C] += 1 # 카운트 올려줌
    print(result)
    remove_set = {0} # 구글링해온 모든 0 제거 방법
    result = [m for m in result if m not in remove_set]

    result_last = ' '.join(map(str, result)) # 문자열로 공백으로 묶어줌
    print(f'#{tc} {result_last}')
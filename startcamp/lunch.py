#점심메뉴 3개의 문자를 menu라는 변수에 담기

menu = ['짜장', '짬뽕', '유산슬']
print(menu)
for _ in range(2):
    i=int(input())
    map=[list(list(map(int,input()))) for _ in range(i)]
    print(map)
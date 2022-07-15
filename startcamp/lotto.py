import requests

#1. lotto api로부터 데이터 받아오기
#2. 지난주 당첨번호 알아내기(1등)
#3. random module이 가지고 있는 sample이라는 함수를 사용하여
#   1~45 중 무작위 6개 뽑기
#4. 그 번호가 당첨번호와 일치하는지 확인
#5. 1000번 이상 새로운 번호를 생성하여 매번 당첨이 되었는지 확인하는 로직 생성
#6. 1~2등 포함한 4등까지 각 당첨횟수 출력하기

#1.
url='https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1023'
response = requests.get(url).json()

#2.
print('지난주 1등 당첨번호는 '+str(response['drwtNo1'])+','+str(response['drwtNo2'])+','+
str(response['drwtNo3'])+','+str(response['drwtNo4'])+','+str(response['drwtNo5'])+','+
str(response['drwtNo6'])+', 보너스번호는 '+str(response['bnusNo'])+'입니다.')

#3.
from random import sample
sp=sample(range(1,46),6)
print(sp)

#4.
ltt=[response['drwtNo1'],response['drwtNo2'],response['drwtNo3'],response['drwtNo4'],response['drwtNo5'],response['drwtNo6']]
cnt=0
for i in range(6):
	for j in range(6):
		if sp[i]==ltt[j]: cnt+=1
print(cnt)

#5,6.
tcnt=[]
nn=50000
for n in range(nn):
    cnt=0
    sp=sample(range(1,46),6)
    for i in range(6):
        for j in range(6):
            if sp[i]==ltt[j]: cnt+=1
    if cnt==5 and sp.count(response['bnusNo'])==1:cnt+=0.5
    tcnt.append(cnt)
dc=[tcnt.count(6),tcnt.count(5.5),tcnt.count(5),tcnt.count(4)]
print('총 '+str(nn)+'번 중 1등은 '+str(dc[0])+'번, 2등은 '+str(dc[1])+'번, 3등은 '+str(dc[2])+'번, 4등은 '+str(dc[3])+'번 당첨되었습니다.')
# CLI INTRO

## 각종 명령어들

### 파일 생성

> ```bash
> $ touch {파일명}
> ```

### 파일 목록

> ```bash
> $ls
> -a : 상위폴더/숨겨진 파일
> -l : 생성날짜/작성자 등 자세한 정보
> ```

### 파일 실행

> ```bash
> $ start {파일명}
> ```

### 파일 경로 확인

> ``` bash
> $ pwd
> ```

### 경로 만들기

> ```bash
> $ mkdir 파일명
> ```

### 경로 바꾸기

> ```bash
> $ cd {경로}
> ./ : 현재 폴더
> ../ : 상위 폴더
> ```

### 폴더 만들기

> ```bash
> mkdir {폴더명}
> ```

###  파일 삭제

> ```bash
> $ rm {파일명}
> -r : 폴더 지우기
> -rf : 폴더 강제로 완전삭제(비권장)
> ```

### 

#### 온라인 실습실

- 당일 5시 시작, 당일 제출
- 온라인 제출`

#### 깃랩

- pdf repo
- 그 주 금요일까지
- 월~목 각각 화화목목에 풀이

 

### Git

#### Repository

특정 디렉토리를 버전 관리하는 저장소

- git init 명령어로 로컬 저장소 생성
- .git 디렉토리에서 관련 정보 있음
- git status : 현재 상태



- Working Directory : 실제 디렉토리, 현재 작업중인 곳
- Staging Area : commit으로 남기고 싶은 곳
- Repository : commit들이 저장되는 곳
- `git add` : Working Directory > Staging Area, tracked됨
- `git commit` : Staging Area > Repository
- Staging Area가 있는 이유 : commit 버전 관리하기 위함



- git add '~~.py'
- git config --global user.email "이메일"
- git config --global user.name "이름"
- git commit -m "SC Day2 | python intro"
  - 로컬에 저장



- git log : 로그 보기
- git log --oneline

앞에 나오는 이상한 문자열 : 고유번호 / oneline도 고유값

- rm : 삭제



- git push

- 새 repository 만들기

- ```git
  git remote add origin https://github.com/dlyj518/TIL.git
  # 원격저장소 origin 추가
  git push -u origin master
  # commit 있는걸 origin에 추가(로컬에 저장하는게 아닌 공유장소에 업로드)
  git remote -v
  리모트
  ```

- 
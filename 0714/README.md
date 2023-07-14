# 7월 14일의 기록

## 깃 허브를 쓰자
~~멍청이의 기록~~

### 깃허브 실행하는법
---

+ git config --global user.name name      : 유저 이름 설정
+ git config --global user.email email    : 유저 이메일 설정
* git config --global -l                  : 유저 확인

    해서 설정을 한다

  1.  그다음에 **git init**으로 깃을 실행함
  2.  그리고 file을 **git add .** 으로 현재 디렉토리의 모든 폴더&파일 워킹디렉토리에서 스테이징 에어리어로 추가함
  3.  **git status**로 상태 확인가능
  4.  스테이징 에어리어에서 **git commit -m '커밋명'** 으로 로컬 레포지터리에 커밋함
  5.  그리고 깃허브에 올리면 됨
  6.  **git log**로 확인

### 깃허브에 올리는법
---

 1. 깃허브에 리모트 레포지터리 생성함
 2. 깃허브 리모트 레포지터리 url 복사해옴
 3. **git remote add origin URL붙여넣기**
 4. **git push -u origin master** 입력
 5. 올라감 
    - 만약 pull하려면 **git pull origin master**
  
  

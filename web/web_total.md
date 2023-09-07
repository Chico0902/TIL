# web 정리

## 01 fundamentals

### 1. html basic

- ! + tab을 하면 기본 구조가 생긴다
- 소문자가 기본
- <div>는 블록요소, 레이아웃 계층 나누기 용도
- <p> 도 블록요소, 문자 단락 용도
- <span>은 inline요소(span태그는 div,p를 하위태그로 포함 못시킴)
- <a> 도 inline요소(문서를 링크시키기 위해 사용하는 태그, 주로 href랑 사용)
  - *인라인요소*가 머냐?
  - 태그안에 적힌 문자정보의 길이만큼만 영역을 차지한다.
- div -> p -> span 순서대로 포함 가능
- 자동완성이 매우 훌륭하게 되어있다.

### 2. text structure
- <h1> 제목같은거
- <h2> 소제목같은거
- 마크다운이 이거 기반이라 비슷함
- 리스트같은거만들때 ul>li*3하면 자동으로 만들어줌!
- 잡다한 기능 있는데 스타일에서 하는게 맞는듯?

### 3. css selectors
- css는 스타일을 만드는건가보다
- <head> 안에다가 <style> 해서 <body>의 스타일을 지정
- *{} 하면 전체에 대해서
- <h1> <p> 이런거처럼 원래 있는 애들은 그냥 h1{}하면 됨
- 앞에 .붙여야하는 애들은 class 임
  - 클래스는 내가 만드는거
  - <body>에서 <div class="bronze"> 이런식으로 하면 그 div는 브론즈 클래스인거다
- 앞에 #붙여야하는건 id애들
  - id도 내가 설정하는건데 한번만쓸 애들은 id 써주면된다
  - 근데 많이는 안쓴다고 한다

### 4. specificity
- 클래스에 여러개 넣으면 스타일에서 뒤에 적은게 적용됨
- 우선순위가 높은 순
 1. importance
 2. inline 스타일
 3. 선택자
    - id 선택자 > class 선택자 > 요소선택자
 4. 소스코드순서

### 5. inheritance
- 상속받는게 있고 안받는게 있음
- 상속받는것도 안받을 수 있고 안받는것도 받을 수 있음.


## 02 box-model
  
  ### 1. part of box
  - 박스의 기본 요소
    - <style> 넣고
        .box1 {
          width: 200px;
          padding-left: 25px;
          padding-bottom: 25px;
          border-width: 3px;
          border-color: black;
          border-style: solid;
          margin-left: 25px;
          margin-bottom: 50px;
              }
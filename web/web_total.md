# web 정리

## 01 fundamentals

### 1. html basic

- ! + tab을 하면 기본 구조가 생긴다
- 소문자가 기본
```
- <div>는 블록요소, 레이아웃 계층 나누기 용도
- <p> 도 블록요소, 문자 단락 용도
- <span>은 inline요소(span태그는 div,p를 하위태그로 포함 못시킴)
- <a> 도 inline요소(문서를 링크시키기 위해 사용하는 태그, 주로 href랑 사용)
  - *인라인요소*가 머냐?
  - 태그안에 적힌 문자정보의 길이만큼만 영역을 차지한다.
- div -> p -> span 순서대로 포함 가능
- 자동완성이 매우 훌륭하게 되어있다.
```

### 2. text structure
```
- <h1> 제목같은거(진우가 헤더래)
- <h2> 소제목같은거(헤더 크기조절이래)
- 마크다운이 이거 기반이라 비슷함
- 리스트같은거만들때 ul>li*3하면 자동으로 만들어줌!
- 잡다한 기능 있는데 스타일에서 하는게 맞는듯?
```
### 3. css selectors
```
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
```

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
   ```
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
      </style>
  ```
   
  ```
    - <body>에 <div class="box1">box1</div>넣으면 끝
  ```
  ### 2. box-sizing
    - 박스의 크기를 어떤것을 기준으로 생성할지 정하는 속성
    - box-sizing 안에는 content-box, border-box 있음 
    - 우리가 박스 만드는거 기준으로 하려면 border-box로 설정하세용
    ```
    <div class="box content-box">content-box</div>
    ```
    - 클래스는 여러개 선언 가능
    - 겹치는거면 나중게 되는데 안겹치면 다 적용됨

  ### 3. block-inline

    - block 요소는 기본적으로 부모 요소의 너비 100%를 차지하며, 자식 콘텐츠의 최대 높이를 취함.
    - block 요소의 총 너비 및 높이는 content + padding + border width/height임.
    - inline 요소는 자체 콘텐츠의 너비와 높이만 차지가능(width,height 속성 지정 불가)
    - 이미지는 인라인이지만 width나 height로 크기변경 가능
    - inline 요소 크기 제어하려면 block으로 변경하거나 inline-block 요소로 설정해야함.
  
  ### 4. inline-block

    - inline-block은 컨텐츠 길이만큼 블록으로 만듬
    - 그래서 width도 주고 height도 주고 할수잇음
  
  ### 5. none

    - display : none 하면 아예 출력을 안함 자리도 차지안함
    - 그냥 세상에서 사라지는거임

## 03 layout-position

  ### 1. position

  - 포지션을 정해줌
  - static 이 기본
  - absloute는 절대값으로 줌 근데 자리차지안함.(그림위에 글 넣을때 주로 씀) 
  - relative 는 자기자리 기준으로 움직임
    - 릴레이티브랑 앱솔이랑 섞어서는 잘 안쓴대
 
  ### 2. 스티키

  - 스태틱 속성과 픽스드 속성을 둘다 가지고 있는것
  ```css
      .sticky {
      position: sticky;
      top: 0;
      background-color: lightblue;
      padding: 20px;
      border: 2px solid black;
      }
  ```
  - 이렇게 씀
  - 이렇게쓰면 top이 0이 되면 스태틱에서 픽스드로 바뀌는것

  ### 3. absolute

  - 이게 뭘까?
  
  ### 4. z-index

  - z 는 3차원 축
  - z index가 크면 맨 위로 올라옴

## 04 layout-flexible

  ### 1. flexbox

  -
# 1026_JS

## 일상속의 이벤트
- 진우에게 인사하는 것
- 근영이에게 맞는 것
- 컴퓨터를 켜는 것
  
## 웹에서의 이벤트
- 버튼을 클릭 했을 때 팝업 창이 출력되는 것
- 마우스 커서의 위치에 따라 드래그 앤 드롭하는 것
- 사용자의 키보드 입력 값에 따라 새로운 요소를 생성하는 것
- 일상에서의 이벤트 처럼 웹에서도 <span style="color:salmon">이벤트를 통해 특정 동작을 수행 </span>

## 이벤트
- 무언가 일어났다는 신호, 사건
- **-> 모든 DOM 요소는 이러한 이벤트를 만들어 냄**

- DOM 요소는 event를 받고 받은 event 를 처리<span style="color:salmon">(event handler)</span> 할 수 있음

### event handler
- 이벤트가 발생했을 때 실행되는 함수
- **-> 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것**

#### .addEventListener()
- 대표적인 이벤트 핸들러
  - **특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출**
![img1](image/image1.png)
- type
  - 수신할 이벤트 이름
  - 문자열로 작성(ex.'click')
#### .addEventListener(type,handler)
- handler
  - 발생한 이벤트 객체를 수신하는 콜백 함수
  - 콜백 함수는 발생한 Event object를 유일한 매배견수로 받음

#### addEventListener의 콜백 함수특징
- 발생한 이벤트를 나타내는 Event 객체를 유일한 매개변수로 받음
- 아무것도 반환하지 않음

### 버블링
- 핸들러는 form 요소에 할당되어 있지만 div 나 p요소같은 중첩된 요소를 클릭해도 동작함
- 왜 div나 p를 클릭했는데 form 에 할당된 핸들러가 동작할까?
- 한 요소에 이벤트가 발생하면 이 요소에 할당된 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현상
- 가장 최상단의 조상요소를 만날 때까지 이 과정이 반복되면서 요소 각각에 할당된 핸들러가 동작
- **-> 이벤트가 제일 깊은 곳에 있는 요소에서 시작해 부모 요소를 거슬러 올라가며 발생하는 것이 마치 물속 거품과 닮아서** 

### 'target' & 'currentTarget'
- 'target'속성
  - 이벤트가 발생한 가장 안쪽의 요소(target)를 참조하는 속성
  - 실제 이벤트가 시작된 target 요소
  - 버블링이 진앻되어도 변하지 않음
- 'currentTarget' 속성
  - 현재요소
  - 항상 이벤트 핸들러가 연결된 요소만을 참조하는 속성
  - 'this'와 같음
![img2](image/image2.png)
![img3](image/image3.png)
![img4](image/image4.png)
![img5](image/image5.png)


### 'currentTarget' 주의사항
![img6](image/image6.png)
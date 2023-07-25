url 주소를 브라우저로 입력해서 요청.


import requests

url = 'https://fakestoreapi.com/carts'
response = requests.get(url)
print(response.json())

API =  클라이언트가 원하는 기능으 ㄹ수행하기 위해서 서버측에 만들어 놓은 프로그램
 - 기능예시 : 데이터 저장, 조회, 수정, 삭제 등등

서버측에 특정 주소로 요청이 오면 정해진 기능[[ 주소로 요청을 보냄]

날씨정보를 수집하기 위해서는 2가지 찾아야함
날씨정보를 가지고있는 서버
해당서버가 제공하는 Api

외부에서 무료로 개방된 API
서버가 견디지 못할 경우 정상적인 서비스 이용 불가


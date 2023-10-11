# Databse

> SSAFY 10기 Databse 과정 라이브 강의 코드

| 진행일 | 주제                    |
| ------ | ----------------------- |
| 10/10  | SQL  |
| 10/11  | Many to one relationships 1 |
| 10/12 | Many to one relationships 2 |
| 10/16 | Many to many relationships 1 |
| 10/17 | Many to many relationships 2 |

## 데이터베이스 역할

데이터를 저장하고 조작
- 어떻게 데이터를 저장?(구조적 저장)

### 관계형 데이터베이스

- 테이블, 행, 열의 정보를 구조화하는 방식
- 서로 관련된 데이터 포인터를 저장하고 이에 대한 액세스를 제공
- 기본 키가 있어야 다른 테이블에서 정보를 식별 가능.
  - 이름으로 쓰면 동명이인으로 인해 어려움 겪음.
### 관계형 데이터베이스 관련 키워드
  - 테이블 
  - 필드
    -각 필드에는 고유한 데이터 형식이 지정됨
  - 레코드
    - 각 레코드에는 구체적인 데이터 값이 저장됨
  - 데이터베이스
    - 테이블의 집합
  - 기본 키
    - 각 레코드의 고유한 값
    - 관계형 데이터베이스에서 레코드의 식별자로 활용
  - 외래 키
    - 테이블의 필드 중 다른 레코드를 식별할 수 있는 키
    - 다른 테이블의 기본 키를 참조

## RDBMS 서비스 종류

  - SQlite, MySQL

## DBMS


# SQL
- 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
- 관계형 데이터베이스와의 대화를 위해 사용하는 언어

## SQL Syntax
- SQL 키워드는 대소문자를 구분하지 않음
  - but 대문자 작성 권장
- 각 SQL Statements의 끝에는 세미콜론이 필요
  
## SQL Statements
- SQL을 구성하는 가장 기본적인 코드 블록

### SQL Statements의 4가지 유형
1. DDL
   - 데이터의 기본 구조 및 형식 변경
2. DQL
   - 데이터 검색
3. DML
   - 데이터 조작
4. DCL
   - 데이터 및 작업에 대한 사용자 권한 제어


### Syntax

* Distinct syntax
* WhERE  syntax
    - IN Operator
      - 값이 특정 목록 안에 있는지 확인
    - LIKE Operator
      - 값이 특정 패턴에 일치하는 지 확인
    - Wildcard Characters
        1. '%' 0개 이상의 문자열과 일치하는지 확인
        2. '_' 단일 문자와 일차히지 확인
    - LIMIT clause
      - 조회하는 레코드 수를 제한

## Grouping Data

- Group by 는 disti





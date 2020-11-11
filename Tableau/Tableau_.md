# 태블로





- 추출 연결
  - 데이터를 캡처하는 방식으로 진행
  - 장점
    - 빠른 처리 속도
    - 모든 종류의 태블로 기능 사용 가능
  - 단점
    - (상대적으로) 느린 업데이트 주기





- 눈에 잘 보이는 바 차트 만들기
  - 불필요한 필드 레이블 숨기기
  - 축 머리글 표시 해제 후 레이블 직접 붙이기
  - 불필요한 참조선 없애기
  - 0이 되는 기준선 표시하기
  - (필요에 따라) 불투명도 설정을 통해 색상 톤 다운
  - (필요에 따라) 짙은 색상의 테두리 활용

![image](https://user-images.githubusercontent.com/58559786/97824097-5d72af00-1cfe-11eb-85d9-03bce1163319.png)



![image](https://user-images.githubusercontent.com/58559786/97824413-2e107200-1cff-11eb-8e8d-0006b91da911.png)



![image](https://user-images.githubusercontent.com/58559786/97824731-12599b80-1d00-11eb-9023-3fd4ece6ee18.png)

![image](https://user-images.githubusercontent.com/58559786/97825151-3b2e6080-1d01-11eb-8064-aaad03069b24.png)

- 라인 차트와 영역 차트의 가장 중요한 차이 : Stack or Not
- Category를 색상 부분에 드래그앤드랍으로 끌어서 이동시켜주면 해당 그래프처럼 표현이 가능하다.





- 아래와 같이 마크 누적 설정과 해체를 통해 영역표시의 표현을 다르게 설정할 수 있다.

![image](https://user-images.githubusercontent.com/58559786/97825097-1639ed80-1d01-11eb-9553-a28594756231.png)





- bar chart를 비율로 표현하는데 100% 기준으로 보고싶다면

![image](https://user-images.githubusercontent.com/58559786/98314990-7e971080-201a-11eb-8778-3ebf21b216a5.png)

![image](https://user-images.githubusercontent.com/58559786/98315221-15fc6380-201b-11eb-82a7-86551c269ef8.png)

- 위와 같이 특정 차원에서 지역을 제거해주면 100% 기준으로 모두 볼 수 있다.



- 파이차트의 약점은 각도로 크기를 표시하기 때문에 눈에 잘 들어오지 않는다.

  파이 차트의 대안으로 제시할 수 있는것이 위의 비율 바 차트이다.

- 퀵 테이블 계산을 활용하면 쉽게 만들 수 있다.



- 

![image](https://user-images.githubusercontent.com/58559786/98331847-c9c41a00-2040-11eb-8152-d1e8232bff38.png)





![image](https://user-images.githubusercontent.com/58559786/98331914-ef512380-2040-11eb-9c42-50ceb1a45c67.png)

- 위와 같이 제품을 기준으로 만들어 우리에게 어떤 제품이 수익을 주는지 그리고 손해를 입히는지 쉽게 찾아낼 수 있다.





![image](https://user-images.githubusercontent.com/58559786/98332060-4b1bac80-2041-11eb-9e85-57621b3455f7.png)

- 위 사진의 표시한 부분처럼 대강의 추세선 역시 표현할 수 있다.

![image-20201106150556460](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201106150556460.png)

- 추세선은 이처럼 간단한 설명도 확인할 수 있다.





![image](https://user-images.githubusercontent.com/58559786/98332727-8e2a4f80-2042-11eb-8cac-047822bb681a.png)

![image](https://user-images.githubusercontent.com/58559786/98332808-bb76fd80-2042-11eb-9343-81e6d7483a98.png)

- 구간 차원의 값을 정해줌으로써 표현하는 범위를 설정할 수 있다.



![image](https://user-images.githubusercontent.com/58559786/98333917-1c073a00-2045-11eb-823b-f2c1d8045a3d.png)











- 트리맵의 단점

  - 넓이로 그 크기를 인지하는 것이 직관적으로 다가오지 않음
  - 공간 활용에서의 비효율성

  ![image](https://user-images.githubusercontent.com/58559786/98334220-c2533f80-2045-11eb-9318-ee9acee66dc4.png)



- 버블차트 역시 트리맵의 단점과 비슷하다.

![image](https://user-images.githubusercontent.com/58559786/98334288-e6168580-2045-11eb-82f4-5ab249eaeefa.png)





- 차원과 측정값
  - https://vizlab.tistory.com/33





- 필터
  - 추출 필터
    - 데이터 원본 소스에서 데이터의 일부분만 추출하고 싶을 때
  - 데이터 원본 필터
    - 작업을 위한 데이터 중 일부만을 워크스페이스로 불러올 때
  - 컨텍스트 필터
  - 차원 필터
  - 측정값 필터
  - 테이블 계산 필터
  - 숨기기

- 이중축의 세 가지 용도

  - 이중축의 의미에 충실한 기본 사용법

    강조 포인트 제공

    디자인 효과 또는 컨텍스트 부여

  - 이중 축 만드는 방법

    - 방법 1 : 두번째 측정값을 화면 오른쪽으로 점신이 보일 때까지 끌기

    ![image](https://user-images.githubusercontent.com/58559786/98783356-c532a380-243c-11eb-8b26-9aeb002bc412.png)

    ![image](https://user-images.githubusercontent.com/58559786/98783431-e2677200-243c-11eb-9aba-6a89b82abbdd.png)

    - 방법 2 : 두번째 측정값 우클릭 -> 이중축

  - 이중축을 설정하면 마크가 각각 설정이 가능하다

    - 마크에서 모양을 막대로 바꾸면 흔히 보는 비교막대그래프
    - 막대에서 크기를 조절해 더 시각적으로 보여줄 수 있다.

  - 보통 이중축을 처음 설정하면 양쪽에 모두 축이 존재하는데 이럴 경우 오른쪽 측정값 축 우클릭 -> 축 동기화 선택 을 해주면 하나의 축으로 표현이 가능하다.

    축 동기화를 할 때 두 측정값의 분포 범위를 고려해야 한다.

  ![image](https://user-images.githubusercontent.com/58559786/98783962-b26c9e80-243d-11eb-8fd7-70e2e359de15.png)

  - 이중축을 설정할 때 기축에 넣을 수 있다(CAC)

  ![image](https://user-images.githubusercontent.com/58559786/98784278-39ba1200-243e-11eb-9537-c70b95a305fc.png)

  - 이 상태롬 만들면 열에 측정값 이름이 존재하는데 해당 값을 ctrl키를 누른채로 복사하여 마크카드 색상위로 올리면 시각적으로 보기 편해진다.

  - CAC의 강점은 아직 이중축을 사용하지 않았다는 것!

    - 더 시각적인 표현이 가능하다.

  - 강조하는 의미에서의 이중축

    ![image](https://user-images.githubusercontent.com/58559786/98785247-a681dc00-243f-11eb-9f02-481ceb7222d5.png)

    - 해당 그래프에서 가장 높은값을 점으로 찍어 강조하고 싶을 때

    - `IIF([Order Date]>=DATE('2018-11-01') AND [Order Date] <= DATE('2018-11-30'), [Sales], NULL)`

      이러한 식으로 해당 포인트를 행에 알약을 추가한 뒤 이중축을 설정하면 된다.

  - 실제 작업해보기

    ![image](https://user-images.githubusercontent.com/58559786/98785734-6707bf80-2440-11eb-8a8e-8f73d4a96fc4.png)

    - Sales를 행으로 두고 Order Date를 연속형 월별로 행으로 설정한 뒤
    - `IIF([Category]='Technology', [Sales], NULL)` 의 식으로 새로운 알약을 만들어 Technology 카테고리를 강조하고자 한다.
    - Sales의 색을 회색계통으로 설정한 뒤 불투명하게 만들어 시각적으로 약하게 만들고 Technology의 색을 붉은 계통으로 설정하면 위의 이미지처럼 강조가 가능하다.



- 분석

  - 분석창 : 화면을 만든 후에 +@를 첨가할 수 있는 기능 모음
  - 상수라인 : 사용자가 설정한 특정한 값을 화면에 표시
    - 목표치 라인 설정 등 다양한 목적으로 설정 가능	

  - 평균 라인
    - 셀 : 카테고리 각 항목 하나 하나/ 테이블 : 화면 전체 / 패널 : 셀과 테이블 중간
    - 평균 라인 우클릭 -> 편집 -> 레이블 -> 사용자 지정 -> <계산> = <값>
  - 한 화면에서 평균 라인은 1개, 상수 라인은 2개 이상 포함 가능

  ![image](https://user-images.githubusercontent.com/58559786/98792860-7986f680-244a-11eb-99ad-55943a2e42d6.png)

  - 상수 및 평균 라인을 활용하면, 화면에 컨텍스트와 스토리를 더할 수 있다.
  - 총계
    - 행과 열의 총계를 볼 수 있다
    - 분석 탭에서 설정하면 총계의 출력 위치를 설정할 수 있다.

  ![image](https://user-images.githubusercontent.com/58559786/98801507-3a11d780-2455-11eb-9496-83c898e55b5b.png)

  - 예측
    - 태블로의 예측 기법 : 지수 평활법(Exponential Smoothing)
    - 예측 라인 위에서 우클릭 -> 예측 -> 예측 옵션 에서 여러가지 설정이 가능하다.
    - 예측 라인 위에서 우클릭->예측->예측 옵션 -> 다음 기간 무시 -> 지난 0
  - 클러스터링
    - 머신러닝의 클러스터링과 같은 알고리즘
  - 참조선



- 지도

  - 시도 및 시군구 화면 만들기

    - 필드 앞의 문자열을 의미하는 ABC 기호 클릭
    - 제일 아래쪽 지리적 역할
    - 시/도 또는 시군구. 필드에 맞게 선택
    - 마크에 자동이 아닌 지도를 선택하면  지도에 맞게 표현된다.

  - 불확실한 부분은 화면 오른쪽 아래 [알수없음]이 표현된다

    - 보통 잘못된 이름이거나 동시에 2개 이상의 위치가 존재할 때 알 수 없음이 표시된다.

    - 이러한 경우에는 단계를 나누면 된다
      - ex) 고성군은 강원도 고성과 경상남도 고성 둘 다 존재한다.
      - 시도를 먼저 넣은 후 시군구를 넣으면 된다.
      - 필드 계층구조 만들기
        - 하나의 필드를 잡아서 계층을 만들 필드 위로 올린다.
        - 박스가 보일 때 마우스 클릭 놓기
        - 계층 만들기 창에서 계층 이름 설정

  - 지역 필드에 지리적 역할 부여하기
    - 필드 앞 abc 문자열 선택
    - 제일 아래쪽 지리적 역할 선택
    - 만들기 원본 -> 시도 선택
  - 데이터 집계 결과를 면적을 가진 지도 위에 표현하기 때문에 왜곡 가능성이 존재한다.

- 계산된 필드

  - 계산된 필드 만들기로 보통 생성된다

  - `SUM([Sales]) + SUM([Profit])` 이러한 방식으로 생성한 뒤 이름을 설정해준다.

  - sum을 붙여서 계산하는 이유는 집계(sum)가 먼저 이루어지고, 그 다음에 계산이 이루어져야 한다.

  - 주석 표현 => //

  - `IF SUM([Sales]) >= 100000 THEN 'High' ELSE 'Low' END`

    `IF SUM([Sales]) >= 100000 THEN 'High' END`

    `IIF(SUM([Sales])>=100000, 'High', 'Low')`

    `SUM([Sales]) >= 100000`			<- 이러한 방식은 True/False 방식으로 해결(속도가 더 빠르다.)

  - 만약 조건이 2가지가 아닌 3가지 이상일 경우

    `IF SUM([Sales]) >= 100000 THEN 'High' ELSEIF SUM([Sales]) >= 50000 THEN 'Middle' ELSE 'Low' END`

    위와 같이 ELSEIF로 조건을 설정해준다.




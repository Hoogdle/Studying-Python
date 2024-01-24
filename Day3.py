### DAY3 ###

## {Namespaces - 이름공간}

# X = 2023 
# 2023 == int instance
# X == '변수'

# 작동방법
# 1. '2023' 이라는 int instance 생성 (Dynamic Programming)
# 2. 'X' 변수 생성
# 3. 'X'변수를 '2023' 이라는 int instance 와 연결

# Namespace
# 일종의 테이블
# '변수의 이름' 과 '객체의 메모리주소'를 정리한 테이블
# 변수가 추가될 때마다 객체의 Count up

# X = 2023
# Y = X
# in Namespace,
# X 는 2023의 메모리주소를 가짐
# Y는 X의 객체가 가지는 메모리 주소를 가짐
# ==> X와 Y의 메모리 주소는 같음
# ==> 2023's count == 2 #동일한 메모리주소를 2개의 변수가 가리킴

# X = 2024 
# ==> X와 Y의 메모리주소가 달라짐
# X 는 2024의 메모리 주소 Y는 2023 메모리주소
# 2023,2024's count == 1

# X = 2023
# Y = X
# print(hex(id(X))) #0x238d523a0b0
# print(hex(id(Y))) #0x238d523a0b0
# print(X is Y)  #True #is 는 '메모리 주소'를 비교할 때 사용

# X = 2024
# print(hex(id(X))) #0x238d5520110
# print(hex(id(Y))) #0x238d523a0b0
# print(X is Y) #False

# Y = 2024?
# 2024's count == 2
# 2023's count == 0
# Counter == 0 
# ==> Garbage Collector가 잡아먹음

## Quiz

# X와 Y는 서로 다른 객체이다. 이유를 설명해라.
# X = [100,200,300]
# Y = [100,200,300]
# print(X is Y) 

## {내장함수}
# ex) print(), type(), id(), hex(), len()


## {변수}

# 변수 Rule
# 1. 숫자로 시작 X
# 2. 소문자로만 만든다.(암묵적 룰)
# 3. 키워드 사용불가
# 4. '_'로 시작가능.
# 5. 최대한 자세한 단어 사용

# 같은 데이터를 여러번 사용 => 변수 지정

#2:04:33
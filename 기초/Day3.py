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
# print(id(X)) #3027983055504
# print(id(Y)) #3027983055504
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


# Mutable vs Immutable
# 수정 O : List, Dictionary(key는 수정불가)
# 수정 X : Numbers, Str, Tuple, Set
# Mutable 객체 : 각각 다른 메모리에 저장됨
# Immutable 객체 : 값이 같다면 동일한 메모리에 저장

# X = 'hello'
# Y = 'hello'
# print(X is Y) #True

# X = (100,200,300)
# Y = (100,200,300)
# print(X is Y) #True

# X = {'kim':300}
# Y = {'kim':300}
# print(X is Y) #False

# X = [100,200,300]
# Y = [100,200,300]
# print(X is Y) #False

## Quiz

# X와 Y는 서로 다른 객체이다. 이유를 설명해라.
# X = [100,200,300]
# Y = [100,200,300]
# print(X is Y) 

# Answer
# : int instance의 값은 같고 객체를 공유하지만 
# : list instance가 서로 다른 영역에 생성되므로 서로 다른 객체이다


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

## {Memory and Referencing}

# Shared Reference

# list1 = [100,200,300]
# int class가 100,200,300 instance 생성
# list class가 list instance 생성
# list instance에 100,200,300 각각의 메모리 주소 저장
# 100,200,300 의 counter == 1
# 변수와 객체 연결, list1과 list instance mapping
# list instance counter == 1

# list2 = list1
# list2 변수 생성
# list2 와 list instance 연결
# list intstance count == 2 #list1과 list2가 가리키고 있음
# int instance 를 가리키는 list instance는 여전히 하나이므로 int instance coutner == 1
# list1 list2 같은 변수는 list객체의 카운터 up
# list 안의 객체들의 카운터를 늘리는 것은 그 객체들을 감싸는 []가 생성되면 늘려진다.

# list1[0] = 1000
# int instance 1000 생성
# list instance 의 [0] 메모리 주소를 1000의 메모리주소로 변경
# 1000 counter == 1 , 100 counter == 0
# 100's couter == 0 ==> garbage collector


# list3 = [1000,200,300]
# 새로운 list instance 생성
# 이미 존재하고 있는 int instance(1000,200,300) 과 연결
# 새로운 변수 list3 과 list instance 연결
# list instance's counter == 1 #위의 list intsance와는 다른 instance
# 1000,200,300's counter == 2 #int instance 를 가리키는 list instance 가 추가됨
# https://youtu.be/j8vXaGMJxQI?t=7860

# list2[1] = 2000
# int instance 2000 생성
# 200's counter ==1 2000's counter == 1

# list1 = list3
# list3 instance's counter == 2
# lsit2 instance's coutner == 1

## {is vs ==}

# list2 == list3 # 값이 같은가?
# list2 is list3 # 같은 객체인가? #메모리 주소가 같은가?

# 'class'로 'instance'를 만드는 것은 '새로운 객체를 생성'한다는 것.
# '새로운 객체'를 생성한다는 것은 '서로 다른 메모리 공간'에 저장된다는 것.

# x = [100,200,300]
# y = x
# z = [100,200,300]
# print(y is x) #True
# print(z is x) #False
# print(z == x) #True

## {interning}

# 이전에 사용한 객체를 기억하고 사용하는 기법
# '20자 미만 문자열' or '-5~256 사이 정수'에서 사용가능
# 조건이 randomly 하다!

# x = 100
# y = x
# z = 100
# print(y is x) #True
# print(z is x) #True

## Quiz

# x['name'] ?
# x = {'name' : 'craftsman'}
# y = x
# y['name'] = 'mentality'
# print(x['name'])

# Answer :
# mentality
# '서로 같은 객체를 공유'하므로 변경됨.

## {Numbers}

# Integer - 정수
# Float - 소수
# Boolean - True(1) or False(0)

# 표현식연산
# +, -, *, **, /, //, %, ()

# print(5/2) #2.5
# print(5//2) #2 #2 and 1/2 ==> 2~3's min ==> 2
# print(5%2) #1
# print(5//-2) #-3 #-2 and -1/2 ==> -3~-2's min ==> -3
# print((3+3)*2**2-23) #1
# // 은 value 가 b라면 a<b<c 중 a의 값으로, 즉 가장 min한 값으로!

# 비교
# number는 free하게 비교 가능
# int와 float형도 비교 가능!
# >, <, >=, <=, ==, !=, and, or
# print(3>3) #False
# print(3>=3) #True
# print(2.1>2) #True #'int과 float도 비교' 가능하다!
# print(5 == 5.0) #True
# print(5 != 4) #True

# x=2
# y=3
# z=4

# c언어 처럼 %% || 를 쓰지 않는다.
# and or 로 논리연산
# a<b<c 같은 연속 연산도 가능
# print(x<y and y>z) #False
# print(x<y or y>z) #True
# print(1<2<3.0<4) #and 생략 #==1<2 and 2<3.0 and 3.0<4

## {Numbers 내장함수}

# pow(), abs(), around(), int(), float(), hex(), bin()
# float(3+3)
# int(float(3+3))

# print(float(3+3)) #6.0
# print(int(float(3+3))) #6

# # best way
# x = 3+3
# print(float(x)) #6.0
# print(int(float(x))) #6

# print(3**2) #9
# print(pow(3,2)) #9 #밑과 지수

# print(5/3) #1.6666666666666667
# print(round(5/3,2)) #1.67 #소수점 2자리 까지 반올림

# print(hex(15)) #0xf #16진법
# print(bin(5)) #0b101 #2진법

## {Import Modules} - math and random

# import math
# import random

# 모듈명.함수명()

# math.sqrt(25)
# math.log(100,10)
# math.pow(5,2)

# random.random()
# random.randint(0,9) 

# import math

# print(math.sqrt(25)) #5.0
# print(math.log(100,10)) #2.0
# print(math.pow(5,2)) #25.0

# import random
# print(random.random()) #0.927778240555753 #0~1 중 random 소수
# print(random.randint(0,9)) #0~9 중 random

## {Floating Number in Memory}

# 소수가 메모리에 저장하는 방식은 복잡하다.
# 정수 부분과 소수 부분을 따로 저장한다.
# int 보다 메모리 공간을 많이 차지한다.

# print(1.1+2.2==3.3) #False
# 1.1 을 메모리에 저장할 때
# 1.1과 매우 비슷한 숫자를 저장한다.
# 2.2을 메모리에 저장할 때
# 2.2과 매우 비슷한 숫자를 저장한다.
# 연산결과 3.3과 매우 비슷한 숫자를 연산한다.
# ==> False

# 해결방법
# int로 형변환
# print(int(1.1+2.2) == int(3.3)) #True

## {Boolean}

# True는 int의 instance?
# Z = True
# print(isinstance(Z,bool)) #True
# print(isinstance(Z,int)) #True
# print(Z) #True
# print(True == 1) #True
# print(True is 1) #False
# print(int(Z)) #1
# print(True + 4) #5

# True or False == 1 or 0
# True and False == 1 and 0
# True > 0 == 1 > 0

# print(1 or 0) #1
# print(1 and 0) #0

## {Complex numbers}
# 복소수... 쓰는일 거의 없음



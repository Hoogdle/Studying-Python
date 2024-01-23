### Day2 ###

## {Object Oriented Programming}

# Object : 물건
# Oriented : 만들어진
# Programming : 프로그래밍

# 물건은 재사용 가능
# 파이썬은 물건들로 만들어진 언어, 물건들을 이용해 프로그래밍

## {Data Types}

# Built-in data : int,float,bool,str,list,tuple,set,dict,none....
# int 객체 => int 데이터 객체를 만든다.
# bool 객체 => bool 데이터 객체를 만든다.
# integer : 정수
# float : 소수
# Boolean : True or False(1,0)


## {파이썬의 핵심 객체들을 보는 방법}

# .__class__
# x = 100
# print(x.__class__) #<class 'int'> ,x는 int 객체로 만들어짐
# print(x.__class__.__class__) #<class 'type'> , int는 type 객체로 만들어짐

## {isinstance}
# X = 400 # 400(int) 로 int 객체 X 만듦
# print(isinstance(X,int)) # X(400) 은 int의 인스턴스? #True
# Y = 400.1
# print(isinstance(Y,int)) # Y(400.1)은 int의 인스턴스? #False
# print(isinstance(Y,float)) #True
# Z = True
# print(isinstance(Z,bool)) # Z(True)는 bool의 인스턴스? #True
# print(isinstance(Z,int)) # True #True,False == 1,0

## {type()}

# X = 400
# print(type(X)) # X(400)은 어떤 클래스로 만들었나? #<class 'int'>
# print(X.__class__) #<class 'int'>

# Y = 400.1
# print(type(Y)) #<class 'int'>
# print(Y.__class__) #<class 'int'>

# Z = True
# print(type(Z)) #<class 'bool'>
# print(Z.__class__) #<class 'bool'>

## {숫자 연산}

# +,-,*,%,**,//
# print(400+300) #700
# print(True+1) #2
# print(400-100) #300
# print(4*100) #400
# print(400/100) #4.0
# print(2**2) #4

## {문자열}

#문자를 담고있는 데이터
# Str class 객체로 Str class 인스턴스 객체를 만드는 과정

# X = "안녕하세요"
# print(isinstance(X,str)) # X(안녕하세요)는 str의 인스턴스? #True

# Y = "안녕하세요"
# print(type(Y)) # Y(안녕하세요)는 어떤 클래스로 만들었는가? #<class 'str'>
# print(Y.__class__) #<class 'str'>

# 문자열은 문자 '하나하나'가 왼쪽=>오른쪽 으로 '하나씩' 저장된다.
# X[0] == '안'
# X[4] == '요'
# '안' 과 '요' 에 해당하는 바이너리 코드가 저장됨.

# X = "안녕하세요"
# print(X[0]) #안
# print(X[4]) #요
# print(len(X)) #5

## 1:10:03 리스트부터!


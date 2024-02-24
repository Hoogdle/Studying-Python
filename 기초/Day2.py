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
# print(type(Y)) #<class 'float'>
# print(Y.__class__) #<class 'float'>

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

## {List - 리스트}

# 대괄호 안에 객체들을 '순서대로' 모아 놓은 객체, 데이터 타입 상관 x
# 리스트가 리스트를 포함할 수 있다.
# [0,1,2,3] or [123,'hello',156.0] or [0,[1,2],[3,4,5],['안녕',['하','세요]]]
# List class 객체를 통해 List 객체를 만든다.

# X = ['안녕하세요']
# print(isinstance(X,list)) #X(['안녕하세요'])는 List 인스턴스? #True

# Y = ['안녕하세요']
# print(type(Y)) #Y는 어떤 클래스로 만들어졌는가? #<class 'list'>
# print(Y.__class__) #<class 'list'>

# 객체의 '메모리 주소' '하나하나'를 왼쪽=>오른쪽 으로 저장
# 리스트안에 메모리 주소에 접근 후 값을 갖고옴.

# X = [0,[1,2],[3,4,5],['안녕',['하','세요']]]
# print(len(X)) #4
# print(X[3][1][0]) #하
# X[0] == 0의 메모리 주소
# X[1] == [1,2]의 메모리 주소
# X[3] == ['안녕',['하','세요]] 의 메모리 주소

## {Dictionaries - 사전}

# 중괄호 {} 안에 객체들을 랜덤 순서대로 모아 놓은 객체
# {key1 : value, key2 : value2, key3 : value3}
# 메모리에 저장될 때는 '랜덤한 순'으로 저장이 됨.
# {
#     'age' : 30,
#     'hobby' : ['최강야구보기','스타크래프트','음악듣기'],
#     'name' : {'first name': 'Craftsman',
#               'last name' : 'Mentality'},
#     0 : '0',
#     1 : '1'
# }

# X = {'name' : 'Craftsman Mentality'}
# print(isinstance(X,dict)) #X는 dict의 객체?

# Y = {'hobby' : ['쉬기','놀기','밥먹기']}
# print(type(Y)) #Y의 클래스? #<class 'dict'>
# print(Y.__class__) #<class 'dict'>

# Dictionary 는 '열(sequence)' 가 아니다.
# 객체들이 Random하게 저장됨.
# '인덱스'로 접근 X, 'Key'로 접근 O

# X = {
#     'age' : 30,
#     'hobby' : ['최강야구보기','스타크래프트','음악듣기'],
#     'name' : {'first name': 'Craftsman',
#               'last name' : 'Mentality'},
#     0 : '0',
#     1 : '1'
#     }

# Y = 'hobby'

# print(X[0]) #0
# print(X['age']) #30
# print(X['name']) #{'first name': 'Craftsman', 'last name': 'Mentality'}
# print(X['hobby'][0]) #최강야구보기
# print(len(X)) #5
# print(X[Y]) #['최강야구보기', '스타크래프트', '음악듣기']

# Key는 string,numbers,tuples,bool 만 가능
# Key는 중복되면 안 된다.

## {Dictionaries 작동원리}

# with 'Hash Table'
# *** dictionary는 'key의 메모리주소'와 'value의 메모리주소'를 저장
# 1. 'key' 메모리 주소에 접근하여 key 값을 가져옴
# 2. key값을 Hash 함수의 input, output으로 특정 메모리 주소 생성
# 3. output 메모리주소에 value 객체 생성

# 값을 저장할 때
# key address 접근 => key 값 get => hash(key) = address => address에 value 객체 생성

# 값을 가져올 때
# key address 접근 => key 값 get => hash(key) = address => address에 접근 value 가져오기

# key 값은 동일 하지만 주소가 다를 수도 있다.
# 하지만 Hash 함수에 들어가는 것은 'key의 값'이기 때문에 주소가 달라도 상관없다.

# ***
# key값이 다르다면 서로 다른 해쉬 값을 내뱉게 된다. 일반적으로 해쉬 값이 다르면 메모리 주소도 다르다.
# 하지만 파이썬에서는 메모리 최적화를 위해 immutable 데이터 타입이면 동일한 메모리 주소를 가리키게 한다.
# ***

# d = {1:'a',2:'a'}
# print(d[1] is d[2]) #True #immutable -> 메모리 최적화 동일한 주소

# d = {1:[1],2:[1]}
# print(d[1] is d[2]) #False #mutable -> 다른 메모리 주소





## {Tuples - 튜플}

# "수정이 불가능한 객체"
# "수정하려면 새로운 튜플 생성!"
# 괄호 () 안에 객체들을 왼쪽 => 오른쪽으로 모아 놓은 객체
# (1,2,3,4,5)
# ([1,2,3],(4,5),{'이름' : '크래프트맨','나이' : 30},'하이 헬로 안녕')
# 데이터 상관 X
# 리스트 수정 O , 튜플 수정 X
# 수정하려면 새로운 튜플 생성해야 함.

# 객체가 1개 -> ", 필수"
# X = ('안녕하세요',) 
# print(isinstance(X,tuple)) #X는 tuple의 객체? #True
# print(type(X)) #X의 클래스? #<class 'tuple'>
# print(X.__class__) #X의 클래스? #<class 'tuple'>

# 객체 '메모리 주소' '하나하나' 를 왼쪽 => 오른쪽 저장
# X = ([1,2,3],(4,5),{'이름' : '크래프트맨','나이' : 30},'하이 헬로')
# print(X[0]) #[1, 2, 3]
# print(X[2]['이름']) #크래프트맨
# print(X[2]) #{'이름': '크래프트맨', '나이': 30}
# print(len(X)) #4


## {Sets - 세트}

# 수정 불가한 객체!
# 중복 불가한 객체!
# 중괄호 {} 안에 객체들을 '랜덤 순서대'로 모아 놓은 객체
# {1,2,3,4,5}
# 객체의 중복 불가
# 수정 불가
# Dictionary의 'key' 들만 모아 놓은 개념

# X = {'안녕하세요'}
# print(isinstance(X,set)) #X는 set의 객체? #True
# print(type(X)) #X의 클래스? #<class 'set'>
# print(X.__class__) #X의 클래스? #<class 'set'>

## {None Type}

# 존재하지 않는 값
# error를 피하기 위해 사용

# X = None
# print(isinstance(X,None)) #error
# print(type(X)) #X의 클래스? #<class 'NoneType'>
# print(X.__class__) #<class 'NoneType'>

## {Mutable vs Immutable} - 수정가능성

# 수정 O : List, Dictionary(key는 수정불가)
# 수정 X : Numbers, Str, Tuple, Set

## Quiz

# X = [{(1,2,3) : ['크래프트맨 멘탈리티','최고',[100,200]],'취미' : ['최강야구','쉬기','놀기']}]

# 1. 100 가져오기
# 2. '최강야구' 가져오기

# print(X[0][(1,2,3)][2][0]) #100
# print(X[0]['취미'][0]) #최강야구

### Day7 ###

## {For Loop}
# 열에 있는 아이템을 하나하나씩 거쳐간다.
# object 가 열의 형태라 했을 때
# for item in object :
#     statements
# else :
#     statements

# for item in ['a','b','c']:
#     print(item)
# a
# b
# c

# x = 0
# for item in [100,200,300,400] : 
#     x+=item
# print (x) #1000

# for letter in '머신러닝' : 
#     print(letter)
#머
#신
#러
#닝

# for item in ('a','b','c','d'):
#     print(item)
#a
#b
#c
#d 

# for item in [('a','b'),('b',2),('c',3)]:
#     print(item)
#('a','b')
#('b',2)
#('c',3)

# for item in [('a','b'),('b',2),('c',3)] : 
#     print(item[0]) 
#a
#b
#c

# for item1,item2 in [('a',1),('b',2),('c',3)]:
#     print(item1)
#     print(item2)
#a
#1
#b
#2
#c
#3

# Dictionary은 열이 아닌데.... 사용가능!
# Dictionary은 반복이 가능한 객체, 사용가능!
# D = {'a':1,'b':2,'c':3}
# for key in D:
#     print(key, '=', D[key])
# a = 1
# b = 2
# c = 3

# D = {'a':1,'b':2,'c':3}
# print(D.items()) #dict_items([('a', 1), ('b', 2), ('c', 3)]) #List가 아님
# for key,value in D.items():
#     print(key, '=' , value)
# a = 1
# b = 2
# c = 3

# Dictionary 처럼 열이 아니더라도 반복이 가능하면 for loop 사용 가능
# 반복 가능한 객체들을 하나씩 거쳐감.
# 리스트 터플 문자열 사전 == 반복 가능한 객체
# 숫자, 반복 불가능 : for loop에서 사용 안 됨.
# 숫자의 경우 range() 로 대체. 
# range(5) == range(0,5) == range(0,5,1)

# range()
# 연속된 숫자를 만듦.
# x = range(5)
# print(x) #range(0, 5)
# print(list(x)) #[0, 1, 2, 3, 4]

# range(5) == range(0,5,1) ==> (start,stop,step)
# y = list(range(100,500,100))
# print(y) #[100, 200, 300, 400]

# range는 List를 만들지 않고 range 객체를 만들어낸다.
# x = range(5)
# print(type(x)) #<class 'range'>

# range는 반복이 가능한 객체인가?
# for x in range(5):
#     print(x)
# 0
# 1
# 2
# 3
# 4
# => for문에서 사용가능 ==> 반복 가능한 객체

# range(len())
# s = '머신러닝'
# for index in range(len(s)):
#     print(s[index])
# 0
# 머
# 1
# 신
# 2
# 러
# 3
# 닝
# len(s) == 4 ==> range(4) ==> index : 0~3

# range(len()) 을 심플화 =>
# for char in 문자열:
# 계산량 적어짐.
# s = '머신러닝'
# for char in s:
#     print(char)
# 머
# 신
# 러
# 닝

# range(len)은 List안의 내용을 변경할 때 유용
# L = [1,2,3,4,5]
# for i in range(len(L)):
#     L[i] = L[i] * 100
# print(L) #[100, 200, 300, 400, 500]
# memory save

# 새로운 List를 만드는 방법
# L = [1,2,3,4,5]
# new_L = []
# for i in L:
#     new_L.append(i*100)
# print(L) # [1, 2, 3, 4, 5]
# print(new_L) #[100, 200, 300, 400, 500]
# time save

# memory 와 time은 trade-off 관계

# range(len) 을 While Loop에서
# L = [1,2,3,4,5]
# i=0
# while i<len(L):
#     L[i] = L[i]*100
#     i+=1
# print(L) #[100, 200, 300, 400, 500]

# List Comprehension
# 바로 기계어로 변환, 속도 fast

# 기존의 새로운 리스트 생성
# L = [1,2,3,4,5]
# new_L = []
# for i in L:
#     new_L.append(i*100)
# print(L) #[1, 2, 3, 4, 5]
# print(new_L) #[100, 200, 300, 400, 500]

# 새로운 방법
# L = [1,2,3,4,5]
# new_L = [x*100 for x in L]
# print(L) #[1, 2, 3, 4, 5]
# print(new_L) #[100, 200, 300, 400, 500]

# str case
# L = ['한국','캐나다','미국','일본','중국']
# new_L = [x+'사람' for x in L]
# print(L) #['한국', '캐나다', '미국', '일본', '중국']
# print(new_L) #['한국사람', '캐나다사람', '미국사람', '일본사람', '중국사람']

# if 추가
# L = ['한국','캐나다','미국','일본','중국']
# new_L = [x+'사람' for x in L if len(x)>2]
# print(L) #['한국', '캐나다', '미국', '일본', '중국']
# print(new_L) #['캐나다사람']

# 위 code를 for loop으로
# L = ['한국','캐나다','미국','일본','중국']
# new_L = []

# for x in L:
#     if len(x)>2 :
#         new_L.append(x+'사람')
# print(L) #['한국', '캐나다', '미국', '일본', '중국']
# print(new_L) #['캐나다사람']

# 다른 반복가능한 객체들

# zip()
# 객체를 하나로 모아줌

# L1 = [1,2,3,4]
# L2 = [100,200,300,400]
# print(zip(L1,L2)) #<zip object at 0x000002135492F9C0> #메모리객체 #List가 아님
# print(list(zip(L1,L2))) #[(1, 100), (2, 200), (3, 300), (4, 400)]

# for a,b in zip(L1,L2):
#     print(f'{a}+{b} => {a+b}')
# 1+100 => 101
# 2+200 => 202
# 3+300 => 303
# 4+400 => 404
    
# map()
# 변수1 : 함수, 변수2 : 객체(반복가능)
# 함수의 매개변수로 객체를 이용

# L = ['a','ab','abc','abcd']
# print(map(len,L)) #<map object at 0x0000028244375990>
# print(list(map(len,L))) #[1, 2, 3, 4]

# for x in map(len,L):
#     print(x)
# 1
# 2
# 3
# 4

# enumerate()
# 튜플의 형태
# index num, instacne를 모아놓은 객체

# L = ['a','ab','abc','abcd']
# print(enumerate(L)) #<enumerate object at 0x00000135E9E159E0>
# print(list(enumerate(L))) #[(0, 'a'), (1, 'ab'), (2, 'abc'), (3, 'abcd')]

# for idx,item in enumerate(L):
#     print(f'{idx} => {item}')
# 0 => a
# 1 => ab
# 2 => abc
# 3 => abcd

# s = '머신러닝'
# for idx,item in enumerate(s):
#     print(f'{idx} => {item}')
# 0 => 머
# 1 => 신
# 2 => 러
# 3 => 닝

# Quiz
# 동일한 문자 리스트형태로 출력

# s1 = '기계정리'
# s2 = '기계학습'
# L = []
# for i1 in s1:
#     if i1 in s2:
#         L.append(i1)
# print(L)



## {Functions - 함수}

# 코드 재활용
# 중복 코드 방지
# 역할 분담

# in 자동차
# 엔진 함수, 바퀴 함수, 시트 함수 etc...

# 함수 또한 객체

# def name(매개변수1,매개변수2,매개변수3):
    # statement
    # return

# def adder(a,b):
#     return a+b

# print(adder(1,2)) #3
# print(adder('머신','러닝')) #머신러닝
# print(adder([1,2,3],[4,5])) #[1, 2, 3, 4, 5]
# print(adder.__class__) #<class 'function'>

# Polymorphsim(다항성)
# Data type에 따라 연산 symbol들이 다양한 역할을 한다

# fucntion의 생성과정 
# function class 로 함수 instance 생성
# 변수(함수이름)생성, 함수 instance 연결 #instance count == 1
# 함수 호출시 결과 return
# https://youtu.be/j8vXaGMJxQI?t=22751

# return 문구 없어도 됨

# 함수 이름 변경
# 기존 이름으로 이용 가능
# 새로운 변수(happy)와 함수 instance연결, instance count == 2
# https://youtu.be/j8vXaGMJxQI?t=22912

# def adder(a,b):
#     return a+b
# happy = adder #이름 변경
# print(happy(1,2)) #3

# 이름 아예 변경

# 기존 이름으로 이용 불가, instance count == 1
# https://youtu.be/j8vXaGMJxQI?t=22947
# happy = adder
# adder = None

# 기존 이름으로 이용 불가, instance count == 1
# https://youtu.be/j8vXaGMJxQI?t=23016
# happy = adder
# del adder

# call 방법
# 함수이름(), ()안에 매개변수 넣기

# 매개변수가 없어도 됨

# def adder():
#     return 10+20
# print(adder()) #30
# print(adder(1,2)) #error

# Default 매개변수
# 지정 매개변수, 추후 변경 가능
# def adder(a = 100, b = 200, c = 300, d = 400):
#     return a+b+c+d
# print(adder()) #1000
# print(adder(1,2,3,4)) #10
# print(adder(1,d=5)) #506

# Quiz1
# 두 매개변수를 곱하는 함수를 만들어라

# def mul(a,b):
#     return a*b
# print(mul(4,5)) #20

# Quiz2
# 매개변수와 상관없이 100을 반환하는 함수를 만들어라

# def mul(a,b):
#     return 100
# print(mul(4,5)) #100
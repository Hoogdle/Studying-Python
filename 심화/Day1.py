### Day1 ###

## {Scopes - 스코프}
# 범위
# 소설 A의 브라이언, 소설 B의 브라이언 => 서로 다른 인물
# 변수가 어느 스코프, 어느 Namespace에 있느냐에 따라 다름

# Namespace : 변수 이름과 메모리 주소를 테이블 형태로 저장
# x = 2023
# 2023 int 객체 생성
# x 변수 생성
# x 와 2023 연결
# https://youtu.be/5xXB93rX_X8?t=198

# Functions 함수
# 함수는 함수 자체로 Namespace 를 가지게 된다.
# def 로 함수 생성
# def novel1():
    # name = "Bryan"
    # return name

# 함수내의 name 변수는 어디에 존재하는가?
# Function class 객체가 Function class instance 객체생성
# novel1 는 메모리 주소를 가짐. Namespace
# novel1()
# 함수 호출시 새로운 함수내에 새로운 namespace생성
# name = (메모리 주소)
# 함수 실행이 종료되면 함수내의 namespace 삭제 for 메모리 save

# Different Name
# name = "Bryan"

# def novel1():
#     name = 'Bryan'
#     return name

# def novel2():
#     name = 'Bryan'
#     return name

# 서로 다른 범위의 name
# name은 함수 호출 전까지 존재하지 않음

# name = 'Bryan'

# def novel1():
#     name = 'Kim'
#     return name

# novel1()
# print(name) #Bryan
# 함수 호출시 함수내 변수의 Namespace삭제!

# Global Scope
# 함수 밖의 영역
# 함수내의 해당 변수가 없으면 Global Scope에서 참조

# Nested Scopes (함수내의 함수)
# Global Scope => Enclosed Scope => Local Scope
# 포함되는 영역에서는 포함하는 영역을 참조가능

# Built-In-Scope 
# Global Scope 를 포함하는 Scope
# int,float,in,for 같은 '키워드'를 포함하는 Scope

## {Nested Functions - 함수 안의 함수}
# name = 'Kim'
# def outer():
#     name = 'Tae'
#     print(name)
#     def inner():
#         name = 'Yeong'
#         print(name)
# print(name) #Kim
# outer() #Tae

# inner 함수는 어떻게 실행?
# name = 'Kim'
# def outer():
#     name = 'Tae'
#     print(name)
#     def inner():
#         name = 'Yeong'
#         print(name)
#     inner()

# outer()
# Tab
# Yeong

# inner 함수의 name이 없어진다면?
# name = 'Kim'
# def outer():
#     name = 'Tae'
#     print(name)
#     def inner():
#         print(name)
#     inner()

# outer()
# Tae
# Tae

# outer 함수의 name도 없어진다면?
# name = 'Kim'
# def outer():
#     print(name)
#     def inner():
#         print(name)
#     inner()

# outer()
# Kim
# Kim

# 함수는 호출이 끝나면 namespace가 사라짐
# == 함수 안의 함수 또한 사라짐


## {global 키워드}

# name = 'Kim'
# def outer():
#     print('outer',name) #outer Kim

# outer()
# print('Global',name) #Global Kim

# outer에서 name = name + 'Tae'?
# error
# Local 변수로 Global 변수를 바꿀수 없음.
# 함수내에선 함수외의 변수를 변경할 수 없다(코드 복잡성)
# name = 'Kim'
# def outer():
#     name = name + 'Tae' #error
#     print('outer',name) 

# outer()
# print('Global',name) 

# Global 
# 함수내에서 함수외, Local에서 Global 변수에 영향을 줄 때 사용
# name = 'Kim'
# def outer():
#     global name # == Global의 name을 사용하겠다, Global 변수에도 영향을 끼침
#     name = name + "Tae"
#     print('outer',name) #outer KimTae

# outer()
# print('Global',name) #Global KimTae


## {nonlocal 키워드}
# local 변수로 enclosed 변수를 바꿀 수 없음
# error
# local에서 enclosed 변수에 영향을 줄 때 사용
# enclosed 변수가 필히 있어야 함!
# def outer():
#     name = "Kim"
#     print('outer',name) #otuer Kim

#     def inner():
#         name = name + 'Tae' 
#         print('inner',name) #error, 할당이 안 됨

#     inner()
# outer()

# def outer():
#     name = "Kim"
#     print('outer',name) #otuer Kim

#     def inner():
#         nonlocal name #local에서 enclosed 변수(name)에 영향을 주겠다.
#         name = name + 'Tae' 
#         print('inner',name) #inner KimTae

#     inner()
#     print('outer after inner()',name) #outer after inner() KimTae
# outer()



## {closure - 클로져}
# outer 함수 호출이 끝나면 inner 함수는 사라진다.
# outer 함수 namespace가 사라지기 때문
# outer가 끝나도 inner 함수를 기억하고 싶다면?
# return inner
# def outer():
#     name = 'Kim'
#     print('outer',name)
#     def inner():
#         name = 'Tae'
#         print('inner',name)
#     return inner
# A = outer() #outer Kim
# A() #inner Tae, #A가 return 값인 inner 함수를 받아옴

# 만약 inner에서 nonlocal 키워드를 사용했다면?
# def outer():
#     name = 'Kim' 
#     print('outer',name) #outer Kim
#     def inner():
#         nonlocal name
#         name = name + 'Tae'
#         print('inner',name) #inner KimTae
#     return inner
# A = outer() 
# A() 
# outer Kim
# inner KimTae
# outer 함수 종료 후 name 변수가 삭제되어야 할텐데..?
# A() #inner KimTaeTae
# A() #inner KimTaeTaeTae
# A() #inner KimTaeTaeTaeTae

# https://youtu.be/5xXB93rX_X8?t=1938
# outer 함수 종료, garbarge collector 가 처리, name 변수삭제
# 이 때 name의 '상태정보'를 별도로 저장
# A()를 호출할 때마다 name의 '상태정보' 수정 및 저장
# A() 반복, '상태정보' 계속 업데이트

# B = outer()
# A와 B의 상태정보는 다르다
# https://youtu.be/5xXB93rX_X8?t=2189
# def outer():
#     name = 'Kim' 
#     print('outer',name) #outer Kim
#     def inner():
#         nonlocal name
#         name = name + 'Tae'
#         print('inner',name) #inner Tae
#     return inner
# A = outer() #outer Kim
# B = outer() #outer Kim

# A() #inner KimTae
# A() #inner KimTaeTae
# B() #inner KimTae

# 심화
# def outer(start):
#     name = start
#     print('outer',name)
#     def inner():
#         nonlocal name
#         name = name + 'Tae'
#         print('inner',name)
#     return inner
# A = outer('Kim') #outer Kim
# B = outer('Kim') #outer Kim

# A() #inner KimTae
# A() #inner KimTaeTae
# B() #inner KimTae



## {Function Attributes - 함수 속성}
# 함수.속성 == "함수 속성을 정할 수 있음"
# def outer():
#     name = "kim"
#     print('outer',name)

# outer.age = 30
# outer.name = 'tae'
# print(outer.age) #30
# print(outer.name) #tae

# attributes, 속성은 함수와 별개로 저장됨.
# 함수의 name과 outer.name은 다름
# def outer():
#     name = "kim"
#     print('outer',name)
# #####################
# Attributes:
# outer.age = 30
# outer.name = 'tae' 

# closure 활용
# def outer(start):
#     name = start
#     print('outer',name)

#     def inner():
#         inner.name = inner.name + 'tae'
#         print('inner',inner.name)

#     inner.name = name #함수 속성
#     return inner
# A = outer('Kim') #outer Kim
# B = outer('Yeong') #outer Yeong
# # 함수는 종료되었지만 상태정보에 inner.name의 정보를 저장
# A() #inner Kimtae
# B() #inner Yeongtae

# List를 활용한 nonlocal
# local에서 enclosed 변수 변경 => nonlocal 활용
# List는 수정가능한 객체이므로 nonlocal을 사용하지 않아도 됨
# 변수 name 자체, 참조하는 리스트는 변경되지 않음
# 단지 리스트 첫 번째 index의 '내용'만 변경
# def outer(start):
#     name = [start]
#     print('outer',name)

#     def inner():
#         name[0] = name[0] + 'tae'
#         print('inner',name[0])
#     return inner
# A = outer('Kim') #outer ['Kim']
# B = outer('Yeong') #outer ['Yeong']
# A() #inner Kimtae
# B() #inner Yeongtae
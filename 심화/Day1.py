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

def outer():
    name = "Kim"
    print('outer',name) #otuer Kim

    def inner():
        nonlocal name #local에서 enclosed 변수(name)에 영향을 주겠다.
        name = name + 'Tae' 
        print('inner',name) #inner KimTae

    inner()
    print('outer after inner()',name) #outer after inner() KimTae
outer()




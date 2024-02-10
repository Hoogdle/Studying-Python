### Day4 ###

## {Decorators - 데코레이터}

# def decorate(func):
#     func()

# def saySomething():
#     print('hello')

# decorate(saySomething) #hello

# def decorate(func):
#     print('*****')
#     func()
#     print('*****')
    
# def saySomething():
#     print('hello')
    
# decorate(saySomething)
# *****
# hello
# *****


# def decorate(func):
#     def wrapper():
#         print('*****')
#         func()
#         print('*****')
#     return wrapper

# def saySomething():
#     print('hello')

# a = decorate(saySomething)
# a()
# *****
# hello
# *****

# def decorate(func):
#     def wrapper():
#         print('*****')
#         func()
#         print('*****')
#     return wrapper

# @decorate
# def saySomething():
#     print('hello')

# saySomething()
# *****
# hello
# *****


# def decorate(func):
#     def wrapper(say1):
#         print('*****')
#         func(say1)
#         print('*****')
#     return wrapper

# @decorate
# def saySomething(say1):
#     print(say1)

# saySomething('Christmas')
# *****
# Christmas
# *****

# def decorate(func):
#     def wrapper(say1,say2,say3,say4):
#         print('*****')
#         func(say1,say2,say3,say4)
#         print('*****')
#     return wrapper

# @decorate
# def saySomething(say1,say2,say3,say4):
#     print(say1,say2,say3,say4)

# saySomething('Christmas','is','comming','soon')
# *****
# Christmas is comming soon
# *****

# 위의 방법을 대체
# *args arguments
# def decorate(func):
#     def wrapper(*arg):
#         print('*****')
#         func(*arg)
#         print('*****')
#     return wrapper

# @decorate
# def saySomething(say1,say2,say3,say4):
#     print(say1,say2,say3,say4)

# saySomething('Christmas','is','comming','soon')
# *****
# Christmas is comming soon
# *****

## {Decorate를 왜 사용하는가?}

# from time import time

# def decorate(func):
#     def wrapper(*arg,**kwarg):
#         t1 = time()
#         func(*arg,**kwarg)
#         t2 = time()
#         print('the total time taken was : ',(t2-t1))
#     return wrapper

# @decorate
# def long_time():
#     for i in range(10000):
#         i*5

# long_time()
# the total time taken was :  0.0010001659393310547



## {Modules - 모듈}
# import? from?
# Ninja.py 생성

# import Ninja

# print(Ninja.name) #kakashik 
# Ninja 모듈안의 name
# __pycache__가 생성됨, Ninja 모듈을 Bytecode 형태로 변경함
# 다음에 import 할 때 __pycache__에서 참조, 속도 up

# print(Ninja.attack()) #chidori!!!


# from Ninja import name
# print(Ninja.name) #error
# Ninja를 import한 것이 아니라 Ninja의 name을 import한 것

# print(name) #kakashi
# print(attack()) #error
# Ninja의 name만 가져온 것, attack()은 가져오지 않았다!

# from Ninja import name,attack
# print(attack()) #chidori!!!

# name 변경
# print(name)
# name = 'kim'
# print(name) #kim
# import한 name은 main에서의 namespace의 name에 들어오게 됨.

# Ninja안의 name은 변경되지 않음
# import Ninja
# print(Ninja.name) #kakashi

# import vs from import
# 코드가 김 -> import (코드 관리가 힘듦)
# 코드가 짧음 -> from import

# __name__ : 현재 사용중인 py
# import Ninja

# if __name__ == '__main__':
#     print(Ninja.name) #kakashi
#     print(Ninja.attack()) #chidori!!!


## Ninjas 폴더생성
## Ninjas 안에 kakashi,naruto 파일 생성
# import Ninjas

# print(Ninjas.kakashi.name) #error
# print(Ninjas.naruto.name) #error

# import Ninjas.kakashi
# import Ninjas.naruto

# print(Ninjas.kakashi.name) #Kakashi
# print(Ninjas.naruto.name) #Naruto

# from Ninjas import kakashi,naruto

# print(kakashi.name) #Kakashi
# print(naruto.name) #Naruto

## Ninjas == 패키지
# __init__.py 라는 파일을 만들어야 파이썬이 Ninjas를 패키지라 인식




## {Exceptions - 에러관리}
# print('kim) 
# SyntaxError: unterminated string literal (detected at line 204)

# print(100/0)
# ZeroDivisionError: division by zero

# age = int(input('나이가 어떻게 되세요?:'))
# print(age)
# 숫자가 아닌 'hi'를 넣으면 value error 발생
# error를 피하고 계속 실행하려면?
# try except키워드 사용

# try:
#     age = int(input('나이가 어떻게 되세요?:'))
#     print(age)
# except:
#     print('숫자를 입력하세요')
# 나이가 어떻게 되세요?:hi
# 숫자를 입력하세요
# 나이가 어떻게 되세요?:30
# 30

# 계속 실행시키려면 while loop 사용

# while True:
#     try:
#         age = int(input('나이가 어떻게 되세요?:'))
#         print(age)
#     except:
#         print('숫자를 입력하세요')
# 무한반복....
# break로 해결!

# try에서의 else
# : 예외가 발생하지 않는 경우를 처리
# while True:
#     try:
#         age = int(input('나이가 어떻게 되세요?:'))
#         print(age)
#     except:
#         print('숫자를 입력하세요')
#     else:
#         break

# 좀 더 복잡하게!
# while True:
#     try:
#         age = int(input('나이가 어떻게 되세요?:'))
#         percentage = pow(100/age,-1)*100 # == (age/100)*100 #일부러 어렵게 한거랍니다.
#         print(f'당신은 {percentage}%만큼 살았습니다.')
#     except:
#         print('숫자를 입력하세요')
#     else:
#         break
# if input : 0
# '숫자를 입력하세요' ...?
# => 100을 0으로 나누는 error
    
# except 나누기
# while True:
#     try:
#         age = int(input('나이가 어떻게 되세요?:'))
#         percentage = pow(100/age,-1)*100 
#         print(f'당신은 {percentage}%만큼 살았습니다.')
#     except ZeroDivisionError:
#         print('0보다 큰 숫자를 입력하세요.')
#     except ValueError:
#         print('숫자를 입력하세요.')
#     else:
#         break


# finally 키워드(in try)
# 마지막에 무조건적으로 실행
# 어떤 조건이든 실행됨
# while True:
#     try:
#         age = int(input('나이가 어떻게 되세요?:'))
#         percentage = pow(100/age,-1)*100 
#         print(f'당신은 {percentage}%만큼 살았습니다.')
#     except ZeroDivisionError:
#         print('0보다 큰 숫자를 입력하세요.')
#     except ValueError:
#         print('숫자를 입력하세요.')
#     else:
#         break
#     finally:
#         print('Thank You')
# 나이가 어떻게 되세요?:0
# 0보다 큰 숫자를 입력하세요.
# Thank You
# 나이가 어떻게 되세요?:str
# 숫자를 입력하세요.
# Thank You
# 나이가 어떻게 되세요?:20
# 당신은 20.0%만큼 살았습니다.
# Thank You

# ZeroDivisionError as err
# ValueError as err       
# while True:
#     try:
#         age = int(input('나이가 어떻게 되세요?:'))
#         percentage = pow(100/age,-1)*100 
#         print(f'당신은 {percentage}%만큼 살았습니다.')
#     except ZeroDivisionError as err:
#         print(err)
#     except ValueError as err:
#         print(err)
#     else:
#         break
#     finally:
#         print('Thank You')
# 나이가 어떻게 되세요?:0
# division by zero
# Thank You
# 나이가 어떻게 되세요?:str
# invalid literal for int() with base 10: 'str'
# Thank You
# 나이가 어떻게 되세요?:
        

# 'raise Excception()'
# 일부러 error 내기
# ex) max를 넘는 숫자를 input 했을 때


# while True:
#     try:
#         age = int(input('나이가 어떻게 되세요?:'))
#         if age > 1000:
#             raise Exception('나이가 너무 많습니다..')
#         percentage = pow(100/age,-1)*100 
#         print(f'당신은 {percentage}%만큼 살았습니다.')
#     except ZeroDivisionError as err:
#         print(err)
#     except ValueError as err:
#         print(err)
#     else:
#         break
# 나이가 어떻게 되세요?:1234
# Traceback (most recent call last):
#   File "C:\Users\rlaxo\Desktop\천천히 배우는 파이썬(기초)\심화\Day4.py", 
# line 335, in <module>
#     raise Exception('나이가 너무 많습니다..')
# Exception: 나이가 너무 많습니다..


## {Exception으로 For loop 구현(Bonus)}
# 반복 가능 객체 : iterable
# 반복 객체 : iterator

# myList = [1,2,3,4,5] 
# num = 0

# for item in myList:
#     num = num + item

# print(num) #15

# 위 코드를 for loop 없이 구현
# mylist 는 반복가능한 객체
# 반복문에서 사용하기 위해서 반복객체로 변경
# myList = [1,2,3,4,5] 
# iterator = iter(myList)
# num = 0
# while True:
#     try:
#         num = num + iterator.__next__()
#     except StopIteration:
#         break
# print(num) #15


## {구글링}

# 모르는 것이 있으면 구글링!
# 'python documentatioon'
# '파이썬 문서'
# '점프 투 파이썬'

# 파이썬의 모든 것을 알고 있는 것이 중요한 것이 아니다.
# 필요한 것들을 구글에서 잘 찾아내는 것이 중요하다.

# 모르는 것을 파악하고 
# 모르는 것을 알아내는 능력이 중요하다!


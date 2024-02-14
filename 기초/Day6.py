### Day6 ###

## {Statements vs Expression} 문구 vs 수식

# 프로그램 구성
# 프로그램 => 모듈 => Statements(문구) => Expression(수식)
# https://youtu.be/j8vXaGMJxQI?t=16473

# Statements vs Expression
# a = 1+2
# 1+2 : 수식(Expression)
# a = 1+2 : 문구(Statements)
# Statements : 명령을 다룸
# Expression : 객체를 다룸

# Statements 는 "무언가를 하라고" 알려준다.
# Expression 은 객체를 생성하고 다룬다.
# Statements 안에 Expression 이 포함됨.

## {Syntax - 문법}

# 파이썬은 문구를 '한 줄씩' 써야한다
# 타 프로그래밍 언어는 한 줄씩 안 쓰는게 일반적
# a = 1+2 #good
# a =
# 1+2   #error

# 한 줄씩 안 써도 되는 경우
# a = [1,2,3,
#     4,5,6,
#     7,8,9]
# x = (1+2+
#      3+4)
# mydict = {'name' : 'kim',
#           'age' : 30,
#            'hobby' : 'programming'}
# print (a,x,mydict) # not error

# Indentation('들여쓰기')가 중요하다
# Indentation 의 space를 지켜야 한다. 맞춰줘야 함.
# Tab 을 적극활용!
# A = 10; B = 5
# if A>B:
#     print('A is bigger than B') #A is bigger than B

# Sequence unpacking(열 할당)
# A,B = (1,2) #A==1 B==2
# print(A,B) #1 2
# A,B = [1,2] #A==1 B==2
# print(A,B) #1 2
# A,B,C,D = '머신러닝'
# print(A,B,C,D) #머 신 러 닝

# seq = [1,2,3,4]
# a,*b = seq
# print(a) #1
# print(b) #[2,3,4]

# seq = [1,2,3,4]
# a,*b,c = seq
# print(a) #1
# print(b) #[2,3]
# print(c) #4

## {if Test}
# 조건 충족시 실행
# if 조건문1:
#   statement1
# elif 조건문2:
#   statement2
# else:
#   statement3

# x=100
# y=10
# z=1

# if y>x:
#     print('if test has passed')
# elif z>y:
#     print('elif test has passed')
# else:
#     print('else test has passed')
    
# print('outside if test') #else test has passed
#                          #outside if test
# https://youtu.be/j8vXaGMJxQI?t=17474

# 조건문에서 물어보는 것은 True of False 이다
# 100 >10
# not 100>10
# 100==100
# 100!=100

# 객체가 비어있지 않음 => True
# 객체가 빔 => False

# if 1: print('true') #true
# if 100 : print('true') #true
# if 'spam' : print('true') #true
# if [100,200,300] : print('true') #true

# if 0 : print('true') #
# if 0 : print('true') #
# if '' : print('true') # 
# if [] : print('ture') #
# 아무것도 출력안됨.

# and or

# or : 왼쪽부터 탐색, true 가 나오면 pass
# 2 or 3 / 3 or 2 / [] or 2 / [] or '' 
# 2 == true => end
# 3 == true => end
# [] == false => 2 == true => end
# [] == false => '' == false => end
# print(2 or 3) #2
# print (3 or 2) #3
# print([] or 2) #2
# print([] or '') #
# print([] or '' or 2) #2

# and : 왼쪽부터 탐색, false가 나오면 pass
# 2 and 3, 3 and 2, [] and 2, 2 and [], [] and ''
# 2 == true => 3 == true => end
# 3 == true => 2 == true => end
# [] == false => end
# 2 == true => [] == false => end
# [] == false => end
# print(2 and 3) #3
# print (3 and 2) #2
# print([] and 2) #[]
# print(2 and []) #[]
# print([] and '') #[]
# false라면 and 종료, 마지막 객체 print

# A = ((X and Y)or Z)
# 만약 X와 Y 모두 true 라면 A == Y
# 만약 X False A== Z
# 위의 식과 동일
# if X:
    # A=Y
# else:
    # A=Z
# A = Y if X else Z # X true, A==Y. X false, A==Z.

 
## {While Loop}
# 가장 위의 문구가 True일 동안 반복적으로 밑에 문구들을 실행
# 위 조건이 False가 되면 Loop 에서 나감.

# Infiinet Loop (무한 루프)

# while True:
#     print('무한루프 진입')

# x = '머신러닝'
# while x:
#     print(x)
#     x = x[1:] #x에 새로운 문자열 대입
# 머신러닝
# 신러닝
# 러닝
# 닝
# x가 비어있는 문자열 => flase => while문 종료

# x = 5
# while x:
#     print(f'로켓발사 {x}초 전')
#     x -= 1

# a=0;b=5
# while a<b:
#     print(b)
#     b-=1

# break,continue,pass
# break : 루프에서 바로 나감
# continue : 루프 가장위로 올라감
# pass : 아무것도 안 함 (==None), 보통 사용 X

# pass
# while True:
#     pass

# continue
# x = 10
# while x:
#     x-=1
#     if x%2!=0:
#         continue
#     print(x)
# 8 6 4 2 0

# 10을 포함하는 code
# x = 10
# while x:
#     if x%2==0 : 
#         print(x)
#         x-=1
#     else: x-=1
# else:
#     print(x)
# 10 8 6 4 2 0

# break
# while 문과 else 문의 결합
# while loop의 조건이 충족 안 됨 => else로 이동
# input : 입력값 받아옴
# a = 5
# s_pw = 'secret'
# while a:
#     a-=1
#     pw = input('What is your pw : ')
#     if pw == s_pw:
#         print('Your pw is correct.')
#         break
#     print(f'You have {a} tiems left to try')
# else :
#     print('failed to login')

# while 문을 가능한 사용하지 않는게 좋다.
# 속도, for loop > while loop
# 가능한 for loop 사용
### Day2 ###

## {Recursion - 재귀}
# empty list, 비어있으면 false
# not x == x가 비어있다
# def adding_machine(x):
#     if not x:
#         return 0
#     else:
#         return x[0] + adding_machine(x[1:])

# my_list = [1,2,3,4,5]
# print(adding_machine(my_list)) #15

# 과정
# [1,2,3,4,5] +1
# [2,3,4,5] +2
# [3,4,5] +3
# [4,5] +4
# [5] +5
# [] return 0

# for loop 이용
# for loop을 이용하는 것이 훨씬 빠르다
# def adding_machine(x):
#     num = 0
#     for item in x:
#         num += item
#     return num
# my_list = [1,2,3,4,5]
# print(adding_machine(my_list)) #15

# 리스트안의 리스트인 경우
# for loop만으로 해결 불가, for loop과 recursion 교차사용
# *** adding_machine이 재귀 될때마다의 num의 주소는 다르다!
# 각 리스트의 총합이 return 됨.
# my_list = [1,[2,[3,4],5],6,[7,7]]

# def adding_machine(x):
#     num = 0
#     for item in x:
#         if not isinstance(item,list):
#             num += item
#         else:
#             num += adding_machine(item)
#     return num

# print(adding_machine(my_list))



## {For Loop은 어떻게 작동하는가?}
# 우주의 별이 1억개 있다고 가정
# 별의 이름을 번역하는 방법
# 1. 별의 이름을 모두 읽고 번역
# 2. 별의 이름을 하나씩 읽으면서 번역
# 파이썬에서의 for loop 은 2번째 방법(하나씩 읽으면서)

# for loop 은 열에 있는 아이템을 하나씩 거쳐간다.
# list,tuple 심지어 dictionary 모두 반복이 가능하기에 for loop 사용 가능
# 숫자는 반복이 불가능, for loop 사용 불가

# 반복 가능 객체 vs 반복 객체
# iter()
# 반복이 가능한 객체로 반복 객체 생성
# 서로 다른 타입의 객체
# 반복 가능 객체 : list,dict,tuple,str etc..
# 반복 객체

# 반복객체?
# 반복을 해주는 공장
# 리스트 객체를 처음부터 끝까지 읽지 않는다.
# 하나씩 반복만 한다.
# .__next__() => 반복 시작 메소드
# stars = ['Neutron','Leo','Vega','Rigel']
# eachStar = iter(stars)
# print(type(stars)) #<class 'list'>
# print(type(eachStar)) #<class 'list_iterator'> #리스트 반복개체

# .__next__()가 끝이나면
# Stopiteration 이라는 exception으로 종료
# print(eachStar.__next__()) #Neutron
# print(eachStar.__next__()) #Leo
# print(eachStar.__next__()) #Vega
# print(eachStar.__next__()) #Rigel
# print(eachStar.__next__()) #error

# For Loop
# '반복 객체'를 생성하고 반복시킴
# 아래의 과정을 자동적으로 실행
# stars = ['Neutron','Leo','Vega','Rigel']
# eachStar = iter(stars)
# print(eachStar.__next__()) #Neutron
# print(eachStar.__next__()) #Leo
# print(eachStar.__next__()) #Vega
# print(eachStar.__next__()) #Rigel
# print(eachStar.__next__()) #error

# 사전 반복객체
# 'key' 들을 반복시킨다!
# for loop 에서는 'key'들이 item 으로 지정됨.
# stars = {'star1':'Neutron',
#          'star2': 'Leo',
#          'star3': 'Vega',
#          'srat4': 'Rigel'}
# x = iter(stars)
# print(type(stars)) #<class 'dict'>
# print(type(x)) #<class 'dict_keyiterator'> # 딕셔너리_키 반복객체

# print(x.__next__()) #star1
# print(x.__next__()) #star2
# print(x.__next__()) #star3
# print(x.__next__()) #star4

# keys() 
# key 값들을 모아줌
# keys = stars.keys()
# print(keys) #dict_keys(['star1', 'star2', 'star3', 'srat4'])
# print(type(keys)) #<class 'dict_keys'>
# print(list(keys)) #['star1', 'star2', 'star3', 'srat4']

# For loop with Dictionary
# Dic 의 key 들을 item으로

# for item in stars:
#     print(item)
# star1
# star2
# star3
# srat4

# range 반복객체
# x = range(9)
# print(type(x)) #<class 'range'>
# print(x) #range(0, 9)
# print(list(x)) #[0, 1, 2, 3, 4, 5, 6, 7, 8]

# y = iter(x)
# print(type(y)) #<class 'range_iterator'>

# range는 반복가능한 객체
# for loop 에서는 range를 반복객체로 변환 후 사용
# for item in x:
#     print(item)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# enumerate 반복객체
# enumerate는 그 자체로 반복객체
# for loop 에서 사용가능
# x = 'hello'
# y = enumerate(x)
# print(type(y)) #<class 'enumerate'>
# print(y) #<enumerate object at 0x00000186A91F2890>
# print(list(y)) #[(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

# z = iter(y)
# print(z) #<enumerate object at 0x00000112969028E0>
# print(type(z)) #<class 'enumerate'>

# print(iter(y) is y) #True

# for item in y:
#     print(item)
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')



## {Functional Programming - 함수형 프로그래밍}
# 함수와 데이터를 구분하여 관리


# {lambda - 람다}
# simple한 함수를 만들 때 사용
# 이름 없는 함수를 만듦
# 따로 변수로 할당해야 함.

# <형식>
# lambda 매개변수 : 수식

# def mysum(a,b):
#     return a+b

# mysum = lambda a,b : a+b
# print(mysum(4,5)) #9

# lambda 또한 local -> enclosed -> global -> built-in scope 룰을 따른다.
# local 함수가 enclosed 함수의 변수 '참조'는 가능
# '수정'할 때 nonlocal 키워드 사용
# def novel(start):
#     name = start
#     position = (lambda x : name + ' ' + x)
#     return position
# person = novel('Kim') # person 이 position 함수를 가져옴
# print(person('TaeYeong')) #Kim TaeYeong



# {map() 함수}
# mapping - 어떤 값을 다른 값에 대응 시킴
# 함수와 반복 가능한 객체들을 대응시킨다.
# map(함수,반복가능 객체)
# mapping만 하고 연산은 하지 않음
# map 자체는 반복객체, .__next__() 가능

# nums = [(1,2),(3,4),(5,6)]

# def mysum(a):
#     return a[0]+a[1]
# result = map(mysum,nums)
# print(result) #<map object at 0x00000185DDC0AB30>
# print(result.__next__()) #3
# print(result.__next__()) #7
# print(result.__next__()) #11

# result = map(mysum,nums)
# print(list(result)) #[3, 7, 11]

# lambda 활용
# nums = [(1,2),(3,4),(5,6)]

# result = map(lambda a : a[0]+a[1],nums)
 
# print(result) #<map object at 0x000001F3691FAB00>
# print(list(result)) #[3, 7, 11]




# {filter() 함수}
# 조건함수와 반복가능 객체를 대응시킴
# filter(조건함수, 반복가능 객체)
# mapping만, 연산은 하지 않음
# filter() 객체는 반복객체
# 조건이 true, 값 반환 false, 반환 값 없음
# data = [1,2,3,'a','b','c',4,5,6]

# def condition(item):
#     return isinstance(item,int)

# result = filter(condition,data)
# print(result) #<filter object at 0x000002811511ABF0>
# print(list(result)) #[1, 2, 3, 4, 5, 6]

# result = filter(condition,data)
# print(result.__next__()) #1
# print(result.__next__()) #2
# print(result.__next__()) #3
# print(result.__next__()) #4

# lambda 활용]
# data = [1,2,3,'a','b','c',4,5,6]
# result = filter(lambda x : isinstance(x,int),data)
# print(list(result)) #[1, 2, 3, 4, 5, 6]




# {reduce() 함수}
# 반복가능 객체들의 item을 함수의 input으로 했을 때
# output을 누적해서 반환
# from functools import reduce 해야 사용가능

# from functools import reduce

# mylist = [1,2,3,4,5]

# def accumulator(acc,item):
#     print('acc:',acc,'item:',item)
#     return acc + item
# acc: 0 item: 1
# acc: 1 item: 2
# acc: 3 item: 3
# acc: 6 item: 4
# acc: 10 item: 5

# result = reduce(accumulator,mylist,0) #acc 는 0부터, 기본값 item의 first value
# print(result) #15

# lambda 활용
# mylist = [1,2,3,4,5]
# result = reduce(lambda acc, item : acc + item, mylist)
# print(result) #15


# {Comprehensions - 컴프리헨션}
# [], (), {} 안에 사용 
# (원하는 수식 for item in 반복가능객체)
# for loop 대체 
# map 대체
# filter() 대체
# if else 대체

# mylist = ['kim','tae','yeong','travis','mark']
# newlist = [item + 'best' for item in mylist]
# print(newlist) #['kimbest', 'taebest', 'yeongbest', 'travisbest', 'markbest']

# mylist = [0,1,2,3,4,5]
# newlist = [item * 10 for item in mylist]
# print(newlist) #[0, 10, 20, 30, 40, 50]

# celsius = [0,10,20,30,40,50]
# fahrenheit = [(c*(9/5)+32) for c in celsius]
# print(fahrenheit) #[32.0, 50.0, 68.0, 86.0, 104.0, 122.0]

# for loop?, 코드가 길어짐
# fahrenheit = []
# for c in celsius:
#     f = c*(9/5)+32
#     fahrenheit.append(f)
# print(fahrenheit) #[32.0, 50.0, 68.0, 86.0, 104.0, 122.0]

# map 대체가능

# map으로 작성한 코드
# def fahren(c):
#     f = c*(9/5)+32
#     return f
# fahrenheit = map(fahren,celsius)
# print(list(fahrenheit)) #[32.0, 50.0, 68.0, 86.0, 104.0, 122.0]

# comprehension으로 작성한 코드
# fahrenheit = [fahren(c) for c in celsius]
# print(fahrenheit) #[32.0, 50.0, 68.0, 86.0, 104.0, 122.0]

# filter와 비교
# 남자 or 여자 직원들만 필터링

# comprehension으로 작성한 코드
# employees = [{'이름' : 'Bryan','연봉':'100000','성별':'남'},
#              {'이름' : 'Sally','연봉':'500000','성별':'여'},
#              {'이름' : 'Chris','연봉':'400000','성별':'남'},
#              {'이름' : 'Susan','연봉':'500000','성별':'여'},
#              {'이름' : 'Jimmy','연봉':'900000','성별':'남'}]

# male = [emp for emp in employees if emp['성별']=='남']
# print(male)
# [{'이름': 'Bryan', '연봉': '100000', '성별': '남'}, {'이름': 'Chris', '연
# 봉': '400000', '성별': '남'}, {'이름': 'Jimmy', '연봉': '900000', '성별': '남'}]

# femail = [emp for emp in employees if emp['성별'] == '여']
# print(femail)
# [{'이름': 'Sally', '연봉': '500000', '성별': '여'}, {'이름': 'Susan', '연
# 봉': '500000', '성별': '여'}]

# filter로 작성한 코드
# employees = [{'이름' : 'Bryan','연봉':'100000','성별':'남'},
#              {'이름' : 'Sally','연봉':'500000','성별':'여'},
#              {'이름' : 'Chris','연봉':'400000','성별':'남'},
#              {'이름' : 'Susan','연봉':'500000','성별':'여'},
#              {'이름' : 'Jimmy','연봉':'900000','성별':'남'}]

# def ismail(emp):
#     return emp['성별'] == '남'

# mail = filter(ismail,employees)
# print(list(mail))
# [{'이름': 'Bryan', '연봉': '100000', '성별': '남'}, {'이름': 'Chris', '연
# 봉': '400000', '성별': '남'}, {'이름': 'Jimmy', '연봉': '900000', '성별': '남'}]

# def isfemail(emp):
#     return emp['성별'] == '여'

# femail = filter(isfemail,employees)
# print(list(femail))
# [{'이름': 'Sally', '연봉': '500000', '성별': '여'}, {'이름': 'Susan', '연
# 봉': '500000', '성별': '여'}]

# in [] , list 생성
# in () , Generator 생성 
# in {} , dictionary 생성

# in {}
# key와 value 값을 설정해줘야 함.
# employees = [{'이름' : 'Bryan','연봉':'100000','성별':'남'},
#              {'이름' : 'Sally','연봉':'500000','성별':'여'},
#              {'이름' : 'Chris','연봉':'400000','성별':'남'},
#              {'이름' : 'Susan','연봉':'500000','성별':'여'},
#              {'이름' : 'Jimmy','연봉':'900000','성별':'남'}]
# male_employees = {emp['이름'] : emp['연봉'] for emp in employees if emp['성별'] == '남'}
# print(male_employees)
#{'Bryan': '100000', 'Chris': '400000', 'Jimmy': '900000'} 


# if else 대체
# employees = [{'이름' : 'Bryan','연봉':'100000','성별':'남'},
#              {'이름' : 'Sally','연봉':'500000','성별':'여'},
#              {'이름' : 'Chris','연봉':'400000','성별':'남'},
#              {'이름' : 'Susan','연봉':'500000','성별':'여'},
#              {'이름' : 'Jimmy','연봉':'900000','성별':'남'}]

# money = [[emp['이름'],'돈 많음']if int(emp['연봉']) >400000 else [emp['이름'],'돈 적음'] for emp in employees]
# print(money)
# [['Bryan', '돈 적음'], ['Sally', '돈 많음'], ['Chris', '돈 적음'], ['Susan', '돈 많음'], ['Jimmy', '돈 많음']]

# comprehension은 빠르다
# cmoprehension은 c언어로 실행 됨, 빠름
# for loop(),map(),filter() 보다 빠름
# 간단한 연산 -> comprehension 이용!



# {Generators - 제네레이터}
# range(),enumerate(),map(),filter(),zip()
# 메모리 사용량을 줄임
# 반복 객체

# a = range(0,10)
# print(a) #<class 'range'>
# print(list(a))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range(0,100)
# 0~99 까지 다 읽고 만들지 않음
# 0부터 '하나하나씩' 99까지 감

# yield 
# 사용자 정의 generator 만들기
# def my_genreator(num):
#     for i in range(0,num):
#         yield i
# a = my_genreator(5)
# print(a) #<generator object my_genreator at 0x00000179818A8D60>
# print(a.__next__()) #0
# print(a.__next__()) #1
# print(a.__next__()) #2
# print(a.__next__()) #3
# print(a.__next__()) #4

# b = my_genreator(3)

# print(b.__next__()) #0
# a와 b는 서로 다른 generator

 



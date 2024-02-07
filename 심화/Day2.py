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


# lambda - 람다
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


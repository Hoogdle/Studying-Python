### Day5 ###

## {Dictionaries - 사전}

# {} 안에 객체들을 "랜덤" 순으로 모아놓음
# key 와 value 로 분류
# sequence X, Mapping O
# dict 내장 함수로 생성가능

# Dictionary 'in' test
# 'Key'의 존재유뮤를 테스트
# D = {'name' : 'Kim' , 'age' : 24 , 'hobby' : 'programming'}
# print('name' in D) #Ture
# print('food' in D) #False
# print('Kim' in D) #False

# Dictionary Indexing by 'Key'
# D = {'name' : 'Kim' , 'age' : 24 , 'hobby' : 'programming'}
# print(D['name']) #Kim
# print(D['age']) #24
# print(D['hegiht']) #error

# Dcitionary Method
# Dictionary class 객체 안에 존재
# .keys(), .values(), .items()
# return 값이 List 는 아님 => index 활용 X

# D = {'name' : 'Kim' , 'age' : 24 , 'hobby' : 'programming'}
# print(D.keys()) #dict_keys(['name', 'age', 'hobby'])
# print(D.values()) #dict_values(['Kim', 24, 'programming'])
# print(D.items()) #dict_items([('name', 'Kim'), ('age', 24), ('hobby', 'programming')])

# List로 변경하기
# list(), indexing 활용 가능
# list로 변환 과정 중 메모리가 더 사용됨.
# D = {'name' : 'Kim' , 'age' : 24 , 'hobby' : 'programming'}
# print(list(D.keys())) #['name', 'age', 'hobby']
# print(list(D.values())) #['Kim', 24, 'programming']
# print(list(D.items())) #[('name', 'Kim'), ('age', 24), ('hobby', 'programming')]

# Dictionary 수정하기
# Value는 수정가능 // Key는 수정 불가능 (해쉬 함수를 이용하기 때문)
# 따라서 Key에 수정가능한 '리스트'는 오지 못한다. 튜플은 가능

# D = {'name' : 'Kim' , 'age' : 24 , 'hobby' : 'programming'}
# D['name'] = 'Lee'
# D['hobby'] = ['야구','축구','농구']
# D['height'] = '182' #키추가
# print(D) # {'name': 'Lee', 'age': 24, 'hobby': ['야구', '축구', '농구'], 'height': '182'}
# del D['height'] #키삭제

# D = {}
# print(D) #{}

# D[(1,2,3)] = 'value1'
# print(D) #{(1, 2, 3): 'value1'}

# D[(4,5,6)] = 'value2'
# print(D) #{(1, 2, 3): 'value1', (4, 5, 6): 'value2'}

# D['name'] = 'kim'
# print(D) #{(1, 2, 3): 'value1', (4, 5, 6): 'value2', 'name': 'kim'}

# x = 1; y = 2; z = 3
# t = (x,y,z)
# print(D[(x,y,z)]) # == print(D[1,2,3]) #value1
# print(D[t]) #value1 #t와 (1,2,3) 은 다른 객체 but 같은 값을 가짐 ==> 해쉬 함수 이용

## {Tuples - 튜플}
# () 안에 객체를 순서대로 모아 놓은 객체
# 수정 불가, 새로 생성해야 함.
# 모든 데이터를 넣을 수 있음
# 인덱싱 가능
# 객체들의 메모리 주소를 순서대로 저장
# T = 1,2,3 // 괄호 없어도 상관 X

# 객체 하나 ==> , 를 추가해야함.
# T = (40,)
# t = (40)
# print(type(T)) #<class 'tuple'>
# print(type(t)) #<class 'int'>

# Tuple Polymorphism(다항성)
# print((1,2,3)+(4,5,6)) #(1, 2, 3, 4, 5, 6) # 새로운 튜플 생성
# print((1,2,3)*3) #(1, 2, 3, 1, 2, 3, 1, 2, 3)

# Tuple in Test
# print(100 in (100,200,300)) #True
# print((100,200) in (100,200,300)) #False

# Tuple indexing, slicing
# t = (100,200,300,400)
# print(t[0]) #100
# print(t[1:-1]) #(200,300)

# Tuple => List
# a = (1,2,3,4,5)
# a = list(a)
# print(a) #[1, 2, 3, 4, 5]
# a = tuple(a)
# print(a) #(1, 2, 3, 4, 5)

# List 수정 O // Tuple 수정 X
# L = list('가나다라마바사')
# L[0] = '케'
# print(L) #['케', '나', '다', '라', '마', '바', '사']

# T = tuple('가나다라마바사')
# # T[0] = '케' #error
# T = ('케',) + T[1:] #('케', '나', '다', '라', '마', '바', '사') #새로운 튜플생성
# print(T)

# 튜플 안에 수정가능한 객체들은 수정 가능하다
# t = (['가','나','다'],100,200,300)
# t[0][0] = '케'
# print(t) #(['케', '나', '다'], 100, 200, 300)

# Tuple Method
# .count(), .index()

# t = '안녕','내','이름은','후그들이야'
# print(t.count('안녕')) #1
# t = 1,2,3,4,4,4,4
# print(t.count(4)) #4

# t = '안녕','내','이름은','후그들이야'
# print(t.index('내')) #1
# t = 1,2,3,4,4,4,4
# print(t.index(4)) #3 #4가 처음나오는 index
# print(t.index(4,4)) #index 4부터 시작해서 처음 나오는 4의 index
 
## {Sets - 세트}
# {}안에 객체들을 랜덤순으로
# 중복 불가능
# 수정 불가능
# Dictionary의 키의 집합

# 중복 제거에 용이
# l = [1,2,2,3,3,3,3,4,4,4,4,5]
# l = list(set(l))
# print(l) #[1, 2, 3, 4, 5]

# 랜덤으로 저장
# S = set('가나다라마마마바바바사')
# print(S) #{'라', '나', '마', '바', '가', '다', '사'}

# 반복 불가능 객체 이용 불가
# S = set(5) #error

# 집합 연산
# a = {1,2,3,4,5}
# b = {3,4,5,6,7}
# print(a | b) #{1, 2, 3, 4, 5, 6, 7}
# print(set.union(a,b)) #{1, 2, 3, 4, 5, 6, 7}

# a = {1,2,3,4,5}
# b = {3,4,5,6,7}
# print(a&b) #{3, 4, 5}
# print(set.intersection(a,b)) #{3, 4, 5}

# a = {1,2,3,4,5}
# b = {3,4,5,6,7}
# print(a-b) #{1, 2}
# print(set.difference(a,b)) #{1, 2}

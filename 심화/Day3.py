### Day3 ###

###{객체 지향형 프로그래밍}
# 클래스 객체 vs 인스턴스 객체
# 클래스 객체로 인스턴스 객체를 만듦
# 인스턴스 객체들은 클래스 객체들의 메소드와 속성들을 상속받음
# 클래스 객체 또한 상급 클래스 객체들의 속성과 메소드들을 상속 받음

## Built in Data types
# int,float,bool,str,list,tuple,set,dict,none

## int class 객체
# int class instacne 객체를 만듦

## self 키워드
# instance 객체를 가리킴, instance 객체가 상속받게 해줌

# a = list() # a : instance , list : class
# print(a) #[]
# print(type(a)) #<class 'list'> #a가 어떤 type으로 만들어졌는가?
# print(a.__class__) #<class 'list'> #a가 어떤 클래스로 만들어졌는가?
# print(dir(a))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

## class 생성
# class 키워드 사용
# __init__ : 가장 먼저 실행
# self는 객체를 가리킨다.
# self 키워드가 없다면 객체에게 상속을 시키지 않는다.
# feature는 물론 함수(method) 또한 상속시킬 수 있다.
# class Animals:
#     def __init__(self,legs,ears,eyes):
#         self.legs = legs #lion or monkey의 legs
#         self.ears = ears #lion or monkey의 ears
#         self.eyes = eyes #lion or monkey의 eyes
#     def shout(self,sound):
#         print(f'{sound} {sound} {sound}')

# lion = Animals(4,2,2)
# print(lion) #<__main__.Animals object at 0x000001B51888D790>
# print(type(lion)) #<class '__main__.Animals'>
# print(lion.legs) #4

# monkey = Animals(2,2,2)
# print(monkey.legs)

# 구체적으로 명시 가능
# lion = Animals(legs = 4, ears = 2, eyes = 2)
# monkey = Animals(legs = 2, ears = 2, eyes = 2)

# self == lion, sound == '어흥'
# lion.shout('어흥') #어흥 어흥 어흥
# monkey.shout('끼익끼이') #끼익끼이 끼익끼이 끼익끼이

# def shout가 
# def shout(sound)로 정의되는 경우 == 상속되지 않는 경우
# Animals.shout('어흥')
# Animals.shout('끼익끼이')



## 클래스가 상급 클래스를 상속 받는 경우
# () 안에 상급 클래스명 넣기
# 상속 받는 클래스는 __init__필요 없음, 이미 상급 클래스에서 __init__ 됨
# class Animals:
#     def __init__(self,legs,ears,eyes):
#         self.legs = legs #lion or monkey의 legs
#         self.ears = ears #lion or monkey의 ears
#         self.eyes = eyes #lion or monkey의 eyes
#     def shout(self,sound):
#         print(f'{sound} {sound} {sound}')

# class Mammals(Animals):
#     def run(self):
#         print('run run run run')

# Mammals가 lion을 객체화 할 때 Animals의 init함수가 자동으로 실행
# 매개변수를 넣어줘야 함
# lion = Mammals(legs=4,ears=2,eyes=2)
# lion.run() #run run run run
# lion.shout('어흥') #어흥 어흥 어흥

# class Birds(Animals):
#     def __init__(self,legs,ears,eyes,wings):
#         Animals.__init__(self,legs,ears,eyes)
#         self.wings = wings
#     def fly(self):
#         print('fly fly fly fly')

# chicken = Birds(legs = 2, ears = 2, eyes = 2, wings = 2)
# print(chicken.legs) #2
# print(chicken.wings) #2

# chicken.fly() #fly fly fly fly
# chicken.shout('끼룩끼룩') #끼룩끼룩 끼룩끼룩 끼룩끼룩

# print(dir(chicken))
# '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ears', 'eyes', 'fly', 'legs', 'shout', 'wings']


## 실전코드
# class Person:
#     def __init__(self,name,pay,job):
#         self.name = name
#         self.pay = pay
#         self.job = job
#     def giveRaise(self,percent):
#         self.pay = self.pay * (1+percent)

# bob = Person(name = 'bob boy',pay = 1000,job = 'developer')
# print(bob.pay) #1000
# bob.giveRaise(10)
# print(f'after rasie : {bob.pay}') #11000
        
# class Manager(Person):
#     def __init__(self, name, pay, job, position = 'manager'):
#         Person.__init__(self,name,pay,job)
#         self.position = position

#     def giveRaise(self,percent,bonus = .1):
#         Person.giveRaise(self,percent + bonus)
# tom = Manager(name = 'tom boy',pay=1000,job='engineer')
# bob = Person(name = 'bob boy',pay=1000,job='developer')

# print(f'Tom Before Raise : {tom.pay}') #Tom Before Raise : 1000
# print(f'Bob Before Raise : {bob.pay}') #Bob Before Raise : 1000
# tom.giveRaise(.10)
# bob.giveRaise(.10)
# print(f'Tom Before Raise : {tom.pay}') #Tom Before Raise : 1200.0
# print(f'Bob Before Raise : {bob.pay}') #Bob Before Raise : 1100.0



## {Multiple Inheritance}
# https://youtu.be/5xXB93rX_X8?t=9962

# class Animals:
#     def __init__(self,eyes,ears):
#         self.eyes = eyes
#         self.ears = ears
    
#     def shout(self, sound):
#         print(f'{sound} {sound} {sound}')

# class Mammals(Animals):
#     def __init__(self,eyes,ears,legs,arms):
#         Animals.__init__(self,eyes,ears)
#         self.legs = legs
#         self.arms = arms
#     def run(self):
#         print('run run run')

# class Birds(Animals):
#     def __init__(self,eyes,ears,legs,wings):
#         Animals.__init__(self,eyes,ears)
#         self.legs = legs
#         self.wigns = wings
#     def fly(self):
#         print('fly fly fly')

# class Hybrid(Mammals,Birds):
#     def __init__(self,eyes,ears,legs,arms,wings):
#         Mammals.__init__(self,eyes,ears,legs,arms)
#         Birds.__init__(self,eyes,ears,legs,wings)

# unicorn = Hybrid(eyes = 2, ears = 2, legs = 4, arms = 4, wings = 2)
# print(unicorn.wigns) #2
# unicorn.run() #run run run
# unicorn.fly() #fly fly fly
# unicorn.shout('잇힝') #잇힝 잇힝 잇힝

# 객체의 searching 순서 확인, __mro__
# print(Hybrid.__mro__)
# (<class '__main__.Hybrid'>, <class '__main__.Mammals'>, <class '__main__.Birds'>, <class '__main__.Animals'>, <class 'object'>)
# 상속을 여러 번 하는 것은 추천되지 않는 프로그래밍 기법


## {Dunder Method, Magic Method}
# __~~__ 같은 form
# dir() 로 확인
# a = list()
# print(dir(a))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# __repr__
# __add__ 
# 사용 예시
# class Rand:
#     def __init__(self,start):
#         self.start = start
        
# x = Rand(100)
# print(x) #<__main__.Rand object at 0x000002283A1DCC50>

# class Rand:
#     def __init__(self,start):
#         self.start = start
#     def __repr__(self):
#         return str(self.start)
# x = Rand(100)
# print(x) #100
# print(x+100) #error

# class Rand:
#     def __init__(self,start):
#         self.start = start
#     def __repr__(self):
#         return str(self.start)
#     def __add__(self,item):
#         return self.start + item
# x = Rand(100)
# print(x+100) #200

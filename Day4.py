### Day4 ### 

## {String}

# 문자를 담고 있는 데이터
# 바뀌지 않는 열(Immutable Sequence)
# 문자 하나하나를 왼쪽 => 오른쪽 하나씩 저장

# X = '안녕하세요'
# print(X[0]) #안
# print(X[4]) #요
# print(len(X)) #5

## {String 생성 방법}

# S = ''
# print(S) #
# S = ""
# print(S) #

# 되도록 "" 추천
# S = "Craftsman's"
# print(S) #Craftsman's
# S = 'Craftsman"s'
# print(S) #Craftsman"s
# S = 'Craftsman\'s'
# print(S) #Craftsman's

# """ (Multline Quotation)

# S = """
# Cratsman Mentality
# multiline
# quotation
# """
# print(S) #Cratsman Mentality
#          #multiline
#          #quotation

# S = '''
# Cratsman Mentality
# multiline
# quotation
# '''
# print(S) #Cratsman Mentality
#          #multiline
#          #quotation

# f-string
# age = 30
# S = f'Craftsman\'s age is : {age}'
# print(S) #Craftsman's age is : 30

# String's add
# S1 = '크래프트맨 '
# S2 = '멘탈리티'
# S = S1+S2
# print(S) #크래프트맨멘탈리티

# String mul
# S = '안녕 '
# print(S*4) #안녕 안녕 안녕 안녕

# String Escape '\'

# S ='\\'
# print(S) #\

# S = 'Hello\nHi'
# print(S) #Hello
#          #Hi


## {Polymorphism 다항성}

# '가나다라' + '마바사'
# '가나다라' str instance 생성
# '마바사' str instance 생성
# add ==> '가나다라마바사' str instance 생성(new instance)
# 변수 설정 없다면 counter == 0 ==> garbage collector 
# 두 개의 str instacne 를 붙이는 것이 아니다
# 새로운 str instace 를 생성하는 것
# 문자열은 수정이 불가하기 때문에 new instacne 를 만드는 것

# '가나다라'*4
# '가나다라' str instance 생성
# '가나다라가나다라가나다라가나다라' str instance 생성
# 변수 설정 없다면 counter == 0 ==> garbage collector

# print('가나다라'+100) #error

## {String 'in' test}

# '가' in '가나다라' # '가' 가 '가나다라' 문자열에 존재하는가?
# print('가'in'가나다라') #True
# print('가다' in '가나다라') #False #서로 떨어짐
# print('나다' in '가나다라') #True

## {String Indexing}

# S = '가나다라'
# print(S[0]) #가
# print(S[3]) #라
# print(S[-1]) #라 #last index == -1, first로 갈수록 -1
# print(S[-4]) #가 #fist index == last index -3 == -4

## {String Slicing}

# S = '가나다라마바사'
# print(S[1:3]) #나다 # 1~before3
# print(S[1:]) #나다라마바사 1~entire
# print(S[:-1]) #가나다라마바 first ~ before-1
# print(S[-7]) #가
# print(S[1:-1:2]) #나라바 1~before-1, 2칸씩 건너뛰기
# print(S[::2]) #가다마사 all,2칸씩 건너뛰기

## {String 전환}

# '100'+300 #error
# print(int('100')+300) #400
# print(int('10a'+300)) #error , only 숫자만

## {String은 수정이 불가능}
# 수정하려면 새로운 문자열을 만들어야 함
# == 새로운 객체를 생성
# S = '가나다라마바사'
# S[0] = '케' #error
# S = '케' + S[1:]
# print(S) #케나다라마바사
# https://youtu.be/j8vXaGMJxQI?t=11143

# replace()
# 새로운 instance가 생성됨.
# S = '가나다라마바사'
# S = S.replace('가','케') #가 => 케
# print(S) #케나다라마바사
# https://youtu.be/j8vXaGMJxQI?t=11327

## {String Method}

# replace(), upper(), lower(), count(), index()...
# String Method로 새로운 String instance가 만들어짐

# .join()
# l = ['안녕','내','이름은','크래프트맨','멘탈리티야']
# s1 = '@'.join(l)
# print(s1) # 안녕@내@이름은@크래프트맨@멘탈리티야
          # 리스트의 객체들을 각각 join 이때 ''안에 내용을 넣어줌

# .replace()
# email1 = 'craftsmanmnetality@gmail.com'
# email2 = email1.replace('gmail','naver')
# print(email1) #craftsmanmnetality@gmail.com
# print(email2) #craftsmanmnetality@naver.com

# .split()
# 리스트 형태로 나눠짐
# email1 = 'crfatsmanmnetality@gmail.com'
# email2 = email1.split('@')
# print(email1) #crfatsmanmnetality@gmail.com
# print(email2) #['crfatsmanmnetality', 'gmail.com']
# email3 = '@'.join(email2)
# print(email3) #crfatsmanmnetality@gmail.com
# print(email1 is email3) #False
# print(email1 == email3) #True

# .format()
# name = 'rlaxodud7737'
# symbol = '@'
# email = 'naver.com'

# my_email = '{}{}{}'.format(name,symbol,email) 
# print(my_email) #rlaxodud7737@naver.com
# print(f'{name}{symbol}{email}') #rlaxodud7737@naver.com

## {List}
 
# 문자열과 다르게 변경 가능
# 객체의 메모리 주소 하나하나를 차례대로 저장
# https://youtu.be/j8vXaGMJxQI?t=11885
# [] 를 이용
# 모든 객체를 넣을 수 있다.
# in, float, str, list, dict, tuple, sets, None, bool, fucntions, methods

# L = []
# L = [1,2,3]
# L = ['abcd',100,1.23]
# L = [[1,2,3],[4,5,6],[7,8,9]]
# L = [str.replace,list.append,print,len]
# L[2]("this is print fucntion " + str(L[3](L))) #this is print fucntion 4

# List Operation - 리스트연산
# print([1,2,3]+[4,5,6]) #[1, 2, 3, 4, 5, 6]
# print([1,2,3]*3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]
# print([1,2,3]+100) #error #서로 다른 객체

# List in test
# print(100 in [100,200,300]) #True
# print([100,200] in [100,200,300]) #False

# List indexing
# L = [100,200,300,400]
# print(L[0])
# print(L[3])

# List Slicing
# L = [100,200,300,400,500,600,700]
# print(L[1:3]) #[200,300]
# print(L[1:-1:2]) #[200, 400, 600]

# List 전환
# ['a','b'] + 'c' #error
# print(str(['a','b'])+'c') #['a', 'b']c
# print(['a','b']+list('c')) #['a', 'b', 'c']
# a = (1,2,3,4,5)
# b = '크래프트맨'
# c = 100
# print(list(a)) #[1, 2, 3, 4, 5]
# print(list(b)) #['크', '래', '프', '트', '맨']
#print(list(c)) #error #int은 불가!(반복불가능)
# print([c]) #100

# List는 수정 가능한 열 1
# 1. 리스트 수정
# L =list('가나다라마바사')
# https://youtu.be/j8vXaGMJxQI?t=12839
# L[0] = '케'
# https://youtu.be/j8vXaGMJxQI?t=12849
# print(L) #['케', '나', '다', '라', '마', '바', '사']
# 2. 새로운 리스트
# L = list('가나다라마바사')
# L = ['케']+L[1:]
# https://youtu.be/j8vXaGMJxQI?t=12863
# print(L) #['케', '나', '다', '라', '마', '바', '사']

# List는 수정 가능한 열 2
# L = list('케나다라마바사')
# L[3:6] = list('벤쿠버') 
# print(L) #['케', '나', '다', '벤', '쿠', '버', '사']
# L[6:6] = ['최','고'] 
# print(L) #['케', '나', '다', '벤', '쿠', '버', '최', '고', '사']
# L[0:3] = []
# print(L) #['벤', '쿠', '버', '최', '고', '사']

# List Method

#.append()
# in-place replacement ('수정' 하는 메소드, return 값이 없음(None))
# L = ['안녕','헬로우']
# L.append('반가워')
# print(L) #['안녕', '헬로우', '반가워']
# L = L.append('반가워')
# print(L) #None

#.extend()
# List를 추가(하나 이상의 데이터)
# L = ['안녕','헬로우']
# L.extend(['정말','반가워'])
# print(L) #['안녕', '헬로우', '정말', '반가워']
# # == 
# L = ['안녕','헬로우']
# L[3:] = ['정말','반가워']
# print(L) #['안녕', '헬로우', '정말', '반가워']
# # ==
# L = ['안녕','헬로우']
# L[len(L):] = ['정말','반가워']
# print(L) #['안녕', '헬로우', '정말', '반가워']

#.sort()
# 가나다 순으로 정렬
# 수정하는 함수, return값 == None
# L = ['나비','소세지','과일','바나나']
# L.sort()
# print(L) #['과일', '나비', '바나나', '소세지']
# L2 = L.sort()
# print(L2) #None

#.reverse()
# 역순으로 정렬
# L = ['나비','소세지','과일','바나나']
# L.reverse() #in place replacement
# print(L) #['바나나', '과일', '소세지', '나비']
# ==
# L = ['나비','소세지','과일','바나나']
# L = L[::-1] #new list created
# print(L) #['바나나', '과일', '소세지', '나비']

#.pop()
# 마지막 값 삭제
# return 값 존재, 마지막값
# L = ['나비','소세지','과일','바나나']
# print(L.pop()) #바나나
# print(L) #['나비', '소세지', '과일']

#.insert(index,contents)
# 해당 index를 뒤로 밀고 값 삽입.
# return 값 없음, None
# 매개변수 2개 필요
# L = ['나비','소세지','과일','바나나']
# L.insert(1,'반가워')
# print(L) #['나비', '반가워', '소세지', '과일', '바나나']
# L = ['나비','소세지','과일','바나나']
# L.insert(1,['정말','반가워'])
# print(L) #['나비', ['정말', '반가워'], '소세지', '과일', '바나나']
# L = ['나비','소세지','과일','바나나']
# L.insert(1,('정말','반가워'))
# print(L) #['나비', ('정말', '반가워'), '소세지', '과일', '바나나']
# L = ['나비','소세지','과일','바나나']
# L.insert(1,'정말')
# L.insert(1,'반가워')
# print(L) #['나비', '반가워', '정말', '소세지', '과일', '바나나']
 




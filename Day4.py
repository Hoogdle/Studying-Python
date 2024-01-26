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

# https://youtu.be/j8vXaGMJxQI?t=10858
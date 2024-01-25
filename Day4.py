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

S = ''
print(S) #
S = ""
print(S) #

# 되도록 "" 추천
S = "Craftsman's"
print(S) #Craftsman's
S = 'Craftsman"s'
print(S) #Craftsman"s
S = 'Craftsman\'s'
print(S) #Craftsman's

# """ (Multline Quotation)

S = """
Cratsman Mentality
multiline
quotation
"""
print(S) #Cratsman Mentality
         #multiline
         #quotation

S = '''
Cratsman Mentality
multiline
quotation
'''
print(S) #Cratsman Mentality
         #multiline
         #quotation

# f-string
age = 30
S = f'Craftsman\'s age is : {age}'
print(S) #Craftsman's age is : 30

# String's add
S1 = '크래프트맨 '
S2 = '멘탈리티'
S = S1+S2
print(S) #크래프트맨멘탈리티

# String mul
S = '안녕 '
print(S*4) #안녕 안녕 안녕 안녕

# String Escape '\'

S ='\\'
print(S) #\

S = 'Hello\nHi'
print(S) #Hello
         #Hi

# https://youtu.be/j8vXaGMJxQI?t=10367
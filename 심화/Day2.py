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
my_list = [1,[2,[3,4],5],6,[7,7]]

def adding_machine(x):
    num = 0
    for item in x:
        if not isinstance(item,list):
            num += item
        else:
            num += adding_machine(item)
    return num

print(adding_machine(my_list))
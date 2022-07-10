# Python tutorial 5. Data Structures

from xml.etree.ElementInclude import LimitedRecursiveIncludeError


liist = [0, 1, '2']

#list.append(x) # == a[len(a):] = [x]
liist.append('x')
print(liist)

x = liist.remove('x') # List목록 중 처음으로 나오는 'x'를 제거한다. 만약없으면 error발생.
print(liist)

liist.extend('x')
print(liist)

liist.insert(3, 'sam') #지정 index에 항목 삽입.
print(liist)

liist.pop(3) #index 3을 제거후 반환
print(liist)
liist.insert(3, 3)


#list.index(x[, start[, end]]) == 값이x와 같은 첫 번째 항목의 목록에서 0부터 시작하는 index 반환.

liist.count(3)
print(liist)


#liist.sort(*, key=None, reverse=False)
#print(liist)


liist.reverse() #뒤집기
print(liist)

liist.copy()
print(liist)


liist.clear() # 모두 지우기
print(liist)







#5.1.1. Using List as Stacks
#List method를 사용하면, List를 stack(스택)으로 매우 쉽게 사용할수있다.
#stack이란? https://gmlwjd9405.github.io/2018/08/03/data-structure-stack.html
           # 한쪽 끝에서만 자료를 넣고 뺄수있는 LIFO(Last in First out)형식 자료 구조
           #pop() = 스택에서 가장 위의 항목 제거
           #push(item) = item하나를 스택의 가장 윗부분에 추가.
           #peek() = 스택의 가장 위에 있는 항목 반환
           #isEmpty() = 스택이 비어있을때, true반환.
           #재귀알고리즘을 쓸 경우, 스택이 유용하다고함.
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop() #7이 반환..
print(stack)

stack.pop() #6
stack.pop() #5

print(stack) #3,4




#5.1.2 Using Lists as Queues
## Queue == 대기열
from collections import deque
queue = deque(["eric", "john", "micheal"])
queue.append("terry")
queue.append("Graham")
queue.popleft() #왼쪽의 요소를 꺼낸다.(index0)
queue.popleft()
print(queue) #추가된 2인, eric john은 빠져나간 최종형태.




#5.1.3
#for 문 활용한 예.
squares = []
for x in range(10): #arg x 에 0이상~10미만(range)의 숫자를 대입 한다.
    squares.append(x**2)

print(squares)

squares2 = list(map(lambda x : x**2, range(10))) #위의껄 람다식으로 더 간단하게.
print("squares2 : ", squares)


squares3 = [x**2 for x in range(10)] # 더 간단하게 나타냄.
print("squares3 : ", squares3)



print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]) #조건문도 섞어서..(1,1), (3,3)같은건 제외할려할떄.
#위와같음
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)



#for문 응용예시1
babo = [4, -2, -35523 ,6, 7, 1235, 452, 3]
print([x**2 for x in babo])

#2
print([x**2 for x in babo if x >= 0])

#3
print([abs(x) for x in babo]) # 0에서 떨어져있는 절대값(거리) = 음수도양수로..

#4
from math import pi
print([str(round(pi, i)) for i in range(5, 13)]) #strings 형태의 자료형으로 list에 담는다.
#pi값을 소수점 i자리수의 정확도로 라는뜻(round)




#5.1.4 List의 Nesting 
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
] #tensor와 비슷한 느낌.

print([[row[i] for row in matrix] for i in range(4)]) #list안에 list를 넣을 수 있다.





#5.2 del 문
#pop문은 값을 반환, del은 값을 지우거나, List전체를 "지움" 그래서 다름.

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

#del a
#print(a) = 변수 자체를 지워서 오류뜸. 아예 변수자체를 지울수도있다.








#5.3 Tuple, Sequences
#tuple
tup = 12345, 54321, 'hello!'
print(tup[0])
print(tup)

#튜플의 Nesting
u = tup, (1,2,3,4,5)
print(u)

#튜플의 값은 바꿀 수 없다.
#tup[0] = 88888 #<<<안됨.
print(tup)


#튜플에 요소가 하나만있다면? 쉼표를 써서 구분하라. (그냥 문자열이되는걸 막고 튜플이되게하기.)
empty = ()
singleton = 'hello',
print('length of empty tuple : ', len(empty))
print('length of tuple singleton :', len(singleton))






#5.4 Sets
#Sets (집합)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket) #True or False
print('babou' in basket)


#집합: 합집합, 교집합, 차, 대칭같은 연산이 가능함.
a = set('abracadabra')
b = set('alacazam')

print(a) #나오는 문자

print(a-b) #차집합(중복 문자 제거
print(a | b) #합집합
print(a & b) #교집합
print(a ^ b) #중복되지 않은 문자 (합집합-교집합?)





#5.5 Dictionaries
#데이터유형중 "사전"
tel = {'jack': 4098, 'sape': 4139} #이런식으로 딕셔너리형 자료형을 만들 수 있다.
tel['guido'] = 4127
print(tel)

tel['jack']

del tel['sape']
tel['irv'] = 4127

print(tel)

sa = list(tel)
print(sa)

saso = sorted(sa)
print(saso)

print('guido' in tel)
print('jack' not in tel)




#5.6 반복 기술
#딕셔너리를 반복할때, items() 메소드를 사용하여 키, 해당값을 동시 검색가능.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v)
#k v 가 각각 키와 값으로 나온 모습


for i, fg in enumerate(['tic', 'tac', 'toe']):
    print(i,fg)



basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket): #리스트안의 내용물을 섞는다.
    print(i)




#5.7 조건에대한 추가 정보
#While, if에는 비교만이 아닌, 모든 연산자 사용 가능.
#a < b == c 는 a가 b보다 작고, b가 c와 같은지 테스트.
saro = 143
mb14 = 140
nme = 138

print(saro > mb14 > nme)
print(saro > mb14 == nme) #2가지 다 맞아야 함.

string1, string2, string3 = '', 'babo', 'soraka'
non_null = string1 or string2 or string3
print(non_null)




#5.8 시퀀스와 다른 개채의 비교
print((1, 2, 3)              < (1, 2, 4))
print([1, 2, 3]              < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4)           < (1, 2, 4))
print((1, 2)                 < (1, 2, -1))
print((1, 2, 3)             == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))
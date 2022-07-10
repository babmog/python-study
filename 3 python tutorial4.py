#More control flow tools

#if, elif(else if..)

#for - 모든 시퀀스(List of Strings)
from distutils.log import error


words = ['cat','window','defenestrate']
for w in words:
    print(w, len(w))





#range - 일련의 숫자를 반복해야 하는 경우. 숫자를 순서대로 진행.
for i in range(5):
    print(i)


print(list(range(5, 244, 35)))





#4.5 pass - 그냥 지나침(패스함) - 구문적으로 써야하지만, 프로그램에 조치가 필요하지 않을때 사용.
#while True:
#    pass


#4.6 match - 표현식을 취하고, 그값을 연속 패턴과 비교..
#def http_error(status):
    #match status:
     #   case 400:
      #      return "Bad request"
       # case 404:
        #    return "Not found"
        #case 418:
        #    return "I'm a teapot"
        #case _:
        #    return "Something's wrong with the internet"




## 패턴은 정수를바인딩 하는데 사용 할 수도. - 바인딩이란?: 어떤 프로그램에 사용된 구성요소의 실제 값을 결정짓는 행위.
# point is an (x, y) tuple
#match point:
  #  case (0, 0):
   #     print("Origin")
   # case (0, y):
   #     print(f"Y={y}")
   # case (x, 0):
   #     print(f"X={x}")
   # case (x, y):
   #     print(f"X={x}, Y={y}")
   # case _:
   #     raise ValueError("Not a point")



# 4.7 함수 정의
# def fib(n) << fib라는 함수를 정의하기. 그 밑에 들여쓰기로 함수의 내용을 쓴다. n은 매개변수(arg)

#xx.append(a) --> 자료 a를 xx라는 list마지막 원소 뒤에 추가.
ssar = [1, 2, 3, '4', 5]
ar = ["lyuk"], 'babo' #list 안에 list 추가 할수도있다.
ssar.append(ar)
print(ssar)



def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        return result #return을 이용, 함수 외부로 값을 전달한다(output) --> 쓰는이유: 함수 내부에서 일어난 일은 함수 외부에서 알 수 없기 때문! = 함수의 "결과값"이라 보면됨.

print(fib2(100))





#4.8 함수정의2
#4.8.1 - 기본인수값 - 아래함수: 인풋값으로 prompt값을 받는다.
#def ask_ok(prompt, retries=4, reminder='Please try again!'):
#    while True:
#        ok = input(prompt)
#        if ok in ('y', 'ye', 'yes'):
#            return True
#        if ok in ('n', 'no', 'nop', 'nope'):
#            return False
#        retries = retries - 1
#        if retries < 0:
#            raise ValueError('invalid user response')
#        print(reminder)


i = 5
def f(arg=i):
    print(arg)

i = 6
f() #arg가 기본적으로 i로 설정되어있다.


#arg에 List를 넣음. return으로 L이 빠져나오니, 다시 함수를 호출할때 그 return된 L값이 또 들어감. 그래서 114~116줄의 코드를 거치면서 리스트길이가 늘어남.
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3)) #함수를 쓸수록? 반복될수록 계속 추가 (f3을 114줄에 옮기면 순서가 다르게 됨.)



#4.8.2
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


##이건 안됨.
#parrot()                     # 필수 arg 누락(voltage)
#parrot(voltage=5.0, 'dead')  # 키워드arg뒤에 키워드가 아닌 인수.
#parrot(110, voltage=220)     # 동일한 인수에대한 중복 값(voltage, voltage)
#parrot(actor='John Cleese')  # actor은 arg목록에 없음.




#사전형 : **(2개랑 쌍을 이루는 자료형 key/value)
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])



cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")






#4.8.3 - 특수 arg

#아래: /, * 는 arg가 함수에 전달되는 방식에따라 arg의 종류를 나타냄(position, /: pos or keyword, * : keyword only)
#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      #-----------    ----------     ----------
      #  |             |                  |
      #  |        Positional or keyword   |
      #  |                                - Keyword only
      #   -- Positional only

#positional arg: 자리요소
#keyword arg: 
#


#standard arg - 호출 규칙에 제한을 두지 않음. arg는 pos or keyword로 전달 될 수 있다.
#standard_arg(2) = 2
#standard_arg(arg=2)= 2



#pos only arg
#pos_only_arg(1) = 1
#pos_only_arg(arg = 1) = error



#keyword인수
#kwd_only_arg(3) = error
#kwd_only_arg(arg=3) = 3 -- 이유 모르겠다..




#4.8.3.5 요약 : 사용자가 매개변수의 이름을 사용할수없도록 하려면, 위치전용을 사용하라.
#이름에 의미가있고, 이름을 명시적으로 지정하여 함수 정의를 더 이해하기 쉽게 하거나, 전달되는 인수의 위치에 의존하는 사용자를 방지하려는 경우, keyword전용을 사용.






#4.8.4 임의 인수 lists : 임의의 수의 인수로 함수를 호출. : 가변 인수 앞에 0개 이상의 일반 인수가 발생할 수 있다. (튜플에 래핑됨)




#4.8.5 인수 목록 풀기.
#인수가 이미 목록이나 튜플에 있지만, 별도의 위치 인수가 필요한 함수 호출을 위해 압축을 풀어야 하는 경우.
lows = list(range(3,6))
print(lows)

args = [3, 6]
print(list(range(*args))) #list에서 압축을 푼 인수로 호출. = list형에서 대괄호를 없애는 역할?(그냥 args로 하면 정수형만 사용가능하다고 나오면서 에러뜸.)




#4.8.6 람다 표현식.
#lambda를 사용, lambda a, b: a+b
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))




def babo(x):
    return x + n






def add(x):
    return x + 3

c = add
print(c(3))
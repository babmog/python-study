#python tutorial 3..

sa = 2 + 2
print(sa)

# 50 - 5 * 6 << SC와 다르게 일반 수학처럼 연산.
# ** = 제곱


word = 'python'

sa = word[-1]
print(sa)

sa = word[-2:]
print(sa)

sa = word[3:42]
print(sa)

sa = word[42:]
print(sa)

sa = 'J' + word[1:]
print(sa)

sa = word[:2] + 'py'
print(sa)






s = 'newbesupercolliderman'
print(len(s))







#3.1.3 Lists
squares = [1, 4, 9, 16, 25]
print(squares[-1])

print(squares[-3:])

print(squares[:])

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1]) # List안의 List, index0의 리스트안의 index1을 찾는다는 말인듯.(슈퍼콜라이더에서도 비슷한 걸 봤음.)

sar, go = 0, 1
while sar < 10:
    print(sar)
    sar, go = go, sar + go




#string - \n
print('C:\some\name')
print(r'C:\some\name')
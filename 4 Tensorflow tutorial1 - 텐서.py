import tensorflow as tf

#https://www.tensorflow.org/guide/tensor
#Tensorflow - 기본사항: "텐서"

#텐서는 다차원 배열.(dtype) 지원되는 모든 dtypes는
#tf.dtypes.DType 에서 볼수있다.



#기본 텐서 만들어보기.
rank_0_tensor = tf.constant(4)
print(rank_0_tensor)

#tf.Tensor(4, shape=(), dtype=int32) ==> int32 = 32bit.

rank_1_tensor = tf.constant([2.0, 3.0, 4.0]) #실행시키면 텐서2. , 3. ,4.가 만들어지고,
#shape는 3(도형의 모양 = 3각형), dtype = 32비트소수로 생성되는걸 볼 수 있다.
print(rank_1_tensor)


rank_2_tensor = tf.constant([[1. , 2.], [3., 4.], [5., 6.]])

#3개의 축의 텐서 사용.
rank_3_tensor = tf.constant([
    [[0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9]],
    [[10, 11, 12 ,13 ,14],
    [15, 16, 17, 18, 19]],
    [[20, 21, 22, 23, 24],
    [25, 26,27, 28, 29]],])

print(rank_3_tensor) #리스트안의 리스트안의 리스트, 3/2/5각형







#Tensor의 연산(덧셈, 요소별 곱셈, 행렬곱셈 등)이 가능하다.
a = tf.constant([[1, 2],[3, 4]])
b = tf.constant([[5, 6], [7, 8]]) # Could have also said 'tf.ones([2, 2])'

print(tf.add(a, b), "\n") # ""add"" ==> tf.add = tensor를 더한다. 
print(tf.multiply(a, b), "\n") #""multiply"" ==> tf.multiply = 텐서를 곱한다.
print(tf.matmul(a, b), "\n") # ""matmul"" ==> tf.matmul = 행렬곱셈.

#행렬곱셈: 두개의 행렬에서 한개의 행렬을 만들어내는 이항연산. https://ko.wikipedia.org/wiki/행렬_곱셈
    #첫째 행렬의 열 갯수와 둘째 행렬의 행 갯수가 동일해야 한다. 곱셈을하여 만들어진 행렬은
        #첫째 행렬의 행갯수와 둘째 행렬의 열 갯수를 가진다.(세로, 가로)
        #첫째 행렬의 행(가로축 일렬의 원소들)과 둘쨰 행렬의 열(세로축들)이 만나 행렬곱의 요소가 형성.
        #첫째 행렬의 행의 1열x둘째 행렬의 해당열의 1행 + 2열*2행 .... 한 모든 합이 matmul로 만들어지는 해당 행렬의 행/열원소가 된다.
        #결론: 1*5 + 2*7 = 19, 1*6 + 2*8 = 22, 3*5 + 4*7 = 43, 3*6 + 4*8 = 50


#3차원 행렬곱셈도 한번 해보자..
c = tf.constant([[[1, 2], [3,4]], [[5,6],[7,8]],[[9,10],[11,12]]])
d = tf.constant([[[13, 14], [15,16]], [[17,18],[19,20]],[[21,22],[23,24]]])
print(tf.add(c,d), "\n")
print(tf.matmul(c, b), "\n")




print(a + b, "\n") # = tf.add
print(a * b, "\n") # = tf.multiply
print(a @ b, "\n") # = tf.matmul

e = tf.matmul(c,d)
fll = tf.constant([[4.0, 5.0], [10.0, 1.0]])

#다른 연산
print(tf.reduce_max(e)) #가장 큰값을 찾는다.
print(tf.argmax(e)) #가장 큰 값의 index를 찾는다.
print(tf.nn.softmax(fll)) #softmax 계산 !!!!정수형이면 계산 안되는듯.
#softmax? - 입력받은 값을 0~1사이의 값으로 모두 정규화 한다. (최소값0, 최댓값 1)
    #정수형으로 되어있는걸 float형으로 바꿔야 정규화 할수있는듯... 나중에 쓸때 dtype를 바꾸거나 하는식으로 해보자.








#형상 정보.
#Tensor는 형상이있다. 사용되는 용어들
    #형상 shape: 텐서의 각 차원의 길이(요소의 수)
    #순위 Rank: 텐서 축의수
    #축 or 차원 Dimension : Tensor의 특정 차원
    #크기 size : 텐서의 총 항목수, 곱 형상 벡터

rank_4_tensor = tf.zeros([3, 2, 4, 5])

print(rank_4_tensor) #리스트안의^4, 3,2,4,5각형의 텐서를 만들고 각 리스트요소는 다 0.으로 넣는다.


print("Type of every element:", rank_4_tensor.dtype) #32비트 float
print("Number of dimensions:", rank_4_tensor.ndim) #차원의 수 =4
print("Shape of tensor:", rank_4_tensor.shape) #각형- 3,2,4,5
print("Elements along axis 0 of tensor:", rank_4_tensor.shape[0]) 
print("Elements along the last axis of tensor:", rank_4_tensor.shape[-1]) #텐서 마지막 차원에 있는 요소(index-1이니..)
print("Total number of elements (3*2*4*5): ", tf.size(rank_4_tensor).numpy()) # size
#.dtype, .ndim, .shape[index], .numpy








#Tensor의 indexing
    #numpy나 표준 파이썬 인덱싱 규칙을 그대로 따름
    #numpy: 행렬이나 다차원 배열을 쉽게 처리할수있도록 지원하는 파이썬 라이브러리.
    #index는 0부터 시작, -1, -2는 끝에서 1,2번째부터 거꾸로 계산.

rank_1_tensor = tf.constant([0, 1, 1, 2, 3, 5, 8, 13, 21 ,34])
print(rank_1_tensor.numpy())

#스칼라를 사용하여 인덱싱하면 축 제거.(차원이 줄어듬) 
print("First:", rank_1_tensor[0].numpy())
print("Second:", rank_1_tensor[1].numpy())
print("Last:", rank_1_tensor[-1].numpy())
#- 2차원이면??
print("Last:", a[-1].numpy()) #2차원 텐서를쓰니, 1차원으로 차원이 1개 줄어듬.


# : 를 사용하여 인덱싱하면 차원 유지됨.
print("Everything:", rank_1_tensor[:].numpy())
print("Before 4:", rank_1_tensor[:4].numpy())
print("From 4 to the end:", rank_1_tensor[4:].numpy())
print("From 2, before 7:", rank_1_tensor[2:7].numpy())
print("Every other item:", rank_1_tensor[::2].numpy()) #인덱스를 +1씩하는게아닌, -2씩 계산
print("Reversed:", rank_1_tensor[::-1].numpy()) #인덱스를 +1씩하는게아닌, -1씩 계산.






#다축인덱싱 (다차원 인덱싱)
#높은 Rank의 텐서는 여러 index를 써서 인덱싱해야함.
#단일차원의 경우와 같은규칙이 각 차원에 독립적으로 적용.
print(rank_2_tensor.numpy())

#이제 각 index에 정수를 전달하면..
print(rank_2_tensor[1, 1].numpy()) #indexing은 0부터하니, 가로,세로로 2번째에 있는 원소(4.0)이 나옴.

#3차원은?
print(rank_3_tensor[1,1,2].numpy()) #된다.

#슬라이스 조합
print("Second row:", rank_2_tensor[1, :].numpy()) #세로->가로순. !!!!바깥 괄호부터 indexing하는거임!!!!
print("Second column:", rank_2_tensor[:, 1].numpy())
print("Last row:", rank_2_tensor[-1, :].numpy())
print("First item in last column:", rank_2_tensor[0, -1].numpy())
print("Skip the first row:")
print(rank_2_tensor[1:, :].numpy(), "\n")
#row가 세로축을 의미하는듯.....







#Tensor의 형상 조작하기..

#.shape = 각 차원의 크기를 보여주는 method
var_x = tf.Variable(tf.constant([[1], [2], [3]]))
print(var_x.shape)


#이걸 python list로 변경(자료형변환) 할 수도있다.!!
print(var_x.shape.as_list())


#텐서를 새로운 형상으로 바꾸기
reshaped = tf.reshape(var_x, [1,3])

print(var_x.shape)
print(reshaped.shape)
print(reshaped) #3,1에서 1,3으로 바뀜. 제일 끝에나오는숫자가 제일 안쪽차원.[[], [], []] --> [[ , , ]]


#텐서를 평평하게(차원을 없앤다?) 해보자. 그러면 어떤 순서로 메모리에 배치되어 있는지 확인 가능하다.
print(rank_3_tensor)
#shape의 argument -1은 "무엇이든 맞는것"이라는 뜻.
resa = tf.reshape(rank_3_tensor,[-1])
print(resa) #1차원 리스트로 바뀜.

#보통 tf.reshape는 인접한 차원을 결합하거나 분할하는것으로 쓴다.
print(tf.reshape(rank_3_tensor, [3*2, 5]), "\n")
print(tf.reshape(rank_3_tensor, [3, -1]))

#형상변경할경우, 축의 순서를 고려하지 않으면 별로 쓸모가 없다.
#tf.reshape에서 축교환이 작동하지 않으면 tf.reanspose가 있다.

#안좋은 예시들 : reshape로 축을 재 정렬 할 수 없다.
print(tf.reshape(rank_3_tensor, [2, 3, 5]), "\n")
print(tf.reshape(rank_3_tensor, [5, 6]), "\n")
#이건 아예 안됨.
try:
    #tf.reshape(rank_3_tensor, [7, -1]) #30개의 값이 있는 텐서인데, 여기에선 7의 배수의 텐서가 있어야 제대로 딱 맞게 완성됨.
    tf.reshape(rank_3_tensor, [1, -1]) #reshape가 안됨.

except Exception as e:
    print(f"{type(e).__name__}: {e}")
#참고: try - except : try에 실행할 코드를 넣고 except에 예외가 발생했을때 처리하는 코드를 넣는다.






#브로드캐스팅
#Numpy의 해당 특성에서 빌린 개념. - 특정 조건에서 작은 텐서는 결합된 연산을 실행할 때 더 큰 텐서에 맞게 자동으로 "확장(streched)" 됨
#간단하고, 일반적 경우. - 스칼라에 텐서를 곱하거나 추가할때. - 스칼라는 다른 인수와 같은 형상으로 브로드캐스트 됨.
x = tf.constant([1, 2, 3])

y = tf.constant(2)
z = tf.constant([2, 2, 2])

print(tf.multiply(x, 2))
print(x * y) #y가 x의 차원의 크기에 맞춰 [2,2,2]로 바뀜.
print(x * z)

#1차원도 다른 인수와 일치하도록 확장 가능.
x = tf.reshape(x, [3,1]) #([1], [2], [3])
y = tf.range(1, 5) #[1, 2, 3, 4] --> 1이상 4미만이니 .. 4개.
print(x, "\n") #2차원 : 3x1 
print(y, "\n") #1차원: 4 --> 안쪽차원으로 계산하는듯. (2차원으로 변환될때 1x4..)
print(tf.multiply(x, y)) #[3,4]형태(shpae)의 텐서가 만들어 짐. x의 [1] --> [1,1,1,1], y의 [1,2,3,4] --> [1,2,3,4], [1,2,3,4], [1,2,3,4]

#broadcast_to의 2번째 인수는 shape(3,3)이라는 뜻. --> 현재 1,3의 형태를 3,3으로 브로드캐스팅하라 --> [1,2,3],[1,2,3],[1,2,3]
print(tf.broadcast_to(tf.constant([1,2,3]), [3,3]))


#훨씬 복잡한 예시.
# https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html











#비정형 텐서
#어떤 축을 따라 다양한 수의 요소를 가진 텐서를 비정형(ragged)라고 한다.
ragged_list = [
    [0,1,2,3],
    [4,5],
    [6,7,8],
    [9]
]


#try: #시도한다.
   # tensor = tf.constant(ragged_list)
#except Exception as e: #시도중 e를 제외하고.
    #print(f"{type(e).__name__}: {e}")

ragged_tensor = tf.ragged.constant(ragged_list)
print(ragged_tensor)

print(ragged_tensor.shape) #비정형텐서의 형상(shape)확인하기. - 알수없는 길이의 일부 차원이 나옴.(none)
#[ .. ], [], [] []로 바깥차원은 4개의 요소가있지만, 그 안의 요소는 몇개인지 비정형적이라 shape에 안쪽차원 수가 안나옴.







#문자열 텐서
#문자열텐서는 원자성이다. python 문자열같은 방식으로 인덱싱 할 수 없다. 
#문자열의 길이는 텐서의 축 중 하나가 아니다.
scalar_string_tensor = tf.constant("Gray wolf")
print(scalar_string_tensor) #shape에 안뜸.(문자열길이는 차원으로 안침. - python의 string index의 개념으로 생각하지 말것.)


tensor_of_strings = tf.constant(["Gray wolf", "Quick brown fox", "Lazy dog"])

print(tensor_of_strings) #문자열 3개라 (3,)차원으로 뜸., 앞의 문자열 텐서앞의 b는(실행하면) 유니코드문자열이나닌, 바이트 문자열을 나타낸다.
#Tensorflow에서 유니코드 텍스트를 처리하는 자세한 내용은 유니코드튜토리얼 참고
#https://www.tensorflow.org/tutorials/load_data/unicode



emo = tf.constant("🥳👍")
print(emo)



print(tf.strings.split(scalar_string_tensor, sep=" ")) #tensor 분할하기. 공백(" ")을 "빼고", 기준으로 나눔.
#.split ==> .strings 메소드. 문자열을 "분할" 한다. 2번째 arg는 분할할 기준을 찾기.
print(tf.strings.split(scalar_string_tensor, sep="o")) #o가사라지고 Gray w, lf가 남음.


#tf.string.to_number:
text = tf.constant("1 10 100")
print(tf.strings.to_number(tf.strings.split(text, " ")))
#숫자로 구성된 문자열을 공백을 빼고 각자의 텐서로 변환되면서 .to_number 메소드를 이용해 숫자로 변환.
#.to_number ==> .strings메소드. 해당 문자열을 부동소수점형으로(float32) 변환.



#문자열 각 단어를 바이트로 변환.(한글자씩..)
byte_strings = tf.strings.bytes_split(tf.constant("Duck"))
#그 변환된 바이트문자들의 문자값(숫자)을 만든다.
byte_ints = tf.io.decode_raw(tf.constant("Duck"), tf.uint8)
print("Byte strings:", byte_strings)
print("Bytes:", byte_ints)




# 유니코드로 분할 후 디코딩.
unicode_bytes = tf.constant("アヒル 🦆")
unicode_char_bytes = tf.strings.unicode_split(unicode_bytes, "UTF-8")
unicode_values = tf.strings.unicode_decode(unicode_bytes, "UTF-8")

print("\nUnicode bytes:", unicode_bytes)
print("\nUnicode chars:", unicode_char_bytes)
print("\nUnicode values:", unicode_values)






#희소텐서
#SparseTensor를 만든다. arg: indeces: [N, ndims] -- N은값, ndims는 차원수 : index0,0 , 1,2인값이 0이 아닌 값을 갖도록 지정.
#                     values: [N]: 각 index(0이 아닌값)의 값을 정해준다.
#                    dense_shape: [ndims] - 희소텐서의 shape를 정해준다(2차원, 3x4형)
sparse_tensor = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]],
                                        values=[1, 2],
                                        dense_shape=[3, 4])

print(sparse_tensor, "\n")
#위의 희소 텐서를 고밀도로 변환
print(tf.sparse.to_dense(sparse_tensor))














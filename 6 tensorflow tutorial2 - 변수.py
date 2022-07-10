#6 tensorflow tutorial2 - 변수

import tensorflow as tf


#https://www.tensorflow.org/guide/variable
#텐서플로우 기본사항 - 2: 변수


#변수 만들기
my_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])
my_variable = tf.Variable(my_tensor) #tf.constant로 텐서를 만들고 그걸 변수로 만든 모습.

#변수는 텐서처럼 모든 종류의 유형이 될 수 있다. - 
bool_variable = tf.Variable([False, False, False, True]) #바로 변수로만들기(텐서랑 아직까진 다른게없음..)
complex_variable = tf.Variable([5 + 4j, 6 + 1j])
print(bool_variable)
print(complex_variable)


print("Shape: ", my_variable.shape)
print("DType: ", my_variable.dtype)
print("As NumPy: ", my_variable.numpy)



#변수를 재구성할순없다. 하지만, 대부분의 텐서연산은 변수에 대해 작동함.
print("A variable: ",my_variable)
print("\nViewed as a tensor: ",tf.convert_to_tensor(my_variable)) #텐서로 바뀜.(?)
print("\nIndex of highest value: ", tf.argmax(my_variable)) #4.

#다른점: 텐서와는달리 변수는 변형되지 않는다. 아래는 변수에 텐서모양바꾸기를썼는데, 이럴경우, 새로운 텐서가 생성됨.
print("\nCopying and reshaping: ", tf.reshape(my_variable, ([1, 4])))


#메모리 관련해서 더 효율적으로 쓰기위해 변수 텐서 나눈듯.. 또, 변수로 한번지정하고 reshape를 써서 기존 변수를 복사후 변형해서 새로운텐서만듬.
#tf.Variable.assign을 사용해서 텐서를 재 할당할 수 있다.
a = tf.Variable([2.0, 3.0])
#This will keep the same dtype, float32
a.assign([1, 2]) #변수에 새 값을 할당한다(첫번째변수)
print(a)

#Not allowed as it resizes the variable:
#try:
#    a.assign([1.0, 2.0, 3.0])
#except Exception as e:
#    print(f"{type(e).__name__}: {e}") #:: 에러. 호환되지 않음.


a = tf.Variable([2.0, 3.0])
#a의 value로 b를 만든다.
b = tf.Variable(a)

a.assign([5, 6]) #assign : 할당하다.

#a,b두개 같은값으로 만들었지만, a값이 달라져서 두개가 다른걸 볼 수 있다.
print(a.numpy())
print(b.numpy())


print(a.assign_add([2, 3]).numpy()) #[7. 9.] - 2,3을 더하면서 할당
print(a.assign_sub([7, 9]).numpy()) #[0. 0.] - 위의 것에서 7,9를 빼면서 할당



a = tf.Variable(my_tensor, name="Mark")

b = tf.Variable(my_tensor + 1, name="Mark") #my_tensor의 모든 요소에 1의 스칼라값을더한다.(스칼라값은 브로드캐스트됨.)

print(a,"\n" , b)
print(a == b) # 변수 이름은 같지만 내용물이 다 다름(+1씩 더한..) 그래서 모두 같지 않다 라고 나옴.



step_counter = tf.Variable(1, trainable=False) #variable의 인수: trainable:True이면 GradientTapes가 이 사용을 자동으로 감시한다. 기본값은 False.

print(step_counter)




#변수 및 텐서 배치하기.
with tf.device('CPU:0'): #with: 자원을 획득/사용/반납할떄 유용한 문법.
    #프로그래밍은 파일을 열고(자원의 획득) -> 안의 내용확인(자원 사용) -> 파일 닫기(반납) 방식인데, 효율적으로 하도록 해준다.
    #device CPU:0의 파일? 기기? 를 열어서 아래 구문을 실행시키라는것 같다.(그런 내용인듯.)

    # 텐서를 만든다.
    a = tf.Variable([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    c = tf.matmul(a, b)

print(c)



#한 기기에서 변수/텐서 위치저장하고, 계산은 다른 기기에서 할수있다. 이경우, 기기간에 데이터복사가필요해서 좀 지연이 걸림.
with tf.device('CPU:0'):
    a = tf.Variable([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = tf.Variable([[1.0, 2.0, 3.0]])

with tf.device('GPU:0'):
  # Element-wise multiply
  k = a * b

print(k) #GPU가 없는 기기에서 이코드를 실행해도 코드는 실행되고, *는 CPU에서 발생함. (tf.config.set_soft_device_placement는 기본적으로 켜져있기 때문이라는데.. 나중에 다시 알아보기.)




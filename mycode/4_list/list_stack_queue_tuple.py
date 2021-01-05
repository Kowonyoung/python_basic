'''
Stack과 Queue를 list로 작성한다
'''


stack_list = [1,2,3,]
stack_list.append(5)
stack_list.extend([10,20])
print(stack_list)

#LIFO
stack_list.pop()
print(stack_list)
stack_list.pop()
print(stack_list)

#FIFO
queue_list = [10, 20, 30]
queue_list.pop(0)
print(queue_list)

#tuple
my_tuple = tuple([10, 30, 40])
my_tuple2 = (20, 30, 40)
print(type(my_tuple), type(my_tuple2))
print(my_tuple[2], my_tuple2[0:2], my_tuple * 2)

#type error : 튜플에서는 값 변경이 되지 않는다
my_tuple[1] = 50

my_int = (10)
my_tuple = (10,)
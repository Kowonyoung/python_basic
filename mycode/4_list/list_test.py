'''
list 타입을 선언하고 list에 엘리먼트 추가, 삭제
'''
'''
num_list = [10, 20, 30, 40, 50, 60]
print(type(num_list),num_list)
print(num_list[0], num_list[0:3], num_list[3:])

for idx, num in enumerate(num_list):
    print(idx, num)

str_list = ['python', 'java', 'kotlin', 'C++', 'Scalar']
str_list[1] = 'java script'
print(str_list[1], str_list[2:4])

str_list.append('Cobol')
'''
num_list = [60, 10, 30, 70, 80,]
num_list2 = [1, 2, 3, 4, 5]
#리스트의 메모리 저장 방식
print(num_list, num_list2)
num_list2 = num_list
print(num_list, num_list2)
num_list.sort()
print(num_list, num_list2)

a=list('python')
print (a)

my_list2 = 'hello, python'.split(',') # str -> list
print(my_list2)
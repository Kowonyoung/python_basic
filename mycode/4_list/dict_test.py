lang_dict = {}
lang_dict2 = dict()

'''
#dict에 값을 저장
lang_dict[100] = '자바'
lang_dict[200] = '파이썬'
lang_dict[300] = '텐서플로우'
lang_dict[400] = 'PyTorch'

#zip()함수
days = ['월요일', '화요일', '수요일']
fruits = ['사과', '바나나', '딸기']
coffees = ['아메리카노', '라떼', '모카', '믹스']
print(zip(days, fruits, coffees), type(zip(days, fruits, coffees)))
'''

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
for w in message:
    print(w, message.count(w))
    w_dict(w) = message.count(w)

print(w_dict)

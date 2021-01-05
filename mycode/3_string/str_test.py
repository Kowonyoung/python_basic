'''
문자열 관련 대응들
'''

#escape 문자
greet = 'hello' * 4 + '\n\r'
end = 'Good bye'
print(greet + end)

#bool type , str type
is_flag = False
my_str = 'False'
print(type(is_flag), type(my_str))

#문자열 indexing(offset)
greeting = 'hello world'
print(len(greeting))
print('문자열 길이 {}'.format(len(greeting)))

#3.6버전 이후에 생긴 것
print(f'문자열 길이 {len(greeting)}')

#문자열 인덱스 슬라이싱
print(f'greeting[0:5] = {greeting[0:5]}')
print(f'greeting[6:11] = {greeting[6:11]}')
print(f'greeting[:5] = {greeting[:5]}')
print(f'greeting[6:] = {greeting[6:]}')
print(greeting[:])
print(greeting[::2])

#음수값의 인덱스
print(f'greeting[-1:] = {greeting[-1:]}')
print(f'greeting[-2:] = {greeting[-2:]}')
# 문자열이 역순으로 바뀐다
print(f'greeting[::-1] = {greeting[::-1]}')

# 문자열 여러가지 함수들
word = 'Good manufacturing Practice Good'
print(word.upper())
result = word.upper()
print(word)
print(word, '  ', result)
print(f'소문자로 변환 = {word.lower()}')
print(word.find('G'))
print(word.rfind('G'))
print(word.count('g'))
word_list = word.split()
print(word_list)

word2 = 'Good/manufacturing/Practice/Good'
word2_list = word2.split('/')
print(word2_list)

word3 = ' hello python '
print(len(word3), len(word3.strip()), word3.strip())

for value in word:
    print(value, word.count(value))

for w in word_list:
    print(w)
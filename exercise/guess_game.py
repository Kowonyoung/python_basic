#Guess game

import random
guess_number = random.randint(1,101)
count = 1
number = int(input("숫자를 입력하세요 : "))
while True:
    if number > guess_number:
        print("숫자가 너무 큽니다.")
        number = int(input("숫자를 입력하세요 : "))
        count += 1
    elif number < guess_number:
        print("숫자가 너무 작습니다.")
        number = int(input("숫자를 입력하세요 : "))
        count += 1
    else:
        break;

print("정답은 ",guess_number)
print("몇번만에 맞추었나? ", count)
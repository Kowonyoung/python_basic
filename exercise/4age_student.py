'''
나이는 현재년도 - 태어난년도 +1
태어난년도 input()

from 모듈명 import
'''
from datetime import datetime as dt
#현재년도
current = dt.today().year
print("현재년도 :",current)

born = int(input("태어난 년도를 입력하세요 : "))
age = current - born + 1

if 17<=age<20:
    print("고등학생 입니다.")
elif 20<=age<27:
    print("대학생 입니다.")
else:
    print("학생이 아닙니다.")


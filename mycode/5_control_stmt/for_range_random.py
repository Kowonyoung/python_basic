print(range(10), range(1,11))
for val in range(1,10,2):
    print(val)

#dict 선언
wish_travel_cities = {
    '일본':'도쿄',
    '한국':'서울',
    '미국':'뉴욕',
    '한국':'부산'
}
print(wish_travel_cities['일본'])
print(wish_travel_cities.keys())
print(wish_travel_cities.values())
print(wish_travel_cities.items())

for key in wish_travel_cities.keys():
    print(f'{key} 의 {wish_travel_cities[key]}를 여행하고 싶어요')

import random
for val in range(10):
    random_value = random.randint(1, 100)
    print(random_value)

print(random.random())
print(random.choice([1, 2, 3, 4, 5]))
print(random.randint(1,100))
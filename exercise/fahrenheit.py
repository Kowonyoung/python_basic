def fah_convert(value):
    fehren = (9 * value) / 5 + 32
    return fehren


celcius = float(input("변환하고 싶은 섭씨온도를 입력해주세요 : "))
fehren = fah_convert(celcius)


print("섭씨온도 :",celcius)
print("화씨온도 :",round(fehren,2))

def my_average(numbers):
    print(numbers)
    total = 0
    for num in numbers:
        total += num
    avg = total / len(numbers)
    return int(avg)

def main():
    my_list = [20, 50, 60, 100, 30]
    result = my_average(my_list)
    print('평균값은 {}'.format(result))

main()

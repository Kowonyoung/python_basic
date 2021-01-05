while True:
    dan = int(input("몇단을 계산할까요? "))

    if dan != 0:
        print("구구단  %d단을 계산합니다.\n" % dan)
        for num in range(1,10):
            res = dan*num
            print("%d * %d = %d" %(dan,num,res))
    elif dan == 0:
        print("게임이 종료되었습니다.\n")
        break;

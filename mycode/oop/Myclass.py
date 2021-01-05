names = ['홍길동', '박지성', '손흥민', '둘리', '파이썬']
position = ['DF','MF','GK','DF','WF']
back_numbers = [5, 10, 20, 30, 15]

for na, po, ba in zip(names, position, back_numbers):
    print(na, po, ba)

players = [[name, position, back_numbers] for name, position, back_number in zip(names, position, back_numbers)]
print(players)
player1 = players[0]
player1[2] = 20
print(player1)

class SoccerPlayer
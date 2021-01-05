'''
yesterday 가사안에
YESTERDAY 몇번, Yesterday 몇번, yesterday 몇번인지
yesterday_lylic.upper().count('YESTERDAY')
'''

file = open("C:\mypython\python_programming_stu\exercise\yesterday.txt", 'r')
lines = file.read()
#for line in lines:
#print(lines)
list_lines = lines.split()
print(list_lines)

count_upper = 0
for upper in list_lines:
    if 'YESTERDAY' in list_lines:
        count_upper+=1
    else:
        count_upper+=0
print("YESTERDAY포함횟수 : ",count_upper)

count_normal = 0
for normal in list_lines:
    if 'Yesterday' in normal:
        count_normal+=1
    else:
        count_normal+=0
print("Yesterday포함횟수 : ",count_normal)

count_lower = 0
for lower in list_lines:

    if 'yesterday' in lower:
        count_lower+=1
    else:
        count_lower+=0
print("yesterday포함횟수 : ",count_lower)

file.close()
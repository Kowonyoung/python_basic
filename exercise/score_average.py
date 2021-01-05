kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]

midterm_score = [kor_score, math_score, eng_score]
#print(midterm_score)
#print(midterm_score[0])
#print(midterm_score[0][3])

student_score = [0, 0, 0, 0, 0]
idx = 0
for sub in midterm_score:
    #print(sub)
    for score in sub:
       #학생별로 과목 점수를 저장
       #print(student)
        student_score[idx] += score
        idx += 1
    print(student_score)
    #과목이 바뀔때 학생 인덱스를 초기화
    idx = 0
else:
    print(f'학생별합계점수 = {student_score}')
    #평균을 계산(unpacking 사용)
    a,b,c,d,e = student_score
    student_average  = [int(a/3), int(b/3), int(c/3), int(d/3), int(e/3)]
    print(f'학생별 평균점수 = {student_average}')
    pass
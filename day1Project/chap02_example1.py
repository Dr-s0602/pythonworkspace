student_name  = input("학생 이름 : ")
student_no = int(input("학번 : "))
kor = int(input('국어 성적 : '))
eng = int(input('영어 성적 : '))
mat = int(input('수학 성적 : '))

tot = kor + eng + mat
avg = tot/3

print('{}번 {}의 과목총점은 {}점이고 평균은 {}점'.format(student_no,student_name,tot,avg))
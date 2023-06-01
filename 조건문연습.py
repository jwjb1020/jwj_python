kor=int(input("국어점수"))
eng=int(input("영어점수"))
math=int(input("수학점수"))
evg=((kor*0.4)+(eng*0.4)+(math*0.2))
if evg >= 90:
    grade ="A"
elif evg >=80:
    grade ="B"
elif evg>=70:
    grade = "C"
elif evg>=60:
    grade = "D"
else:
    grade = "F"

print("성적결과")
print(f"국어: {kor:.2f}점, 영어: {eng:.2f}점, 수학:{math:.2f}점")
print(f"총 평균 점수:{evg:.2f}점")
print(f"학점: {grade}")
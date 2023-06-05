#학생들의 성적을 딕셔너리로 저장하고, 성적 평균을 계산하는 프로그램을 작성해보세요.
grade = {
    "Alice": [85, 90, 95],
    "Bob": [75, 80, 85],
    "Charlie": [95, 95, 95]
}
print("평균점수")
for name, grade_list in grade.items():
    avg = sum(grade_list)/len(grade_list)
    print(f"{name} : {avg}")
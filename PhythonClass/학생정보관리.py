'''문제: 학생 정보를 관리하는 프로그램을 만드세요.
– 학생(Student) 클래스
• 인스턴스 변수: 이름(name), 학번(student_id), 학년(year), 전공(major), 평균 성적
(avg_score)
• 메서드: get_info() - 학생의 정보를 문자열로 반환
– 학생들을 관리하는 클래스(StudentManager)
• 인스턴스 변수: 학생들(student_list)
• 메서드:
– add_student(student): 학생을 리스트에 추가하는 메서드
– remove_student(student_id): 학번을 이용해 학생을 리스트에서 제거하는 메서드
– find_student(student_id): 학번을 이용해 학생을 찾는 메서드
– show_all_students(): 모든 학생의 정보를 출력하는 메서드
• 위 클래스들을 이용하여 다음과 같은 프로그램을 작성하세요.
– 학생 관리자(StudentManager)를 생성합니다.
– 학생(Student)을 생성합니다. 학생의 인스턴스 변수는 이름, 학번, 학년, 전공, 
평균 성적을 포함합니다.
– 학생 관리자에 학생을 추가합니다.
– 학생 관리자에서 학생을 삭제합니다.
– 학생 관리자에서 학생을 찾습니다.
– 학생 관리자에서 모든 학생의 정보를 출력합니다.'''

class Student:
    def __init__(self, name, student_id, year, major, avg_score):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.avg_score = avg_score
    def get_info(self):
        return self.name,self.student_id, self.year, self.major, self.avg_score 
    
class StudentManager:
    def __init__(self):
        self.student_list = []
        
    def add_student(self,student):
        self.student_list.append(student)
      
    def remove_student(self,student_id):
        for list in self.student_list:
            if list.student_id == student_id:
                self.student_list.remove(list)
              
                  
    def find_student(self,student_id):
        for s in self.student_list:
            if s.student_id == student_id:
                return print(s.get_info())
        return print("찾는 학번이 없습니다.")               
    def show_all_students(self):
        for stu in self.student_list:
            print(stu.get_info())                   

mg = StudentManager()
student1 = Student("john","20231020",2,"science",4.0)
student2 = Student("jessy","20223420",4,"science",3.0)
student3 = Student("minsu","20207820",1,"science",2.0)

mg.add_student(student1)
mg.add_student(student2)
mg.add_student(student3)
mg.show_all_students()
studentNum = input("학번을 입력해주세요")
mg.find_student(studentNum)
studentdel = input("삭제할 학번")
mg.remove_student(studentdel)
mg.show_all_students()
print("1 : 추가, 2: 검색, 3: 삭제, 4: 보기, 5: 종료")
while True:
    n = int(input("숫자 입력"))
    if n == 1:
        pass
    elif n ==2:
        pass
    elif n ==3:
        pass
    elif n ==4:
        pass
    elif n == 5:
        exit()    
    

class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []
    def RunningAverage(self):
        total = sum(int(grade) for grade in self.Grades if grade)
        count = sum(1 for grade in self.Grades if grade)
        return total/count if count else 0
    
    def TotalAverage(self):
        total = sum(int(grade) if grade else 0 for grade in self.Grades)
        return total/len(self.Grades)
    
    def LetterGrade(self):
        total_avg = self.TotalAverage()
        if total_avg >= 90:
            return "A"
        elif 80 <= total_avg < 90:
            return "B"
        elif 70 <= total_avg < 80:
            return "C"
        elif 60 <= total_avg < 60:
            return "D"
        else:
            return "F"

class StudentList:
    def __init__(self):
        self.StudentList = []

    def add_student(self, firstname, lastname, tnumber):
        student = Student(firstname, lastname, tnumber)
        self.StudentList.append(student)

    def find_student(self, tnumber):
        for index, student in enumerate(self.StudentList):
            if student.TNumber == tnumber:
                return index
            return-1

    def print_student_list(self):
        print(f"{'First Name':<12} {'Last Name':<12} {'ID':<12} {'Running Average':<15} {'Semester Average':<15} {'Letter Grade':<12}")
        print('-' * 80)
        for student in self.StudentList:
            print(f"{student.FirstName:<12} {student.LastName:<12} {student.TNumber:<12} {student.RunningAverage():<15.2f} {student.TotalAverage():<15.2f} {student.LetterGrade():<12}")

    def add_student_from_file(self, filename):
            with open(filename, "r") as file:
                for line in file:
                    firstname, lastname, tnumber = line.strip().split(",")
                    self.add_student(firstname, lastname, tnumber)

    def add_scores_from_file(self, filename):
            with open(filename, "r") as file:
                for line in file:
                    tnumber, *grades = line.strip().split(",")
                    index = self.find_student(tnumber)
                    if index != -1:
                        self.StudentList[index].Grades.extend(grades)

if __name__ == "__main__":
    student_list = StudentList()
    student_list.add_student_from_file("11.Project Students.txt")
    student_list.add_scores_from_file("11.Project Scores.txt")
    student_list.print_student_list()
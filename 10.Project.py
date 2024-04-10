class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname.strip()
        self.LastName = lastname.strip()
        self.TNumber = tnumber.strip()
        self.Grades = [int(score) if score else 0 for score in scores]
    def RunningAverage(self):
        non_blank_scores = [score for score in self.Grades if score != 0]
        if non_blank_scores:
            return sum(non_blank_scores) / len(non_blank_scores)
        else:
            return 0
    def TotalAverage(self):
        return sum(self.Grades) / len(self.Grades)
    def LetterGrade(self):
        average = self.TotalAverage()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
#reading scores from file
with open("10.Project Student Scores.txt", "r") as file:
    lines = file.readlines()
students = []
for line in lines:
    data = line.strip().split(',')
    student = Student(data[0], data[1], data[2], data[3:])
    students.append(student)
#output results
for student in students:
    print(f"Student: {student.FirstName} {student.LastName} (TNumber: {student.TNumber})")
    print(f"Running Average: {student.RunningAverage()}")
    print(f"Total Average: {student.TotalAverage()}")
    print(f"Letter Grade: {student.LetterGrade()}")
    print()

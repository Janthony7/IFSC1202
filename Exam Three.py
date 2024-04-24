import math

#create triangle class
class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = float(s1)
        self.s2 = float(s2)
        self.s3 = float(s3)

    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3:
            return "Isosceles"
        else:
            return "Scalene"
        
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s *(s - self.s1) * (s - self.s2) * (s - self.s3))
    
    def angles(self):
        angles = []
        angles.append(math.degrees(math.acos((self.s2**2 + self.s3**2 - self.s1**2) / (2 * self.s2 * self.s3))))
        angles.append(math.degrees(math.acos((self.s1**2 + self.s3**2 - self.s2**2) / (2 * self.s1 * self.s3))))
        angles.append(180 - angles[0] - angles[1])
        return angles
    
#read data from file
TriangleList = []
with open("Exam Three Triangles.txt", "r") as file:
    for line in file:
        sides = line.strip().split(",")
        TriangleList.append(Triangle(*sides))

#print triangles
print("{:<15s}{:<12s}{:<12s}{:<12s}{:<12s}{:<12s}{:<12s}{:<12s}{:<12s}".format("Type", "Side 1", "Side 2", "Side 3", "Perimeter", "Area", "Angle 1", "Angle 2", "Angle 3"))
for triangle in TriangleList:
    print("{:<15s}{:<12.3f}{:<12.3f}{:<12.3f}{:<12.3f}{:<12.3f}{:<12.3f}{:<12.3f}{:<12.3f}".format(triangle.type(), triangle.s1, triangle.s2, triangle.s3, triangle.perimeter(),triangle.area(), * triangle.angles()))


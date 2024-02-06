#Using Hebrons formula (See TrigReview),
#write a program that prompts for the length of the 
#sides of a triangle and calculates the area.
#Note: Be sure to use floating point numbers in your calculations.
def FindAreaofTriangle(a, b, c):
    if a>=0 and b>=0 and c>=0:
        s = (a+b+c)/2
        a = (s*(s-a)*(s-b)*(s-c))**0.5
        return a

def main():
    a = float(input("Enter value for side a: "))
    b = float(input("Enter value for side b: "))
    c = float(input("Enter value for side c: "))
    area = FindAreaofTriangle(a, b, c)
    print("Area: ",area)

main()

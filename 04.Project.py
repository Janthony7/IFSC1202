#Create a program that displays a list or prime number in a specified range.
#A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
#Hint: For a given value N, Loop from 2 to (half of N) + 1
#and check to see if any number evenly divides into N.
start = int(input("start: "))
end = int(input("end: "))

for number in range(start, end + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)


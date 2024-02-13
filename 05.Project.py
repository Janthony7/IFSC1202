#Create a program that displays special numbers in a range.
#A special number is defined to be number that is the sum of its
#   own digits each raised to the power of the number of digits.
#153 is 3 digits long and is equal to 1^3 + 5^3 + 3^3
#8208 is 4 digits long and is equal to 8^4 + 2^4 + 0^4 + 8^4
#Hint: First determine the number of digits using a while loop and reminder division by 10.
#   Do not use any string functions or the LEN function.
#Hint: Recalculate the value using the power from above and see if you get the original value
#Do not use the len function to determine the number of digits.
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))
flag = 0
for n in range(start, end + 1):
    order = 0
    num = n
    while (num != 0):
        order = order + 1
        num = num // 10
    sum = 0
    temp = n
    while temp > 0:
        x = temp % 10
        sum += x ** order
        temp //= 10
    if n == sum:
        flag=1
        print(n)



        
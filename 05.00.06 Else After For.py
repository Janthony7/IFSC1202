for i in range(5):
    a = int(input("Enter a Number:"))
    if a < 0:
        print('Met a negative number', a)
        break
else:
    print('No negative numbers met')
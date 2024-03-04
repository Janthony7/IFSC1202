# Example 1
print()
print("Example 1")
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(Rainbow[0])
Rainbow[0] = 'red'
print('Print the rainbow')
for i in range(len(Rainbow)):
    print(Rainbow[i])
    
# Example 2
print()
print("Example 2")
a = [] # start an empty list
# read number of element in the list
n = int(input("Enter Number of Elements in List:"))  
for i in range(n):
	new_element = int(input("Enter a Number:"))  # read next element
	a.append(new_element) # add it to the list    
for i in range(len(a)):
    print("Element {} = {}".format(i, a[i]))

# Example 3
print()
print("Example 3")
a = [1, 2, 3]
b = [4, 5]
c = a + b
d = b * 3
print(c)
print(d)
print([7, 8] + [9])
print([0, 1] * 3)

# Example 4
a = [1, 2, 3, 4, 5]
# Print all the values on a single line
for i in range(len(a)):
    print(a[i], " ", end="")
print()
# Print all the values one per line
for i in range(len(a)):
    print(a[i])

# Example 5
print()
print("Example 5")
a = "1 2 3"
b = a.split()
for i in range(len(b)):
	b[i] = int(b[i])
for i in range(len(b)):
	print(b[i])

# Example 6
print()
print("Example 6")
a = '192.168.0.1'.split('.')
for i in range(len(a)):
    print(a[i])

# Example 7
print()
print("Example 7")
a = ['red', 'green', 'blue']
print(' '.join(a))    # prints red green blue
print('***'.join(a))  # prints red***green***blue
print('***'.join(a))  # prints red***green***blue
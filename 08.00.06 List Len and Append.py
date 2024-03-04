# Create an empty list
a = []
# Open a file for reading
numbersfile = open("numbers.txt", "r")
# Read the first line of the file
x = numbersfile.readline()
# End of file is indicated when the input is empty
while x != "":
# Convert the number to an integer and append it to the list
	a.append(int(x))
# Read the next line of the file
	x = numbersfile.readline()
# Close the file
numbersfile.close()
# Print the list - get the number of elements using the len() method
for i in range(len(a)):
	print(a[i])
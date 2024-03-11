# Create the array
a = []
# Open the file and read the first line`
numbersfile = open("09.00.02 NumbersList.txt")
x = numbersfile.readline()
# While not at end of file
while x != "":
# Split the line into a list
	y = x.split(" ")
# Convert the values from string to an integer
	for i in range(len(y)):
		y[i] = int(y[i])
# Append the list to the two dimensional array
	a.append(y)
# Read the next line
	x = numbersfile.readline()
# Loop through each row in the two dimensional array
for i in range(len(a)):
# Loop though each element in the list
    for j in range(len(a[i])):
# Print each element in the list
        print(a[i][j], end=' ')
# End of list - go to next line
    print()
a = [2, 3, 5, 8, 13, 5, 5]
# Check to see that 8 is in the list
if 8 in a:
	print("8 is in the list")
# Check to see if 15 is not in the list
if 15 not in a:
	print("15 is not in the list")
# Print the maximum of the list
print(max(a))
# Print the minumum of the list
print(min(a))
# Print the index of the element that has a value of 13
print (a.index(13))
# Print the number of occurrance of the value 5
print (a.count(5))
InputFileName = "06.Project Input File.txt"
MergeFileName = "06.Project Merge File.txt"
OutputFileName = "06.Project Output File.txt"
inputrecordcount = 0
mergerecordcount = 0
outputrecordcount = 0
inputfile = open(InputFileName, "r")
mergefile = open(MergeFileName, "r")
outputfile = open(OutputFileName, "w")
lines1 = inputfile.readline("Hello!", "Welcome to 06.Project Input File.txt")
lines2 = mergefile.readline("This is line 1 of the merge file", "This is line 2 of the merge file")
lines3 = inputfile.readline("This file is for testing purposes.", "Good luck!")
while lines1 != '':
    outputfile.write(lines1, lines2, lines3)
    inputrecordcount += 1
    mergerecordcount += 1
    outputrecordcount += 1
inputfile.close()
mergefile.close()
outputfile.close()
print("{} input records written" .format(inputrecordcount))
print("{} merge records written" .format(mergerecordcount))
print("{} input records written" .format(inputrecordcount))


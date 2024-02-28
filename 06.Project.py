inputfilename = '06.Project Input File.txt'
mergefilename = '06.Project Merge File.txt'
outputfilename = '06.Project Output File.txt'
def recordcount(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)
def mergedfiles(inputfile, mergefile, outputfile):
    inputrecordcount = 0
    mergerecordcount = 0
    outputrecordcount = 0
    with open(outputfile, 'w') as output, \
         open(inputfile, 'r') as input, \
         open(mergefile, 'r') as merge:
        for line in input:
            output.write(line)
            inputrecordcount += 1
            outputrecordcount += 1
            if '**Insert Merge File Here**' in line:
                for mergedline in merge:
                    output.write(mergedline)
                    mergerecordcount += 1
                    outputrecordcount += 1
                merge.seek(0)
        for line in input:
            output.write(line)
            inputrecordcount += 1
            outputrecordcount += 1
    return inputrecordcount, mergerecordcount, outputrecordcount
inputrecordcount, mergerecordcount, outputrecordcount = mergedfiles(inputfilename, mergefilename, outputfilename)
print("inputrecordcount Input file Records")
print("mergerecordcount Merge File Records")
print("outputrecordcount Output File Records")
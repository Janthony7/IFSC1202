def ParseDegreeString(ddmmss):

    #find degree symbol
    degree_symbol_index = ddmmss.find("°")
    degrees = float(ddmmss[:degree_symbol_index])

    #find minutes symbol
    minute_symbol_index = ddmmss.find("'")
    minutes = float(ddmmss[degree_symbol_index + 1:minute_symbol_index])
   
    #find seconds symbol
    second_symbol_index = ddmmss.find('"')
    seconds = float(ddmmss[minute_symbol_index + 1:second_symbol_index])
    
    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    #convert dd, mm, ss to decimal degrees
    decimal_degrees = degrees + minutes / 60 + seconds / 3600
    return decimal_degrees

def main():
    #read angles from file
    with open("07.Project Angles Input.txt", "r") as inputfile:
        lines = inputfile.readlines()

    #counter for number of records processed
    num_records_processed = 0

    #open new file to write decimal degrees
    with open("07.Project Angles Output.txt", "w") as outputfile:
        for line in lines:
            line = line.strip()
            degrees, minutes, seconds = ParseDegreeString(line)
            decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
            outputfile.write(f"{decimal_degrees}\n")
            num_records_processed += 1

    print(f"{num_records_processed} Records Processed")

if __name__== "__main__":
    main()                                    
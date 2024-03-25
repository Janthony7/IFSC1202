import csv
#function to read csv file and load into 2d list
def ReadDistTable(FilePath):
    DistTable = []
    with open(FilePath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            DistTable.append(row)
    return DistTable
#function to print 2d list
def PrintDistTable(table):
    for row in table:
        print(row)
#function to find index of city in table
def FindCityIndex(city, CityList):
    try:
        index = CityList.index(city)
        return index
    except ValueError:
        return None
#main function
def main():
    #read distance table from csv file
    DistTable = ReadDistTable("09.Project Distances.csv")
    #print distance table
    print("Distance Table: ")
    PrintDistTable(DistTable)
    #prompt for FROM city
    FromCity = input("Enter the From City: ").strip()
    #prompt for TO city
    ToCity = input("Enter the To City: ").strip()
    #find index of FROM city in zeroth column
    FromCityIndex = FindCityIndex(FromCity, DistTable[0])
    #find index of TO city in zeroth row
    ToCityIndex = FindCityIndex(ToCity, DistTable[0])
    #check if both cities were found
    if FromCityIndex is None:
        print("Invalid From City")
    elif ToCityIndex is None:
        print("Invalid To City")
    #display FROM city, TO city, and distance
    else:
        print(f"From City: {FromCity}")
        print(f"To City: {ToCity}")
        print(f"Distance: {DistTable[FromCityIndex][ToCityIndex]}")
if __name__ == "__main__":
    main()
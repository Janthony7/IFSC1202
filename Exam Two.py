with open("Exam Two Properties.csv", "r") as file:
    lines = file.readlines()
properties = []

for line in lines:
    data = line.strip().split(",")
    data[4] = float(data[4])
    properties.append(data)
zipcodes = []

for property in properties:
    zip_code = property[3]
    price = property[4]
    found = False
    for zipcode in zipcodes:
        if zipcode[0] == zip_code:
            zipcode[1] += 1
            zipcode[2] += price
            found = True
            break
    if not found:
        zipcodes.append([zip_code, 1, price])
    
print("Zipcode\tCount\tAverage")

for zipcode in zipcodes:
    count = zipcode[1]
    total_price = zipcode[2]
    average_price = total_price / count
    print(f"{zipcode[0]}\t{count}\t${average_price:.2f}")

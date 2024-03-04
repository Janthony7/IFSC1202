import requests
# Read a file from the Internet using GET
response = requests.get('https://example-files.online-convert.com/document/txt/example.txt')
# Get the text string of the response
filestring = response.text
# Split the string by newline character into a list
filestringlist = filestring.split("\n")
# Print the list
for i in range(len(filestringlist)):
    print(filestringlist[i])
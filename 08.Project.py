import requests
#read US constitution from internet
def read_us_constitution():
    url = "http://www.usconstitution.net/const.txt"
    response = requests.get(url)
    return response.text.split('\n')

#find sections based on search term
def find_sections(search_term, lines):
    for i, line in enumerate(lines):
        if search_term.lower() in line.lower():
            #loop backward to find beginning of section
            start_index = i
            while start_index > 0 and lines[start_index - 1].strip() != "":
                start_index -= 1

            #loop forward to find end of section
            end_index = i
            while end_index < len(lines) - 1 and lines[end_index + 1].strip() != "":
                end_index += 1

            #print section
            print(f"\nSection containing '{search_term}' (Lines {start_index + 1}-{end_index + 1})")
            for j in range(start_index, end_index + 1):
                print(f"Line {j + 1}: {lines[j].strip()}")
            print()

            #skip to end of section
            i = end_index
#main function
def main():
    #read us constitution
    lines = read_us_constitution()

    #prompt search term
    while True:
        search_term = input("Enter search term (blank to exit): ").strip()
        if not search_term:
            break
        #find sections
        find_sections(search_term, lines)
                
    #prompt search term
    while True:
        search_term = input("Enter search term (blank to exit): ").strip()
        if not search_term:
            break
        #find sections
        find_sections(search_term, lines)

if __name__ == " __main__":
    main()

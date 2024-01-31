#Write a program that prompts for a length of time in days.
#Note: Assume there are 365 days is a year.
#Calculate and print:
#Number of years specified in the length of time
#Number of weeks specified in the length of time
#Number of days specified in the length of time

#Prompt for time in days:
days = int(input("Enter length of time in days: "))
#Calculate years:
years = days // 365
days %= 365
#Calculate weeks:
weeks = days // 7
days %= 7
#Remaining days:
print("Years: ", years)
print("Weeks: ", weeks)
print("Days : ", days)



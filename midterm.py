# Q1
a = 10
a = a + 2
print(a*2)
a = 19
print(a+3)
a = a // 2
print(a)

#Q2
print((2+3)*6/2 and 18.0)

#Q3
import datetime
a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

#Q4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("4257304920394478392772938744930294037524"))
print(palindrome("0974101607733149676776769413377061014790"))
print(palindrome("7798338247658278460338648728567428338977"))
print(palindrome("2704702208931031198668911301398022074072"))

#Q5
def count_patterns(text):
    """
    Finds and counts words that start with "b", have unlimited letters, and end with "Bob"
    :param text: string to search in
    :return:integer that signifies number of matches
    """
    words = text.split() #splitting the text into words
    count = 0 #counter for matches

    for word in words:
        if word.startswith("b") and word.endswith("Bob") and len(word)>3: #writing out all the criterias
            count += 1 # this will increase the count if a match is found
    print(count)

text1 = "bSuperBob is a hero but bminiBob and bHelloBob are just names. bBob does not count."
count_patterns(text1)

#Q6
list = [1,2,3,4,5,6,7,8]
list.append(9)
print(list)
string = "abcdefg"
print(string[1:5])
print(string.capitalize())
print(string)

#Q7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

processed_numbers = [] #this is starting a new list
for num in random_numbers:
    if num % 2 == 0: #this is checking whether numbers are even
        # this if loop also removes the odd numbers, as they're not being included
        processed_numbers.append(num*2) #this is multiplying the leftover evens by 2, to get their double value

print(random_numbers)
print(processed_numbers)

#Q8
#valid URLS start with http:// or https://
def valid_url(url):
    """
    Function that returns whether a URL is valid or not
    :param url: string to be checked
    :return: True if valid, False if not valid
    """
    try:
        if url.startswith("http://") or url.startswith("https://"):
            print("True")
        else:
            print("False")
    except TypeError:
        print("Please input a valid string")

valid_url("https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL")

#Q9
def birthday_days_passed(birthday):
    """
    calculates how many days has passed since birthday
    :param birthday: string in the format "DD-MM-YYYY"
    :return:integer representing number of days
    """
    try:
        birth_year = int(birthday[-4:]) # reading string from the end
        current_year = int(input("Enter current year: "))

        if current_year <= birth_year:
            print("Please enter a valid year. Current year must be bigger than current year.")
            return
        years_passed = current_year - birth_year - 1 # whole years since bday
        leap_years = 0
        for year in range(birth_year+1, current_year):
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                leap_years +=1
        total_days = (years_passed*365) + (leap_years*366)
        print(total_days)
    except ValueError:
        print("Invalid input. Please enter the date in DD-MM-YYYY format.")

birthday_days_passed("05-04-2005")





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

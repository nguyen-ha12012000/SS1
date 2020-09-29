def date():
    user_date = input("Enter a date in mm/dd/yyyy format: ")
    month_str, day_str, year_str = user_date.split('/')
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    month = int(month_str)

    print(MONTHS[month-1] +',' + day_str + ',' + year_str)

date()
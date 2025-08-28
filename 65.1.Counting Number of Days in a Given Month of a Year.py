import calendar
def days_in_month(year, month):
    if month < 1 or month > 12:
        return "Invalid month. Please enter a month between 1 and 12."
    return calendar.monthrange(year, month)[1]
year = 2023
month = 2
print("Number of days in month {} of year {}: {}".format(month, year, days_in_month(year, month))) 
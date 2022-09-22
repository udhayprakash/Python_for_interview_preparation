from datetime import date, datetime


def age_calculator(date_str, date_format):
    born = datetime.strptime(date_str, date_format)
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


print(age_calculator("1988-04-08", "%Y-%m-%d"))
print(age_calculator("1988-08-08", "%Y-%m-%d"))
print(age_calculator("1988-09-08", "%Y-%m-%d"))
print(age_calculator("1988-11-08", "%Y-%m-%d"))
print(age_calculator("1988-11-17", "%Y-%m-%d"))
print(age_calculator("1988-11-25", "%Y-%m-%d"))

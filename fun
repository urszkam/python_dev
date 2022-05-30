import datetime

birthdate = '1990-06-01'

today = datetime.datetime.now()
birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d")

age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

print(age)

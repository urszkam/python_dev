import datetime

birthdate = datetime(input('Ile?'))

print(birthdate)

today = datetime.datetime.now()
birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d")

age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

print(age)

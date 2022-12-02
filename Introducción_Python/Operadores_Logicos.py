#and
age=40
is_adult = age > 16 and age < 60

user, password = 'admin', '123'
is_login = user == 'admin' and password == '123'

print(is_adult)
print(is_login)

#not
is_not_adult = not(is_adult)
is_not_allowed = not(is_login)

print(is_not_adult)
print(is_not_allowed)

#or
name='Mary'
is_student = name == 'Paul' or name == 'Mark'
print(is_student)


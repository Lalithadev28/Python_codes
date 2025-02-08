'''Write Custom Exception  if entered age is negative , rais the error saying that
age can not be negative'''

class InvalidAge(Exception):
      pass
def person_age(x):
    if x <= 0 :
        raise InvalidAge("age can not be negative ")
try:
    person_age(0)
except InvalidAge  as e:
    print(e)
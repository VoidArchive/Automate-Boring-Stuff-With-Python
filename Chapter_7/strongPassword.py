import re

PASSWORD_CHECKS = [
    re.compile(r'[A-Z]'),
    re.compile(r'.{8,}'),
    re.compile(r'[0-9]'),
]


def strong_password(password):
    """
    Password is considered strong if:
      - is eight characters or longer
      - contains uppercase and lowercase characters
      - has one digit or more

    """
    return all(check.search(password) for check in PASSWORD_CHECKS)


keepgoing = True

while keepgoing:
    passwordInput = input('Enter a strong password: ')
    checked = strong_password(passwordInput)
    if checked == True:
        print("This is a strong password")
        keepgoing = False
    else:
        print("Weak Weak Enter again")

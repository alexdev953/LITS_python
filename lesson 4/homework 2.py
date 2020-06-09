email = input('Enter e-mail: ').lower()
email_check = input('Enter e-mail for check: ').lower()
if email.find('@') != -1:
    if email == email_check:
        print('OK')
    else:
        print('email not match')
else:
    print('Bad email')

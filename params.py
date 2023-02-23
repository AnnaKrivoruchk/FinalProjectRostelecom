LOGIN_URL = "https://b2c.passport.rt.ru/"

def generate_invalid_string(num):
    return "A" * num

def invalid_mail(email):
    return email[:-3]

def invalid_login(login):
    return login[:-3]

def invalid_phone(phone):
    return phone[:-3] + '111'
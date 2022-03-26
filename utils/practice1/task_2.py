
login = str(input("login: "))
mail = str(input("email: "))

is_login_correct = True
is_mail_correct = True

if mail.find("@") == -1:
    is_mail_correct = False

if login.find("@") != -1:
    is_login_correct = False

print(is_login_correct, is_mail_correct)

# TODO
# is(is_login_correct and is_mail_correct):

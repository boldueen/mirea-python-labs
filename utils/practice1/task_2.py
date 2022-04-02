login = str(input("login: "))
mail = str(input("email: "))

is_login_correct = True
is_mail_correct = True

if mail.find("@") == -1:
    is_mail_correct = False

if login.find("@") != -1:
    is_login_correct = False


if (is_login_correct and is_mail_correct):
    print("OK")

else:
    if (not is_login_correct):
        print("Некорректный логин")

    if (not is_mail_correct):
        print("Некорректный адрес")

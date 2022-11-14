def is_email_in_list(email, email_list):
    for e in email_list:
        if email == e:
            print("Znaleziono")
            return True

    print("Nie znaleziono maila")
    return False

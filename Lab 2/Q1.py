password = input("Enter your password: ")

if len(password) >= 8:
    letter = False
    digit = False
    special = False

    for c in password:
        if c.isalpha():
            letter = True
        elif c.isdigit():
            digit = True
        elif c in "@$%&":
            special = True

    if letter== True and digit== True and special==True:
        print("Strong password")
    else:
        print("Password is not strong")
else:
    print("Password must be at least 8 characters.")

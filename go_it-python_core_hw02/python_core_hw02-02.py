is_active = bool(input("Is the user active? "))
is_admin = bool(input("Is the user administrator? "))
is_permission = bool(input("Does the user have access? "))

if is_admin:
    access = True
elif is_active and is_permission:
    access = True
else:
    access = False

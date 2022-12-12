def get_fullname(first_name, last_name, middle_name=""):
    if middle_name == "":
        return f"{first_name} {last_name}"
    else:
        return f"{first_name} {middle_name} {last_name}"

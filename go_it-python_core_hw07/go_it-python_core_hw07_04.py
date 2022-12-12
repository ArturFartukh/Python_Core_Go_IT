def is_integer(s):
    s = s.strip()
    if len(s) == 0:
        return False
    elif s[0].isdigit or s[0] in ('+', '-'):
        return s[1:].isdigit()

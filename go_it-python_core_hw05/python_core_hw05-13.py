import re


def find_all_emails(text):
    result = re.findall(
        r"[a-z][\w+.]+@\w+[.][a-z]{2,3}", text, flags=re.IGNORECASE)
    return result


print(find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net Simple email cool@api.io cool@api.i first.middle.last@iana.or a2@test.com a3@test.com.io 222111@test.com'))

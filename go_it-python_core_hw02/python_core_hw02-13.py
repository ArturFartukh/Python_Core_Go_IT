message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if not ch.isalpha():
        encoded_message += ch
    elif ch.isupper():
        ch = ord(ch) - ord("A")
        ch = (ch + offset) % 26
        encoded_message += chr(ch + ord("a")).upper()
    else:
        ch = ord(ch) - ord("a")
        ch = (ch + offset) % 26
        encoded_message += chr(ch + ord("a"))

import re


def replace_spam_words(text, spam_words):
    for item1 in spam_words:
        spam = re.findall(item1, text, flags=re.IGNORECASE)
        for item2 in spam:
            text = re.sub(item2, '*'*len(item2), text)
    return text
    

# print(replace_spam_words('Ты хорош, но выглядишь как лох. И вообще лошара!', ['лох', 'лошара']))

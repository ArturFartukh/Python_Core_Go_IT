def is_spam_words(text, spam_words, space_around=False):
    spam_words = [word.lower() for word in spam_words]
    if space_around:
        for word in text.lower().replace('.', '').split(' '):
            if word in spam_words:
                return True
    elif not space_around:
        for word in spam_words:
            if text.lower().find(word.lower()) > -1:
                return True
    return False


# print(is_spam_words('Ты хорош, но выглядишь как лох.', ['лох'], True))

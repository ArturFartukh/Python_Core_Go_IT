def real_len(text: str):

    text = text.replace('\n', "").replace(
        "\t", "").replace("\f", "").replace("\v", "").replace("\r", "")

    return len(text)

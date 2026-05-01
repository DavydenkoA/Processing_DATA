import chardet


def get_encoding(source):
    with open(source, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        confidence = result['confidence']

    print(f"Кодировка: {encoding}, уверенность: {confidence}")
    return encoding

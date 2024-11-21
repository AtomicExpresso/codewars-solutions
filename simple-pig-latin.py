def pig_it(text):
    words = text.split()
    return ' '.join([f'{w[1:]}{w[0]}ay' if w.isalpha() else w for w in words])

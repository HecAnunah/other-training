def  normalize_url(adress):
    normalize = adress
    if adress[:8] == 'https://':
        return normalize
    elif adress[:7] == 'http://':
        return 'https://' + adress[7:]
    else:
        return 'https://' + adress




print(normalize_url('google.com'))

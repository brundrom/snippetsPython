def normalize_url(link):
    if link[:8] == "https://":
        return link
    elif link[:7] == "http://":
        return link[:4] + 's://' + link[7:]
    else:
        return 'https://' + link


print(normalize_url('http://ya.ru'))

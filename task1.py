def domain_name(url):
    if url.count('://'):
        url = url[url.index('://')+3:]
    if url.count('/'):
        url = url[:url.index('/')]
    if url.count('www.'):
        url = url.replace('www.', '')
    if url.count('.'):
        url = url[:url.index('.')]

    return url


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"


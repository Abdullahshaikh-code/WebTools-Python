from urllib import request
l = open("crowl url.txt", "r")
for line in l.readlines():
 try:
    url = line
    con = request.urlopen(url, timeout=20)
    webpageb = con.read()
    webpage = webpageb.decode("utf8")
    print(line )
# ----Base URL----
    b1 = url.find('://')
    b2 = url.find('/', b1+3)
    if url.startswith("http:"):
        baseurl = url[b1-4:b2]
    if url.startswith("https:"):
        baseurl = url[b1-5:b2]
    print(baseurl)
    # ---- Related Url----
    z = -1
    anchor = 8
    while anchor >= 0:
        anchor = webpage.find("<a", z+1)
        p1 = webpage.find('"', anchor)
        p2 = webpage.find('"', p1+1)
        crawlurl = webpage[p1+1:p2-1]
        z = anchor
        if z < 0:
            break
        print(crawlurl)
        if crawlurl.startswith("http:") or crawlurl.startswith("https:"):
            f = open("weburl.txt", "a")
            f.write(crawlurl+"\n")
            f.close
        else:
            c_url = baseurl+"/"+crawlurl
            f = open("weburl.txt", "a")
            f.write(c_url+"\n")
            f.close
 except :
    print(f"connection error with :", url)
    pass     
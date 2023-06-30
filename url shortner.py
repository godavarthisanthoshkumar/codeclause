import pyshorteners
url=input("Please Enter url :")
def urlshortner(url):
 s=pyshorteners.Shortener()
 print(s.tinyurl.short(url))
urlshortner(url)
from bs4 import BeautifulSoup
import html5lib
import requests


res = requests.get("https://amarmp.com/mpsearch")

if res.status_code == 200:
  data = res.text

  encoding = res.encoding if 'charset' in res.headers.get('content-type', '').lower() else None

  parser = 'html.parser'  # or lxml or html5lib

  soup = BeautifulSoup(res.content, parser, from_encoding=encoding)

rdata = [item.encode("ascii","ignore") for item in soup.find_all(text=True)]

print(rdata)

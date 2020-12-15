import requests
import re
import random

import logging

from bs4 import BeautifulSoup



class BLBL:
  def __init__(self):
    # modified by sherk
    self.base_url = "https://www.bilibili.com/video/BV1PJ411Y7EG" # '?from=search&seid=16370838628940058696'
    self.cookie = "buvid3=914966CA-F8C4-45CD-9DCC-0B76C41F2890190961infoc; LIVE_BUVID=AUTO2215696355032554; rpdid=|(umk)YJuY~Y0J'ulYmYJllkm; im_notify_type_39940557=0; laboratory=1-1; CURRENT_QUALITY=116; finger=158939783; _uuid=1D09812C-B2A3-0468-F50C-EE7ACF3C6DD425628infoc; sid=htt4ie7h; CURRENT_FNVAL=80; blackside_state=1; PVID=1"
    self.referer = "https://www.bilibili.com/video/BV1PJ411Y7EG?from=search&seid=16370838628940058696"
    self.accept = "image/avif,image/webp,image/apng,image/*,*/*;q=0.8"
    self.accept_encoding = "gzip, deflate, br"
    self.accept_language = "en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7"
    self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"


  @property
  def html(self):
    base_headers = {
      'Accept'                      : self.accept,
      'Accept-Encoding'             : self.accept_encoding,
      'Accept-Language'             : self.accept_language,
      'Cache-Control'               : 'max-age=0',
      'Connection'                  : self.cookie,
      'Host'                        : 'www.bilibili.com',
      'Referer'                     : self.referer,
      'Upgrade-Insecure-Requests'   : '1',
      'User-Agent'                  : self.user_agent
    }

    # request the website
    base_response = requests.get(self.base_url, headers=base_headers)
    print(base_headers)

    # get html
    html = base_response.text

    return html

  def info(self, html):
    soup = BeautifulSoup(html)

    print(soup.prettify())


    try:
      video_name = re.search('<title>(.+)</title>', html, re.S).group(1) + '.flv'
    except:
      pass

  def video(self, html):
    # get video name, download url and host
    pass



if __name__ == "__main__":
  blbl = BLBL()

  from bs4 import BeautifulSoup

  soup = BeautifulSoup(blbl.html, 'lxml')

  # print(soup.title, soup.title.string)
  # print(soup('title'), soup('title')[0].string)
  # print(soup.meta.get('charset'), soup.meta['charset'])
  # print(soup.meta)
  # print(soup.find('meta'))
  # print(soup.find('meta', attrs={'name': 'viewport'}))
  # print(soup.find_all('meta', attrs={'charset': True}))

  # print(soup.prettify())

  with open('resp', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

  





 
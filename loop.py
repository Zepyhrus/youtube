import os
import time
import requests
import re
import random
import logging

from bs4 import BeautifulSoup
import youtube_dl

from configs import MAX_SIZE, YDL_OPTS





class BLBL:
  def __init__(self, base_url, base_referer):
    # modified by sherk
    self.base_url = base_url
    self.cookie = "buvid3=914966CA-F8C4-45CD-9DCC-0B76C41F2890190961infoc; LIVE_BUVID=AUTO2215696355032554; rpdid=|(umk)YJuY~Y0J'ulYmYJllkm; im_notify_type_39940557=0; CURRENT_QUALITY=116; _uuid=1D09812C-B2A3-0468-F50C-EE7ACF3C6DD425628infoc; sid=htt4ie7h; CURRENT_FNVAL=80; blackside_state=1; PVID=1; finger=158939783"
    self.referer = base_referer
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

    return base_response.text



if __name__ == "__main__":
  init_url = "https://www.bilibili.com"
  host = 'https://www.bilibili.com'
  loop = True


  blbl = BLBL(init_url, init_url)
  soup = BeautifulSoup(blbl.html, 'lxml')
  links = ['https:' + _.get('href') + '/' for _ in soup.find_all('a') if 'href' in _.attrs and '/video/BV' in _.get('href')]

  print(links)

  while loop:
    while len(links) >= MAX_SIZE:
      links.pop(0)  # empty

    _idx = random.choice(range(len(links)))

    try:
      new_url = links.pop(_idx)
      print(f'Ready to download: {new_url}')

      with youtube_dl.YoutubeDL(YDL_OPTS) as ydl:
        ydl.download([new_url])
      
      bvid = new_url.split('video/')[-1].replace('/', '')
      blbl = BLBL(new_url, new_url)
      soup = BeautifulSoup(blbl.html, 'lxml')
      with open(f'htmls\\{bvid}.html', 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

      for _a in soup.find_all('a'):
        if 'class' in _a.attrs and 'title' in _a.attrs['class']:
          _href = _a.get('href')
          _appex = _href.split('?')[0]

          if 'video' not in _appex: continue

          _url = host + _appex
          _referer = host + _href

          links.append(_url)
    except Exception as err:
      print(err)

    






  

  

  


  





 
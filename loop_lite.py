import os
import time
import requests
import re
import random
import logging

from bs4 import BeautifulSoup
import youtube_dl

from loop import BLBL
from configs import MAX_SIZE, YDL_OPTS


if __name__ == "__main__":
  # 救命
  init_url = "https://www.bilibili.com/video/BV1ka411A7HJ"
  init_refer = "https://www.bilibili.com/video/BV1ka411A7HJ"
  host = 'https://www.bilibili.com'
  loop = True


  blbl = BLBL(init_url, init_refer)
  links = []

  # loop here
  while loop:
    while len(links) >= MAX_SIZE:
      links.pop(0)
    
    soup = BeautifulSoup(blbl.html, 'lxml')

    for _a in soup.find_all('a'):
      if 'class' in _a.attrs and 'title' in _a.attrs['class']:
        _href = _a.get('href')
        _appex = _href.split('?')[0]

        if 'video' not in _appex: continue

        _url = host + _appex
        _referer = host + _href

        links.append((_url, _referer))

    # try:
    new_url, new_refer = random.choice(links)
    print(f'Ready to download: {new_url}')
    
    try:
      with youtube_dl.YoutubeDL(YDL_OPTS) as ydl:
        ydl.download([new_url])
    except Exception as err:
      print(err)

    blbl = BLBL(new_url, new_refer)
  

  


  





 
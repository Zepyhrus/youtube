import os
import time
import requests
import re
import random
import logging
import json

from bs4 import BeautifulSoup



class BLBL:
  def __init__(self, base_url, base_referer):
    # modified by sherk
    self.base_url = base_url # '?from=search&seid=16370838628940058696'
    self.cookie = "buvid3=914966CA-F8C4-45CD-9DCC-0B76C41F2890190961infoc; LIVE_BUVID=AUTO2215696355032554; rpdid=|(umk)YJuY~Y0J'ulYmYJllkm; im_notify_type_39940557=0; laboratory=1-1; CURRENT_QUALITY=116; finger=158939783; _uuid=1D09812C-B2A3-0468-F50C-EE7ACF3C6DD425628infoc; sid=htt4ie7h; CURRENT_FNVAL=80; blackside_state=1; PVID=1"
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

    # get html
    html = base_response.text

    return html

  def info(self, html):
    soup = BeautifulSoup(html)

  def video(self, html):
    # get video name, download url and host
    pass



if __name__ == "__main__":
  init_url = "https://www.bilibili.com/video/BV1PJ411Y7EG"
  init_refer = "https://www.bilibili.com/video/BV1PJ411Y7EG?from=search&seid=16370838628940058696"
  host = 'https://www.bilibili.com'
  loop = False


  blbl = BLBL(init_url, init_refer)

  soup = BeautifulSoup(blbl.html, 'lxml')

  scripts = soup.find_all('script')

  for script in scripts:
    if len(script.contents):
      _cont = script.contents[0]

      if '__playinfo__' in _cont:
        _playinfo_ = json.loads(_cont.replace('window.__playinfo__=', ''))
        _videoinfo_ = _playinfo_['data']['dash']
        
        
        for _v in _videoinfo_:
          pass
 
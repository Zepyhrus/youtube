"""
https://api.bilibili.com/x/web-interface/newlist?&rid=10&type=0&pn=20&ps=50&jsonp=jsonp
"""
import time, json
import os
from os.path import join, split, basename
import requests





def find_url(num):
  print('开始爬取页面数量')
  left = 0
  mid = 20    # original 80000
  right = 40  # original 160000, 这三个数据定义的目的是
  p = mid

  for k in range(20):
    time.sleep(0.2)
    dis = right - left
    _u = f'https://api.bilibili.com/x/web-interface/newlist?&rid={num}&type=0&pn={p}&ps=50&jsonp=jsonp'
    r = requests.get(_u)
    r.encoding = r.apparent_encoding
    data = json.loads(r.text)

    # print(left, mid, right)
    if len(data['data']['archives']):  # 判断第P页是否有数据
      right = right
      left = mid
      p = int((right + mid) / 2)
      mid = p  
    else:
      left = left
      right = mid
      p = int((left + mid) / 2)
      mid = p
    
    if len(data['data']['archives']) and dis < 2:  # 第P页有数据且“头尾”只差1，结束判断，得到页码
      print('aid:{},页数:{},数量:{}'.format(num, p, p * 50))
      break
  
  print('页面数量爬取结束')
  print('--开始生成URL池--')
  Url_Pool = []

  for m in range(0, p):
    url = "https://api.bilibili.com/x/web-interface/newlist?&rid={}&type=0&pn={}&ps=50&jsonp=jsonp".format(num, m)
    Url_Pool.append(url)
  print('--URL池生成结束--')


  return Url_Pool



if __name__ == "__main__":
  pool = find_url(10)

  print(pool)

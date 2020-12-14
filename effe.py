



if __name__ == "__main__":
  import urllib.request

  _u = "https://api.bilibili.com/x/web-interface/view?aid=2"

  response = urllib.request.urlopen(_u)
  print(response.info())
  print(response.read())
  response.close()



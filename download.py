import pafy


if __name__ == "__main__":
  url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
  
  video = pafy.new(url)

  bestaudio = video.getbest()

  bestaudio.download()




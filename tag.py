from bs4 import BeautifulSoup




if __name__ == "__main__":
  with open('resp.html', 'r') as f:
    soup = BeautifulSoup(f.read(), 'lxml')


import re
import requests
from bs4 import BeautifulSoup
from PIL import Image
from pprint import pprint


def download_image(url):
    image = Image.open(requests.get(url, stream=True).raw)
    remote_filename = url.split('/')[-1]
    filename, ext = remote_filename.split('.')
    saved_filename = '{}.{}'.format(filename, image.format.lower())

    print('download {}'.format(saved_filename))
    with open(saved_filename, 'wb') as f:
        _ = requests.get(url, stream=True)
        for block in _.iter_content(512):
            if not block: break
            f.write(block)

def main():
    url = 'https://www.ptt.cc/bbs/Beauty/M.1501931019.A.AD8.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.find_all('a', attrs={'href': True})

    for link in links:
        if re.search('i\.imgur\.com', link['href']):
            download_image(link['href'])

if __name__ == '__main__':
    main()
import re
import requests
from bs4 import BeautifulSoup
from PIL import Image

def download_image(url):
    response = requests.get(url, stream=True)
    image = Image.open(response.raw)
    remote_filename = url.split('/')[-1]
    filename, ext = remote_filename.split('.')
    saved_filename = '{}.{}'.format(filename, image.format.lower())

    print('download {}'.format(saved_filename))
    image.save(saved_filename)

def main():
    url = 'http://imgur.com/rqCqA.png'
    download_image(url)


if __name__ == '__main__':
    main()

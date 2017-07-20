import requests
from urllib.request import urlretrieve
from PIL import Image


def main():
    url = 'http://imgur.com/rqCqA.png'
    image = Image.open(requests.get(url, stream=True).raw)

    remote_filename = url.split('/')[-1]
    filename, ext = remote_filename.split('.')
    saved_filename = '{}.{}'.format(filename, image.format.lower())

    with open(saved_filename, 'wb') as f:
        _ = requests.get(url, stream=True)
        for block in _.iter_content(512):
            if not block: break
            f.write(block)


if __name__ == '__main__':
    main()
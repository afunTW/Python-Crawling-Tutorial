import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlretrieve

website = requests.get('http://research.sinica.edu.tw/book-sale-data/')
soup = BeautifulSoup(website.text, 'lxml')

image = soup.select('img')

print('get image tag {}'.format(image[0]))
print('get image src {}'.format(image[0]['src']))


root = website.url
print('\n',urlparse(root), '\n')

root = urlparse(root)
root = '://'.join([root.scheme, root.netloc])
print('get root URL: {}'.format(root))

url = root + image[0]['src']
print('get image absolute path: {}'.format(url))

with open('logo.svg', 'wb') as f:
    _ = requests.get(url, stream=True)
    for block in _.iter_content(512):
        if not block:
            break
        f.write(block)

urlretrieve(url, 'logo2.svg')

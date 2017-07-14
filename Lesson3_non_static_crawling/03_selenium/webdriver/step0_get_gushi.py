import requests
from bs4 import BeautifulSoup
from pprint import pprint


url = 'https://gushi.tw'
response = requests.get(url)
#soup = BeautifulSoup('<div class="t-inside style-color-xsdn-bg animate_when_almost_visible bottom-t-top start_animation"><div class="t-entry-visual" tabindex="0"><div class="t-entry-visual-tc"><div class="t-entry-visual-cont"><div class="dummy" style="padding-top: 56.25%;"></div><a tabindex="-1" href="https://gushi.tw/the-martial-law-period/" class="pushed" target="_self"><div class="t-entry-visual-overlay"><div class="t-entry-visual-overlay-in style-dark-bg" style="opacity: 0.01;"></div></div><div class="t-overlay-wrap"> <div class="t-overlay-inner"> <div class="t-overlay-content"> <div class="t-overlay-text single-block-padding"><div class="t-entry t-single-line"></div></div></div></div></div><img src="https://gushi.tw/wp-content/uploads/6257130_812cd803d4_o-uai-1024x576.jpg" width="1024" height="576" alt=""></a></div></div></div><div class="t-entry-text"> <div class="t-entry-text-tc single-block-padding"><div class="t-entry"><h3 class="t-entry-title h6"><a href="https://gushi.tw/the-martial-law-period/">那段不准與學校起衝突的過去，將威權的種子就此埋入每個學生的心底</a><div class="line"></div></h3><div class="t-entry-excerpt"><div class="pf-content"><p>有好長的一段時間，我都一直以為，在解嚴之前的法院是完全不運作的。</p></div></div></div></div></div></div>', 'lxml')
soup = BeautifulSoup(response.text, 'lxml')
pprint(soup.find_all('div', class_='t-inside style-color-xsdn-bg animate_when_almost_visible bottom-t-top start_animation'))


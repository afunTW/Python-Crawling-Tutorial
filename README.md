# Python 爬蟲實戰

## 下載程式與投影片
1. 請於上課前下載好[投影片](https://goo.gl/CFR95x)與程式碼，程式碼可透過這個頁面右邊的 **Clone or download** 下載
![demo](https://user-images.githubusercontent.com/4820492/29063516-c03b2c9c-7c58-11e7-9ba1-a6c2c0f62f7b.png)

## 課前準備: 強烈建議安裝 Anaconda
- 建議下載 Python 3.6 版本 https://www.continuum.io/downloads
- 本課程會使用到瀏覽器 Chrome，麻煩各位選擇自己電腦的平台安裝 Chrome https://www.google.com.tw/chrome/browser/desktop/index.html
- 本課程的 Session A & B 會使用到 jupyter notebook 進行，會提供 .ipynb 檔案，在安裝完 Anaconda 後即可用內建 jupyter notebook 打開 .ipynb 檔
- 本課程會用到的套件較多，建議安裝 Anaconda，如有安裝 Anaconda 只需安裝以下套件

```
pip install selenium tldextract Pillow
```

**optional** <small>- for 資料分析，沒有練習題，可自行選擇是否安裝</small>
```
pip install jieba wordcloud
```

---

- 若無安裝 Anaconda 則須按照您的環境安裝以下套件

```
pip3 install requests beautifulsoup4 lxml Pillow selenium tldextract
```

**optional** <small>- for 資料分析，沒有練習題，可自行選擇是否安裝</small>

```
pip3 install numpy pandas matplotlib scipy scikit-learn jieba wordcloud 
```

由於大家環境都不太相同，如果安裝上有任何問題歡迎來信詢問
- Cheng-Kun Yang：[jimmy15923@iis.sinica.edu.tw](jimmy15923@iis.sinica.edu.tw)
- Chen-Ming Yang：[afun@iis.sinica.edu.tw](afun@iis.sinica.edu.tw)

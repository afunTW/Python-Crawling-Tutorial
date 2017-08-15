# Python 爬蟲實戰

## 下載程式與投影片
1. 請於上課前下載好[投影片](https://goo.gl/CFR95x)與程式碼，程式碼可透過這個頁面右邊的 **Clone or download** 下載
![demo](https://user-images.githubusercontent.com/4820492/29063516-c03b2c9c-7c58-11e7-9ba1-a6c2c0f62f7b.png)

## 課前準備: 強烈建議安裝 Anaconda
- 建議下載 Python 3.6 版本 https://www.continuum.io/downloads
- 本課程會使用到瀏覽器 Chrome，麻煩各位選擇自己電腦的平台安裝 Chrome https://www.google.com.tw/chrome/browser/desktop/index.html
- 本課程的 Session A & B 會使用到 jupyter notebook 進行，會提供 .ipynb 檔案，在安裝完 Anaconda 後即可用內建 jupyter notebook 打開 .ipynb 檔，詳細教學可以參考資料夾中的 jupyter_notebook教學.pdf
- 本課程會用到的套件較多，建議安裝 Anaconda，如有安裝 Anaconda 只需安裝以下套件

```
pip install selenium tldextract Pillow
```

**optional** <small>- for 資料分析，沒有練習題但會有範例 code 可以執行，可自行選擇是否安裝 (如果安裝 wordcloud 時有問題，可能是沒有下載 visual studio，可以從 warining 中提供的網址下載安裝)</small>
```
pip install jieba wordcloud
```

---

- 若無安裝 Anaconda 則須按照您的環境安裝以下套件

```
pip3 install requests beautifulsoup4 lxml Pillow selenium tldextract
```

**optional** <small>- for 資料分析，沒有練習題但會有範例 code 可以執行，可自行選擇是否安裝</small>

```
pip3 install numpy pandas matplotlib scipy scikit-learn jieba wordcloud
```

由於大家環境都不太相同，如果安裝上有任何問題歡迎來信詢問
- 楊証琨 Cheng-Kun Yang：[jimmy15923@iis.sinica.edu.tw](jimmy15923@iis.sinica.edu.tw)
- 楊鎮銘 Chen-Ming Yang：[afun@iis.sinica.edu.tw](afun@iis.sinica.edu.tw)

## Q&A

**Q: 有哪些常用的 API**

課堂中有說到，爬蟲只是一種得到資料的手段，如果對方有提供 API 就可以直接使用 API，
API 通常對方都會幫你整理好資料格式，或是根據權限決定你可以獲取的資料內容
- [Facebook Graph API](https://developers.facebook.com/tools/explorer/)
- [Youtube](https://www.youtube.com/yt/dev/zh-TW/api-resources.html)
- [Yahoo YQL](https://developer.yahoo.com/yql/)
- [Instagram](https://www.instagram.com/developer/)
- [KKTIX](http://support.kktix.com/knowledgebase/articles/558918-%E6%B4%BB%E5%8B%95%E8%B3%87%E8%A8%8A-api)

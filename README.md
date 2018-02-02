# Python-Crawling-Tutorial 基礎爬蟲實戰

## 相關資源

最新的投影片放在 [slideshare](https://www.slideshare.net/ChenMingYang/python-crawling-tutorial) 上, 會不定期更新, 程式碼可透過這個頁面右邊的 **Clone or download** 下載
![demo](https://user-images.githubusercontent.com/4820492/35319787-585ea0c4-011c-11e8-802a-02ae0dbc4044.png)

> 2017 年以前的投影片教材放在 [release](https://github.com/afunTW/Python-Crawling-Tutorial/releases), 但是部份實戰練習網站會失效
> 或是可透過 [link](https://goo.gl/CFR95x) 下載投影片

## 安裝環境

### Anaconda (建議)

- 下載 Python 3.6 版本 https://www.continuum.io/downloads
- 本課程會使用到瀏覽器 Chrome，麻煩各位選擇自己電腦的平台安裝 Chrome https://www.google.com.tw/chrome/browser/desktop/index.html
- 本課程的 Session A & B 將提供 .ipynb 檔案使用 jupyter notebook 進行，安裝完 Anaconda 後即可用內建 jupyter notebook 打開 .ipynb 檔，詳細教學可以參考資料夾中的 jupyter_notebook教學.pdf
- 本課程會用到的套件較多，建議安裝 Anaconda，如有安裝 Anaconda 只需安裝以下套件

```sh
$ pip install selenium tldextract Pillow
```

### pip

pip 是 Python 的套件管理系統，在部份系統裏面會用 `pip3` 代表 Python3 的版本，請各位依照自己的系統安裝 pip3 後，安裝以下 Python3 版本的套件

```sh
# 視情況而定, 使用 pip 或是 pip3
$ pip install requests beautifulsoup4 lxml Pillow selenium tldextract
```

#### Optional: 資料分析

沒有練習題但會有範例 code 可以執行，可自行選擇是否安裝 (如果安裝 wordcloud 時有問題，可能是沒有下載 visual studio，可以從 warining 中提供的網址下載安裝)

```sh
# Anaconda
$ pip install jieba wordcloud

# pip
$ pip3 install numpy pandas matplotlib scipy scikit-learn jieba wordcloud
```

## 請遵守別人的規則

有些網站會在目錄底下加上 robots.txt, 基本上這就是對方定義的爬蟲規則，請大家在練習爬蟲的時候要尊重對方的規則

> robots.txt 詳細的語法與用途請參考 [wiki](https://zh.wikipedia.org/zh-tw/Robots.txt) 與 [google 文件](https://support.google.com/webmasters/answer/6062608?hl=zh-Hant)

---

## Q&A

**Q: 有哪些常用的 API**

課堂中有說到，爬蟲只是一種得到資料的手段，如果對方有提供 API 就可以直接使用 API，
API 通常對方都會幫你整理好資料格式，或是根據權限決定你可以獲取的資料內容

- [Facebook Graph API](https://developers.facebook.com/tools/explorer/)
- [Youtube](https://www.youtube.com/yt/dev/zh-TW/api-resources.html)
- [Yahoo YQL](https://developer.yahoo.com/yql/)
- [Instagram](https://www.instagram.com/developer/)
- [KKTIX](http://support.kktix.com/knowledgebase/articles/558918-%E6%B4%BB%E5%8B%95%E8%B3%87%E8%A8%8A-api)
- [Google Maps API](https://developers.google.com/maps/?hl=zh-tw)
- [Taipei Open Data API](http://data.taipei/opendata/developer)
- [Imgur API](https://api.imgur.com/endpoints)

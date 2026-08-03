

# Python-Crawling-Tutorial Basic Web Scraping Practice

## Related Resources

The latest slides are available on [slideshare](https://www.slideshare.net/ChenMingYang/python-crawling-tutorial-87165481). They will be updated irregularly. The code can be downloaded via the **Clone or download** button on the right side of this page.
![demo](https://user-images.githubusercontent.com/4820492/35319787-585ea0c4-011c-11e8-802a-02ae0dbc4044.png)

> Slide materials prior to 2017 are stored in [release](https://github.com/afunTW/Python-Crawling-Tutorial/releases), but some practical exercise websites may no longer be active.
> Alternatively, you can download the slides via [link](https://goo.gl/CFR95x).

## Environment Setup

### Anaconda (Recommended)

- Download Python 3.6 version from https://www.continuum.io/downloads
- The exercises will use the Chrome browser. Please select your computer's platform to install [Chrome](https://www.google.com.tw/chrome/browser/desktop/index.html).
- Crawlers for dynamic websites also require a webdriver, which needs to be downloaded separately:
    - [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    - [Firefox](https://github.com/mozilla/geckodriver/releases)
- All exercises are conducted using `jupyter notebook`. After installing Anaconda, you can use the built-in `jupyter notebook` to open `.ipynb` files.
- It is recommended to install Anaconda. If you have installed Anaconda, you only need to install the following packages:

```sh
$ pip install selenium tldextract Pillow
```

### pip

`pip` is Python's package management system. On some systems, `pip3` is used to represent the Python 3 version. After installing `pip3` according to your system, install the following Python 3 packages:

```sh
# Depending on your system, use pip or pip3
$ pip install requests beautifulsoup4 lxml Pillow selenium tldextract
```

#### Optional: Data Analysis

There are no exercises for this, but example code is available for execution. Installation is optional. (If you encounter issues installing `wordcloud`, it might be because Visual Studio is not installed. You can download and install it from the URL provided in the warning message.)

```sh
# Anaconda
$ pip install jieba wordcloud

# pip
$ pip3 install numpy pandas matplotlib scipy scikit-learn jieba wordcloud
```

## Please Follow Others' Rules

Some websites include a `robots.txt` file in their root directory. This essentially defines the crawling rules set by the site owner. Please respect these rules when practicing web scraping.

> For detailed syntax and usage of `robots.txt`, please refer to the [wiki](https://zh.wikipedia.org/zh-tw/Robots.txt) and [Google documentation](https://support.google.com/webmasters/answer/6062608?hl=zh-Hant).

---

## Q&A

**Q: What are some commonly used APIs?**

As mentioned in the course, web scraping is just one method of obtaining data. If the target site provides an API, you can use it directly.
APIs usually provide data in a pre-formatted structure, or determine the data you can access based on your permissions.

- [Facebook Graph API](https://developers.facebook.com/tools/explorer/)
- [YouTube](https://www.youtube.com/yt/dev/zh-TW/api-resources.html)
- [Yahoo YQL](https://developer.yahoo.com/yql/)
- [Instagram](https://www.instagram.com/developer/)
- [KKTIX](http://support.kktix.com/knowledgebase/articles/558918-%E6%B4%BB%E5%8B%95%E8%B3%87%E8%A8%8A-api)
- [Google Maps API](https://developers.google.com/maps/?hl=zh-tw)
- [Taipei Open Data API](http://data.taipei/opendata/developer)
- [Imgur API](https://api.imgur.com/endpoints)

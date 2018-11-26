import requests,os,bs4

url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)

while not url.endswith('#'):
    #下载网页
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    #寻找并下载漫画
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
        print('Downloading image %s...' % (comicUrl))
        try:
            res = requests.get('http:' + comicUrl)
        except Exception as e:
            print(e)
    
    #保存至文件夹中
    imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    #切换到前一个页面
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com/' + prevLink.get('href')


print('Done')
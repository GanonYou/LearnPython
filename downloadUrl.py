import requests,bs4,os

os.makedirs('seu_html',exist_ok=True)

res = requests.get('http://seugs.seu.edu.cn/3720/list.htm')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'lxml')
urlElems = soup.select('table[class="wp_article_list_table"] a')

for elem in urlElems:
    print(elem.attrs)
    htmlUrl = 'http://seugs.seu.edu.cn' + elem.get('href')
    htmlRes = requests.get(htmlUrl)
    htmlRes.raise_for_status()

    htmlName = elem.get('title')
    htmlFile = open(os.path.join('seu_html',htmlName),'wb')
    for chunk in htmlRes.iter_content(100000):
        htmlFile.write(chunk)
    htmlFile.close()

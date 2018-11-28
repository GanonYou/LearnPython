import requests,os,bs4

os.makedirs('imgur',exist_ok=True)

keywords = 'pokemon pikachu'
url = 'https://imgur.com/search/score/all?q_type=png&q_all=' + keywords

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
imageElems = soup.select('div[class="cards"] a')
for elem in imageElems:
   imageUrl = 'https://i.imgur.com/' + os.path.basename(elem.get('href')) + '.png'
   print('Downloading image from %s...' % (imageUrl))
   try:
       imageRes = requests.get(imageUrl)
   except Exception as e:
       print(e)

   imageFile = open(os.path.join('imgur',os.path.basename(imageUrl)),'wb')
   for chunk in imageRes.iter_content(100000):
       imageFile.write(chunk)
   imageFile.close()

print('Done.')
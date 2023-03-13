html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk web sayfam</title>
</head>
<body>
     <h1>
        Python Kursu
    </h1> id="header"
    <div class="grup1">
        <h2>
            Programlama
        </h2>
        <ul>
            <li>Menü1</li>
            <li>Menü2</li>
            <li>Menü3</li>
        </ul>
    </div>
    <div class="group2">
        <h2>
            Modüller
        </h2>
        <ul>
            <li>Menü1</li>
            <li>Menü2</li>
            <li>Menü3</li>
        </ul>
    </div>
    <div class="group3">
        <h2>
            Django
        </h2>
        <ul>
            <li>Menü1</li>
            <li>Menü2</li>
            <li>Menü3</li>
        </ul>
    </div>
    <img src="kedi.jpg" alt="">
    [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
</body>
</html>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,'html.parser')

result = soup.prettify()
result = soup.title
result = soup.body
result = soup.title.name
result = soup.title.string

result = soup.h1
result = soup.h2

result = soup.h1.name
result = soup.h1.string
result = soup.h2.name
result = soup.h2.string

result = soup.find_all('h2')
result = soup.find_all('h2')[0]
result = soup.find_all('h2')[1]

result = soup.div
result = soup.find_all('div')[1]   #to reach second division
result = soup.find_all('div')[1].ul.find_all('li')

result = soup.div.findChildren()  #to reach first divisions all subgroup

result = soup.div.findNextSibling()  #to reach second divisions all subgroup

result = soup.div.findNextSibling().findNextSibling()

result = soup.find_all('a')

for link in result:
    print(link.get('href'))




print(result)

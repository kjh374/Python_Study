from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector
from datetime import datetime
import codecs


service = webdriver.ChromeService(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(service=service, options=options)
browser.get('https://www.melon.com/chart/index.htm')
browser.implicitly_wait(5)

'''
- with문을 사용하면 with 블록을 벗어나는 순간
 객체가 자동으로 해제됩니다. (자바의 try with resource와 비슷)

 - with 작성 시 사용할 객체의 이름을 as 뒤에 작성해 줍니다.
'''

d = datetime.today()

file_path = f'C:/test/melon chart100_{d.year}_{d.month}_{d.day}.txt'


mydb = mysql.connector.connect(
    host ='localhost',
    database ='jpa',
    user ='root',
    password ='mysql'
)

mycursor = mydb.cursor()

with codecs.open(file_path, mode='w', encoding='utf-8') as f:


    soup = BeautifulSoup(browser.page_source, 'html.parser')

    lst50 = soup.find_all('tr', class_='lst50')
    lst100 = soup.find_all('tr', class_='lst100')

    for n in lst50:
    
        # 순위
        rank = n.select_one('tr span.rank').text
        print(rank)

        # 노래제목
        title = n.select_one('div.rank01 a').text
        print(title)

        # 가수
        singer = n.select_one('div.rank02').text
        print(singer)
        
        print('-' * 40)

        f.write(f'순위:{rank}')
        f.write(f'제목:{title}')
        f.write(f'가수:{singer}')

        # query = 'INSERT INTO tbl_melon (rank, title, singer) VALUES(%s, %s, %s)'
        # values = (rank, title, singer)

        # mycursor.execute(query, values)

    for n in lst100:
    
        # 순위
        rank = n.select_one('tr span.rank').text
        print('순위:', rank)

        # 노래제목
        title = n.select_one('div.rank01 a').text
        print('제목:', title)

        # 가수
        singer = n.select_one('div.rank02').text
        print('가수:', singer ) 

        print('-' * 40)
        

        f.write(f'순위:{rank}')
        f.write(f'제목:{title}')
        f.write(f'가수:{singer}')

        # query = 'INSERT INTO tbl_melon (rank, title, singer) VALUES(%s, %s, %s)'
        # values = (rank, title, singer)

        # mycursor.execute(query, values)

browser.close()

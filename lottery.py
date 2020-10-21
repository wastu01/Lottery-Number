
import requests
import re
from bs4 import BeautifulSoup

url  = requests.get('http://www.taiwanlottery.com.tw/index_new.aspx')
soup = BeautifulSoup(url.text,'html.parser')
'''開獎時間 and 第幾期'''
date    = []
periods = []
for num in soup.select('span'):
	match = re.search(r'<span class="font_black15">(.*?)(.*?)</span>',str(num))
	if match:
		date.append(match.group(1))
		periods.append(match.group(2))

#正規表達式
# . >> 配對除了 '\n' 之外的任何字元
# \w >> 任意字元，含數字
# ? 0或1次

#http://kaiching.org/pydoing/py/python-library-re.html
#https://ithelp.ithome.com.tw/articles/10194954
#儲存group，之後提出



'''special_ball 特別號'''
special_ball = []
for div in soup.select('div'):
	match = re.search(r'^<div class="ball_red">(.*?)<',str(div))
	if match:
		special_ball.append(match.group(1))

def wiili():
	wiili_1 = []
	wiili_2 = []
	n = 0
	for div in soup.select('div'):
		match = re.search('^<div class="ball_tx ball_green">(.*?)<',str(div))
		if match:
			n += 1
			if n <= 6:
				wiili_1.append(match.group(1))
			elif 6 < n <= 12:
				wiili_2.append(match.group(1))
	print("------------------威力彩------------------")
	print("-----------------38樂合彩-----------------")
	print(date[1],periods[1])
	print('開出順序：',' '.join(wiili_1))
	print('大小順序：',' '.join(wiili_2))
	print('第二區號碼：         ',int(special_ball[1]))
	print("-----------------這是虛線------------------")
	print("***********買彩券、做公益、積功德************")




wiili()

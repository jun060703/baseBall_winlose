#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


sel = webdriver.Chrome()
act = ActionChains(sel)
sel.get('https://www.koreabaseball.com/Schedule/Schedule.aspx')

select = Select(sel.find_element(By.ID, 'ddlSeries'))
select.select_by_index(1)
select = Select(sel.find_element(By.ID, 'ddlMonth'))
game_data = []

for i in range(3, 10):
    select.select_by_index(i)

    # 페이지 로딩을 위해 충분한 시간 대기
    time.sleep(3)  # 3초 대기 (필요에 따라 조절)

    soup = BeautifulSoup(sel.page_source, 'html.parser')
    play = soup.find_all(class_='play')

    for element in play:
        text_data = element.get_text()
        print(text_data)
        game_data.append(text_data)
# 데이터를 데이터프레임으로 변환
df = pd.DataFrame(game_data, columns=['Day_play'])
df.to_csv('kbo_record.csv', index=False)

sel.quit()

# -*- coding: utf-8 -*-
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# 웹 드라이버 초기화
sel = webdriver.Chrome()
sel.get('https://www.koreabaseball.com/Record/Player/HitterBasic/BasicOld.aspx?sort=HRA_RT')

select_series = Select(sel.find_element(By.ID, 'cphContents_cphContents_cphContents_ddlSeries_ddlSeries'))
select_series.select_by_index(0)  

# 데이터 수집
gameRecord_data = []

# 여러 팀 선택
values_to_select = ['OB', 'LT', 'SS', 'WO', 'HH', 'HT', 'KT', 'LG', 'NC', 'SK']

for value in values_to_select:
    select = Select(sel.find_element(By.ID, 'cphContents_cphContents_cphContents_ddlTeam_ddlTeam'))
    select.select_by_value(value)

    # 페이지 로딩 대기 시간
    time.sleep(3)

    # 데이터 수집
    soup = BeautifulSoup(sel.page_source, 'html.parser')
    paragraphs = soup.find_all('tr')
    for tr in paragraphs:
        gameRecord_data.append(tr.text)

# WebDriver 종료
sel.quit()

# 데이터를 DataFrame에 저장하고 CSV 파일로 출력
df = pd.DataFrame(gameRecord_data, columns=['playerRecord_play'])
df.to_csv('kbo_record_player.csv', index=False)

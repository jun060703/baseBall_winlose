# -*- coding: utf-8 -*-
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# 웹 드라이버 초기화
sel = webdriver.Chrome()
sel.get('https://www.koreabaseball.com/Record/Player/PitcherBasic/Basic1.aspx')

select_series = Select(sel.find_element(By.ID, 'cphContents_cphContents_cphContents_ddlSeries_ddlSeries'))
select_series.select_by_index(0)  #인덱스 0만 선택함

# csv에 넣을 데이터의 변수를 만들어줌
gameRecord_data = []

# 여러 팀을 선택하기 위해서
values_to_select = ['OB', 'LT', 'SS', 'WO', 'HH', 'HT', 'KT', 'LG', 'NC', 'SK']
#for문을 돌린다
for value in values_to_select:
    select = Select(sel.find_element(By.ID, 'cphContents_cphContents_cphContents_ddlTeam_ddlTeam'))
    print(select)
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
df = pd.DataFrame(gameRecord_data, columns=['playerRecord_pitcher_play'])
df.to_csv('kbo_record_pitcher.csv', index=False)

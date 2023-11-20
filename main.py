import pandas as pd

# CSV 파일 로드
data1 = pd.read_csv('kbo_record_pitcher.csv',encoding = "cp949")
data2 = pd.read_csv('kbo_record_player.csv',encoding = "cp949")
data3 = pd.read_csv('kbo_record.csv',encoding = "cp949")

# 데이터 확인
print(data1)
print(data2)
print(data3)

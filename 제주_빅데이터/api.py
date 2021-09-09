from urllib.request import urlopen 
import requests
import json 
import pandas as pd

api_key = 'your_api_key'
api_type = '043Y070'

'''    
    - 출처 : ECOS(한국은행, 신용카드), 2020.07.12.
    - 자료 : ECOS(한국은행)>지급결제>신용카드, 2020.07.12.
'''

location = {
    "전국":"X",
    "서울":"X",
    "부산":"B",
    "대구":"C",
    "인천":"D",
    "광주":"E",
    "대전":"F",
    "울산":"G",
    "경기":"L",
    "강원":"M",
    "충북":"N",
    "충남":"P",
    "전북":"Q",
    "전남":"R",
    "경북":"S",
    "경남":"T",
    "제주":"U",
    "기타":"Z"
}

work_type = {
"합계":"1000",
"종합소매":"1100",
"백화점":"1110",
"대형마트/유통전문점":"1120",
"슈퍼마켓":"1130",
"편의점":"1140",
"면세점":"1150",
"전자상거래/통신판매":"1200",
"식료품":"1300",
"일반식료품":"1310",
"건강보조식품":"1320",
"의류/잡화":"1400",
"의복/직물":"1410",
"복식잡화":"1420",
"시계/귀금속/안경":"1430",
"화장품":"1440",
"연료":"1500",
"가구/가전":"1600",
"가구":"1610",
"가전제품/정보통신기기":"1620",
"의료/보건":"1700",
"종합병원":"1710",
"일반병의원/기타의료기관":"1720",
"자동차":"1800",
"국산자동차신품":"1810",
"기타운송수단":"1820",
"자동차 부품 및 정비":"1830",
"여행/교통":"1900",
"여행사/자동차임대":"1910",
"항공사":"1920",
"대중교통":"1930",
"오락/문화":"2000",
"스포츠/오락/여가":"2010",
"서적/문구":"2020",
"교육":"2100",
"숙박/음식":"2200",
"공과금/개인 및 전문 서비스":"2300",
"금융/보험":"2400",
"기타":"2500",
}

result_type ={
    "총액":"TOT",
    "일평균":"DAV"
}


base_url = "http://ecos.bok.or.kr/api/StatisticSearch/" + api_key + "/json/kr/1/200/" + api_type + "/MM/201901/202008/"

# + location['전국'] + "/" + work_type["합계"] + "/" + result_type["총액"]

d = {'날짜': ['0'], '위치': ['0'], '업종': ['0'], '매출': ['0']}
df = pd.DataFrame(data=d)

file_index = 0
for loc in location:
    for wk in work_type:
        file_index+=1
        url = base_url + location[loc] + "/" + work_type[wk] + "/" + "TOT"

        json = requests.get(url).json()
        for index in range(16):
            df2 = {
                "날짜":json['StatisticSearch']['row'][index]['TIME'],
                "위치":loc,
                "업종":wk,
                "매출":json['StatisticSearch']['row'][index]['DATA_VALUE']
            }
            df = df.append(df2,ignore_index=True)
            print(index)
        #중간에 종료되는 경우 때문에 중간 결과 저장
        df.to_csv('output'+str(file_index)+'.csv') 
    

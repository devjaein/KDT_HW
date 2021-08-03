# 엑셀에 데이터를 저장하기 위한 모듈
from openpyxl import Workbook

# 웹에서 데이터를 크롤링하기 위한 모듈
import requests
from bs4 import BeautifulSoup
class NaverNewsCrawler:
    search_url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
    def __init__(self, keyword):
        self.keyword = keyword
        self.search_url += keyword
    def get_news(self, file_name):
        req = requests.get(self.search_url)
        if req.status_code != requests.codes.ok:
            print("사이트 접속 실패 인터넷 상태를 확인하거나, 키워드를 확인하세요.")
            return None
        print(f"{self.keyword}에 대한 기사 수집 시작")
        html = BeautifulSoup(req.text, "html.parser")
        news_items = html.select("div.group_news > ul > li")
        wb = Workbook()
        ws = wb.active
        ws.append(['번호','제목','주소','요약'])
        for index, item in enumerate(news_items, start=1):
            title_tag = item.select_one('a.news_tit')
            title = title_tag.text
            url = title_tag.attrs['href']
            description = item.select_one('div.news_dsc').text if len(item.select_one('div.news_dsc').text) >= 3 else "요약 정보 없음"
            print(index, title, url, description)
            ws.append([index, title, url, description])
        try:
            wb.save(file_name)
            print(f"{file_name}에 데이터 저장 완료")
        except Exception as e:
            print(e)
        print(f"{self.keyword}에 대한 기사 수집 완료")

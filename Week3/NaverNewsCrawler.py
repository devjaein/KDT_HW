# 시트 에러 처리
from openpyxl.utils.exceptions import CellCoordinatesException, IllegalCharacterError, InvalidFileException, NamedRangeException, ReadOnlyWorkbookException, SheetTitleException, WorkbookAlreadySaved

# 엑셀에 데이터를 저장하기 위한 모듈
from openpyxl import Workbook
import openpyxl

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
            print(f"{self.keyword}에 대한 기사 수집 완료")
        except CellCoordinatesException:
            print("숫자 및 셀 참조 간에 변환하는 동안 오류 발생")
        except IllegalCharacterError:
            print("직접 사용할 수 없는 제출 데이터로 제거하거나 이스케이프 해야합니다.")
        except InvalidFileException: #
            print("oomclm이 아닌 파일을 열려고 시도하는 동안 오류 발생")
        except NamedRangeException:
            print("형식이 잘못된 명명된 범위에 대한 오류")
        except ReadOnlyWorkbookException: #
            print("읽기 전용 통합 문서를 수정하는 동안 오류 발생")
        except SheetTitleException:
            print("잘못된 시트 이름에 대한 오류")
        except WorkbookAlreadySaved:
            print("이미 한 번 덤프된 덤프 통합 문서에서 작업을 수행할 때 오류 발생")
        except Exception as e:
            print(e)

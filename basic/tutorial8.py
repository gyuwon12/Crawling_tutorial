# 엑셀을 불러오고 수정해보는 예제
import openpyxl

fpath = r"/Users/gyuwonpark/Desktop/Crawling/기본/참가자_data.xlsx"

# 1) 엑셀 불러오기
wb = openpyxl.load_workbook(fpath)

# 2) 엑셀 시트 선택
work_sheet = wb['오징어게임']

# 3) 데이터 수정하기
work_sheet['A3'] = 456
work_sheet['B3'] = "성기훈"

# 4) 엑셀 저장하기
wb.save(fpath)
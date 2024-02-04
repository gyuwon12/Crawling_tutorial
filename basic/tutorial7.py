# 엑셀 저장해보는 예제

import openpyxl

# 1) 엑셀 만들기
wb = openpyxl.Workbook()

# 2) 엑셀 워크 시트 만들기
work_sheet = wb.create_sheet('오징어게임') # 이건 시트 이름

# 3) 데이터 추가하기
work_sheet['A1'] = '참가번호'
work_sheet['B1'] = '성명'
work_sheet['A2'] = 1
work_sheet['B2'] = '오일남'

# 4) 엑셀 저장하기
wb.save(r'/Users/gyuwonpark/Desktop/Crawling/기본/참가자_data.xlsx') # r을 붙이면 모두 문자열 취급을 해라 이런 뜻
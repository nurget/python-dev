#!/usr/bin/env python3

# 라이브러리를 읽어들임
import sys
import urllib.request as req
import urllib.parse as parse

# import 구문에 as를 지정하면 모듈을 원하는 이름으로 사용 가능
# 이 파일 내에서는 urllib.request가 req, urllib.parse를 parse라는 이름으로 선언

# 명령줄 매개변수 추출
if len(sys.argv) <= 1:
    print("USAGE: download-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

# 매개변수를 URL 인코딩
# 지금은 숫자만 입력하기 때문에 필요없지만 한국어 등을 사용할 때는 필수
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId' : regionNumber
}
params = parse.urlencode(values)
url = API + "?" + params
print("url=", url)

# 다운로드합니다.
data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)
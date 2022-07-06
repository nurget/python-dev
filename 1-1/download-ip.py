# IP 확인 API로 접근해서 결과 출력하기
# 모듈 읽어 들이기
import urllib.request

# 데이터 읽어 들이기
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

# 바이너리를 문자열로 변환하기
text = data.decode("utf-8")
print(text)

# decode() 메서드를 사용해 바이너리를 문자열로 변환
# FTP 상의 리소스를 추출하고 싶으면 request.urlopen()에 지정한 URL을 "http://"에서 "ftp://"로 변경
import urllib.request

# URL과 저장 경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# 다운로드
mem = urllib.request.urlopen(url).read()

# urlopen() 함수로 PNG 파일의 URL 리소스를 열고 read() 메서드로 데이터를 읽어들임. 

# 파일로 저장하기
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다...!")

# mode "wb"에서 "w"는 쓰기 모드, "b"는 바이너리 모드
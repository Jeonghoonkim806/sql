import requests                # api 호출 패키지
from bs4 import BeautifulSoup  # json 혹은 parsing하는 패키지

api_key = 'zE7MopmnIFIpiJJkBW4x4tEdBoZJnqF8eGE2154UxFVUnol1Lmfmnu1nXaad%2BG74KTXbAxSkPNs%2FTkOmRVUI%2Fg%3D%3D'
base_request_url = f'http://apis.data.go.kr/9720000/searchservice/basic?serviceKey={api_key}&pageno=1&displaylines=10&search=자료명,미국'

response = requests.get(base_request_url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup.prettify())
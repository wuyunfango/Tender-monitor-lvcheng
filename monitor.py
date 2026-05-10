import requests
from bs4 import BeautifulSoup

url = "https://lczc.gtcloud.cn/portal/biding"

response = requests.get(url)

print(response.status_code)
print("Website checked successfully")

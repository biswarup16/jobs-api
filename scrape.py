from bs4 import BeautifulSoup
import requests

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    content = soup.find("table",class_="table table-striped table-bordered")
    print(content.find("tbody").find("tr").find("td"))

get_free_proxies()
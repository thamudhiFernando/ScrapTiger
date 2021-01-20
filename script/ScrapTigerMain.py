import requests
from bs4 import BeautifulSoup

from script.ResultJson import ResultJson

class ScrapTigerMain(object):
    url = 'https://scarborough.tigeronlineorder.com/admin/parts_products2.php?hide_title=1'
    data = {"make": '40', "model": '1328', "year": '2019', "query": '', "customer": ''}
    json = {"Content-Type": 'application/x-www-form-urlencoded', "Cookie": 'PHPSESSID=0mcp9h09voim9oro4r2sb78m4l'}

    result = requests.post(url, data, json)
    src = result.content
    soup = BeautifulSoup(src, "html.parser")
    ResultJson(soup)
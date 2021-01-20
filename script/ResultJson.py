import json

from bs4 import BeautifulSoup


class ResultJson():
    def __init__(self, BeautifulSoup):
        result_page = BeautifulSoup.find('div', attrs={'id': 'res-wrap'})

        # create jSON
        jsonArray = {
            "searchResults": tabletopper(result_page),
            "table": [
                tableheaders(result_page),
                tablebody(result_page)
            ]
        }

        print('json --- >', json.dumps(jsonArray))


def tabletopper(BeautifulSoup):
    spanlist = BeautifulSoup.findAll('span', class_='pglnks2 f15')
    searchResults = []
    for span in spanlist:
        searchResults.insert(len(searchResults) + 1, span.getText())

    return {"page": searchResults[0], "pageCount": searchResults[1]}

def tableheaders(BeautifulSoup):
    headerlist = BeautifulSoup.findAll('strong', class_='whiteText')
    tableheader = []
    for header in headerlist:
        tableheader.insert(len(tableheader) + 1, header.getText())

    return {
        "table_header_1": tableheader[0],
        "table_header_2": tableheader[1],
        "table_header_3": tableheader[2],
        "table_header4": tableheader[3],
        "table_header_5": tableheader[4]
    }

def tablebody(BeautifulSoup):
    trlist = BeautifulSoup.findAll('tr')
    dataset = {}
    for tro in trlist:
        datarow = []
        if(tro.find('td',class_='letter-header')):
            print(trlist.index(tro))
            dataset['letter-header'+ str(trlist.index(tro))] = tro.find('td',class_='letter-header').getText()
            continue

        if (tro.find('a', class_='fancybox')):
            datarow.insert(len(datarow) + 1, {"img" : [tro.find('a', class_='fancybox').find('img')['aa'],tro.find('a', class_='fancybox').find('img')['src']]})

        if (tro.find('a', class_='sku-pop')):
            datarow.insert(len(datarow) + 1, {"sku":tro.find('a', class_='sku-pop').getText()})

        if (tro.find('td',{ "headers" : "category"})):
            datarow.insert(len(datarow) + 1, {"description" : tro.find('td',{ "headers" : "category"}).find('span').getText()})

        if (tro.find('td',{ "axis" : "sstring" , "headers" : "" })):
            datarow.insert(len(datarow) + 1,{"listPrice": tro.find('td',{ "axis" : "sstring" , "headers" : ""}).getText()})

        dataset['datarow' + str(len(dataset)+1)] = datarow

    return dataset